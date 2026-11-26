#!/usr/bin/env python3
"""Late payment charges for Brazil. Spec: references/calculation-spec-brazil.md. Standard library only."""
import argparse
import json
import sys
from datetime import date
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

CENT = Decimal("0.01")


def money(text):
    try:
        value = Decimal(text)
    except InvalidOperation:
        raise argparse.ArgumentTypeError(f"valor invalido: {text!r} (use ponto decimal, ex.: 2500.00)")
    if not value.is_finite() or value < 0:
        raise argparse.ArgumentTypeError(f"o valor deve ser um numero nao negativo: {text!r}")
    return value


def cents(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def bucket(days):
    if days == 0:
        return "em_dia"
    if days <= 15:
        return "1_a_15_dias"
    if days <= 30:
        return "16_a_30_dias"
    return "mais_de_30_dias"


def main(argv=None):
    p = argparse.ArgumentParser(description="Encargos por atraso de aluguel.")
    p.add_argument("--valor-principal", type=money, required=True)
    p.add_argument("--data-vencimento", type=date.fromisoformat, required=True)
    p.add_argument("--data-pagamento", type=date.fromisoformat, required=True)
    p.add_argument("--multa-pct", type=money)
    p.add_argument("--juros-mensal-pct", type=money)
    p.add_argument("--correcao-pct", type=money, default=Decimal(0))
    a = p.parse_args(argv)

    warnings = []
    if a.multa_pct is None:
        a.multa_pct = Decimal(2)
        warnings.append("Padrao aplicado: multa de 2%. Confirme no contrato.")
    if a.juros_mensal_pct is None:
        a.juros_mensal_pct = Decimal(1)
        warnings.append("Padrao aplicado: juros de 1% ao mes. Confirme no contrato.")
    raw = (a.data_pagamento - a.data_vencimento).days
    if raw < 0:
        warnings.append("Pagamento antecipado: nenhuma multa ou juros; desconto nao previsto.")
    days = max(raw, 0)
    late = days > 0
    penalty = cents(a.valor_principal * a.multa_pct / 100) if late else cents(Decimal(0))
    interest = cents(a.valor_principal * a.juros_mensal_pct * days / 3000)
    correction = cents(a.valor_principal * a.correcao_pct / 100) if late else cents(Decimal(0))
    if late and a.correcao_pct and days < 30:
        warnings.append("Correcao aplicada com menos de 30 dias de atraso: confirme se o contrato permite.")
    result = {
        "dias_atraso": days,
        "faixa": bucket(days),
        "multa": str(penalty),
        "juros": str(interest),
        "correcao": str(correction),
        "valor_atualizado": str(cents(a.valor_principal + penalty + interest + correction)),
        "avisos": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
