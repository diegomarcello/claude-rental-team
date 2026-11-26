#!/usr/bin/env python3
"""Owner payout for Brazil. Spec: references/calculation-spec-brazil.md. Standard library only."""
import argparse
import json
import sys
from datetime import date, timedelta
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

CENT = Decimal("0.01")


def money(text):
    try:
        value = Decimal(text)
    except InvalidOperation:
        raise argparse.ArgumentTypeError(f"valor invalido: {text!r} (use ponto decimal, ex.: 5000.00)")
    if not value.is_finite() or value < 0:
        raise argparse.ArgumentTypeError(f"o valor deve ser um numero nao negativo: {text!r}")
    return value


def cents(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def add_business_days(start, days, holidays):
    current = start
    while days > 0:
        current += timedelta(days=1)
        if current.weekday() < 5 and current not in holidays:
            days -= 1
    return current


def main(argv=None):
    p = argparse.ArgumentParser(description="Repasse liquido ao proprietario.")
    p.add_argument("--aluguel-recebido", type=money, required=True)
    p.add_argument("--taxa-adm-pct", type=money, required=True)
    p.add_argument("--taxa-intermediacao", type=money, default=Decimal(0))
    p.add_argument("--retencoes-irrf", type=money, default=Decimal(0))
    p.add_argument("--reparos-autorizados", type=money, default=Decimal(0))
    p.add_argument("--encargos-reembolsaveis", type=money, default=Decimal(0))
    p.add_argument("--dias-uteis-prazo", type=int, default=3)
    p.add_argument("--data-compensacao", type=date.fromisoformat)
    p.add_argument("--feriado", type=date.fromisoformat, action="append", default=[])
    a = p.parse_args(argv)
    if a.taxa_adm_pct > 100:
        p.error("--taxa-adm-pct nao pode passar de 100")
    if a.dias_uteis_prazo < 0:
        p.error("--dias-uteis-prazo nao pode ser negativo")

    fee = cents(a.aluguel_recebido * a.taxa_adm_pct / 100)
    discounts = fee + a.taxa_intermediacao + a.retencoes_irrf + a.reparos_autorizados
    net = cents(a.aluguel_recebido + a.encargos_reembolsaveis - discounts)
    warnings = []
    pay_date = None
    if a.data_compensacao:
        pay_date = add_business_days(a.data_compensacao, a.dias_uteis_prazo, set(a.feriado)).isoformat()
        if not a.feriado:
            warnings.append("Nenhum feriado informado: a data considera apenas fins de semana.")
    if net < 0:
        warnings.append("Saldo negativo: bloquear o repasse; compensar ou cobrar conforme company-context.md.")
    result = {
        "taxa_adm": str(fee),
        "total_descontos": str(cents(discounts)),
        "repasse_liquido": str(net),
        "valor_a_pagar": str(max(net, cents(Decimal(0)))),
        "saldo_devedor": str(cents(max(-net, Decimal(0)))),
        "status": "saldo_negativo_reter" if net < 0 else "liberar_pagamento",
        "data_pagamento_repasse": pay_date,
        "avisos": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
