#!/usr/bin/env python3
"""Rent adjustment and prorated termination fine for Brazil. Spec: references/calculation-spec-brazil.md."""
import argparse
import json
import sys
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

CENT = Decimal("0.01")


def number(text):
    try:
        value = Decimal(text)
    except InvalidOperation:
        raise argparse.ArgumentTypeError(f"valor invalido: {text!r} (use ponto decimal, ex.: 3500.00)")
    if not value.is_finite():
        raise argparse.ArgumentTypeError(f"valor invalido: {text!r}")
    return value


def non_negative(text):
    value = number(text)
    if value < 0:
        raise argparse.ArgumentTypeError(f"o valor nao pode ser negativo: {text!r}")
    return value


def cents(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def adjust(a):
    warnings = []
    factor = 1 + a.variacao_pct / 100
    if a.variacao_pct < 0 and not a.permite_deflacao:
        factor = Decimal(1)
        warnings.append("Indice negativo sem deflacao autorizada: aluguel mantido. Confirme a clausula do contrato.")
    if factor <= 0:
        raise ValueError("a variacao informada zera ou torna negativo o aluguel")
    new = cents(a.aluguel_atual * factor)
    warnings.append("Confirme a periodicidade minima anual e a variacao acumulada na fonte oficial do indice.")
    return {"indice": a.indice, "novo_aluguel": str(new), "diferenca": str(cents(new - a.aluguel_atual)),
            "avisos": warnings}


def fine(a):
    warnings = []
    if a.multa_alugueis is None:
        a.multa_alugueis = Decimal(3)
        warnings.append("Padrao aplicado: multa de 3 alugueis. Confirme no contrato.")
    if a.prazo_total_meses is None:
        a.prazo_total_meses = 30
        warnings.append("Padrao aplicado: prazo de 30 meses. Confirme no contrato.")
    if a.meses_cumpridos is None:
        a.meses_cumpridos = 0
        warnings.append("Padrao aplicado: 0 meses cumpridos (multa cheia). Confirme antes de usar.")
    if a.prazo_total_meses <= 0 or a.meses_cumpridos < 0:
        raise ValueError("prazo deve ser positivo e meses cumpridos nao pode ser negativo")
    remaining = max(a.prazo_total_meses - a.meses_cumpridos, 0)
    full = a.aluguel_atual * a.multa_alugueis
    value = cents(full * remaining / a.prazo_total_meses)
    warnings.append("Nao avalia a dispensa por transferencia pelo empregador, com aviso escrito de 30 dias "
                    "(Lei 8.245/91, art. 4o, paragrafo unico).")
    return {"multa_cheia": str(cents(full)), "meses_restantes": remaining, "multa_proporcional": str(value),
            "avisos": warnings}


def main(argv=None):
    p = argparse.ArgumentParser(description="Reajuste anual e multa rescisoria proporcional.")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("reajuste")
    r.add_argument("--aluguel-atual", type=non_negative, required=True)
    r.add_argument("--indice", choices=["IPCA", "IGPM", "INPC", "IVAR"], required=True)
    r.add_argument("--variacao-pct", type=number, required=True)
    r.add_argument("--permite-deflacao", action="store_true")
    r.set_defaults(func=adjust)
    m = sub.add_parser("multa")
    m.add_argument("--aluguel-atual", type=non_negative, required=True)
    m.add_argument("--multa-alugueis", type=non_negative)
    m.add_argument("--prazo-total-meses", type=int)
    m.add_argument("--meses-cumpridos", type=int)
    m.set_defaults(func=fine)
    a = p.parse_args(argv)
    try:
        result = a.func(a)
    except ValueError as e:
        p.error(str(e))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
