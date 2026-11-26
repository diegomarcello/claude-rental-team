"""Run: python3 -m unittest discover -s tests

Cases come from the delivered calculation specs. Where a spec value is wrong, the test says so.
"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AR = ROOT / "finance/skills/accounts-receivable/scripts/accounts_receivable.py"
PAYOUT = ROOT / "finance/skills/owner-payouts/scripts/owner_payout.py"
LEASE = ROOT / "property-management/skills/lease-administration/scripts/lease_administration.py"
LOAN = ROOT / "sales/skills/financing-simulation/scripts/financing_simulation.py"


def run(script, *args):
    return subprocess.run([sys.executable, "-B", str(script), *args], capture_output=True, text=True)


class Base(unittest.TestCase):
    def ok(self, script, *args, **expected):
        proc = run(script, *args)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        for key, value in expected.items():
            self.assertEqual(data[key], value, key)
        return data

    def refused(self, script, *args, contains=""):
        proc = run(script, *args)
        self.assertEqual(proc.returncode, 2, proc.stdout)
        self.assertIn(contains, proc.stderr)


class OwnerPayout(Base):
    base = ("--aluguel-recebido", "5000.00", "--taxa-adm-pct", "10")

    def test_normal(self):
        self.ok(PAYOUT, *self.base, "--reparos-autorizados", "350", taxa_adm="500.00",
                repasse_liquido="4150.00", valor_a_pagar="4150.00", status="liberar_pagamento")

    def test_negative_balance(self):
        self.ok(PAYOUT, *self.base, "--reparos-autorizados", "6000", repasse_liquido="-1500.00",
                valor_a_pagar="0.00", saldo_devedor="1500.00", status="saldo_negativo_reter")

    def test_business_days_skip_weekend_and_holiday(self):
        # 2026-11-26 is a Thursday: D+3 is Tuesday 12-01, or Wednesday 12-02 with one holiday.
        self.ok(PAYOUT, *self.base, "--data-compensacao", "2026-11-26", data_pagamento_repasse="2026-12-01")
        self.ok(PAYOUT, *self.base, "--data-compensacao", "2026-11-26", "--feriado", "2026-11-30",
                data_pagamento_repasse="2026-12-02")

    def test_missing_fee_is_refused(self):
        self.refused(PAYOUT, "--aluguel-recebido", "5000", contains="--taxa-adm-pct")

    def test_invalid_numbers_are_refused(self):
        for bad in ("5.000,00", "-1", "NaN"):
            self.refused(PAYOUT, f"--aluguel-recebido={bad}", "--taxa-adm-pct", "10")


class Lease(Base):
    def test_adjustment(self):
        self.ok(LEASE, "reajuste", "--aluguel-atual", "3500.00", "--indice", "IPCA", "--variacao-pct", "4.62",
                novo_aluguel="3661.70", diferenca="161.70")

    def test_negative_index_keeps_rent(self):
        self.ok(LEASE, "reajuste", "--aluguel-atual", "3000", "--indice", "IGPM", "--variacao-pct=-1.20",
                novo_aluguel="3000.00")

    def test_negative_index_with_deflation(self):
        self.ok(LEASE, "reajuste", "--aluguel-atual", "3000", "--indice", "IGPM", "--variacao-pct=-1.20",
                "--permite-deflacao", novo_aluguel="2964.00")

    def test_prorated_fine(self):
        self.ok(LEASE, "multa", "--aluguel-atual", "3000", "--multa-alugueis", "3", "--prazo-total-meses", "30",
                "--meses-cumpridos", "12", multa_proporcional="5400.00")

    def test_fine_after_term_is_zero(self):
        self.ok(LEASE, "multa", "--aluguel-atual", "3000", "--meses-cumpridos", "30", multa_proporcional="0.00")

    def test_defaults_are_reported(self):
        data = self.ok(LEASE, "multa", "--aluguel-atual", "3000", multa_proporcional="9000.00")
        self.assertEqual(sum("Padrao aplicado" in w for w in data["avisos"]), 3)

    def test_missing_index_variation_is_refused(self):
        self.refused(LEASE, "reajuste", "--aluguel-atual", "3500", "--indice", "IPCA", contains="--variacao-pct")


class Receivables(Base):
    def args(self, paid, principal="2500.00"):
        return ("--valor-principal", principal, "--data-vencimento", "2026-11-05", "--data-pagamento", paid)

    def test_ten_days_late(self):
        self.ok(AR, *self.args("2026-11-15"), dias_atraso=10, multa="50.00", juros="8.33",
                valor_atualizado="2558.33", faixa="1_a_15_dias")

    def test_on_due_date(self):
        self.ok(AR, *self.args("2026-11-05"), dias_atraso=0, multa="0.00", juros="0.00",
                valor_atualizado="2500.00", faixa="em_dia")

    def test_early_payment(self):
        data = self.ok(AR, *self.args("2026-11-01"), dias_atraso=0, valor_atualizado="2500.00")
        self.assertTrue(any("antecipado" in w for w in data["avisos"]))

    def test_bucket_limits(self):
        for paid, name in (("2026-11-20", "1_a_15_dias"), ("2026-11-21", "16_a_30_dias"),
                           ("2026-12-05", "16_a_30_dias"), ("2026-12-06", "mais_de_30_dias")):
            self.ok(AR, *self.args(paid), faixa=name)


class Financing(Base):
    def args(self, rate="10.0", system="PRICE", income="15000.00", down="100000.00"):
        return ("--valor-imovel", "500000.00", "--valor-entrada", down, "--prazo-meses", "360",
                "--taxa-anual-pct", rate, "--sistema", system, "--renda-mensal", income)

    def test_price_ten_percent_effective_per_year(self):
        # The spec expects 3392.64 (22.62%). That is the 0.80% per month figure; 10% a year gives 3383.56.
        self.ok(LOAN, *self.args(), valor_financiado="400000.00", primeira_parcela="3383.56",
                comprometimento_pct="22.56", status="aprovado_renda")

    def test_price_above_income_limit(self):
        self.ok(LOAN, *self.args(income="10000.00"), comprometimento_pct="33.84", status="reprovado_limite_renda")

    def test_price_equivalent_to_080_percent_per_month(self):
        self.ok(LOAN, *self.args(rate="10.033869366"), primeira_parcela="3392.64")

    def test_sac(self):
        data = self.ok(LOAN, *self.args(system="SAC"), primeira_parcela="4300.77")
        self.assertLess(float(data["ultima_parcela"]), float(data["primeira_parcela"]))

    def test_zero_rate(self):
        self.ok(LOAN, *self.args(rate="0"), primeira_parcela="1111.11")

    def test_down_payment_covering_price_is_refused(self):
        self.refused(LOAN, *self.args(down="500000.00"), contains="saldo a financiar")


if __name__ == "__main__":
    unittest.main()
