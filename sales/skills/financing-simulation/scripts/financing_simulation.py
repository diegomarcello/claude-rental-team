#!/usr/bin/env python3
"""SAC and Price simulation for Brazil. Spec: references/calculation-spec-brazil.md. Standard library only."""
import argparse
import json
import sys
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

CENT = Decimal("0.01")
INCOME_LIMIT = Decimal("0.30")


def money(text):
    try:
        value = Decimal(text)
    except InvalidOperation:
        raise argparse.ArgumentTypeError(f"valor invalido: {text!r} (use ponto decimal, ex.: 400000.00)")
    if not value.is_finite() or value < 0:
        raise argparse.ArgumentTypeError(f"o valor deve ser um numero nao negativo: {text!r}")
    return value


def cents(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def main(argv=None):
    p = argparse.ArgumentParser(description="Simulacao de financiamento imobiliario.")
    p.add_argument("--valor-imovel", type=money, required=True)
    p.add_argument("--valor-entrada", type=money, required=True)
    p.add_argument("--prazo-meses", type=int, required=True)
    p.add_argument("--taxa-anual-pct", type=money, required=True, help="taxa efetiva ao ano")
    p.add_argument("--sistema", choices=["PRICE", "SAC"], required=True)
    p.add_argument("--renda-mensal", type=money)
    p.add_argument("--seguros-mensais", type=money, default=Decimal(0))
    a = p.parse_args(argv)
    if a.valor_entrada >= a.valor_imovel:
        p.error("a entrada cobre o valor do imovel: nao ha saldo a financiar")
    if a.prazo_meses <= 0:
        p.error("--prazo-meses deve ser positivo")
    if a.renda_mensal is not None and a.renda_mensal <= 0:
        p.error("--renda-mensal deve ser positiva")

    principal = a.valor_imovel - a.valor_entrada
    rate = (1 + a.taxa_anual_pct / 100) ** (Decimal(1) / 12) - 1
    if a.sistema == "PRICE":
        if rate:
            growth = (1 + rate) ** a.prazo_meses
            payment = principal * rate * growth / (growth - 1)
        else:
            payment = principal / a.prazo_meses
        first = last = payment
    else:
        amortization = principal / a.prazo_meses
        first = amortization + principal * rate
        last = amortization + amortization * rate
    first = cents(first + a.seguros_mensais)
    last = cents(last + a.seguros_mensais)

    share, status = None, "renda_nao_informada"
    if a.renda_mensal is not None:
        share = str(cents(first / a.renda_mensal * 100))
        status = "aprovado_renda" if first <= a.renda_mensal * INCOME_LIMIT else "reprovado_limite_renda"
    result = {
        "valor_financiado": str(cents(principal)),
        "taxa_mensal_pct": str((rate * 100).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)),
        "sistema": a.sistema,
        "primeira_parcela": str(first),
        "ultima_parcela": str(last),
        "comprometimento_pct": share,
        "status": status,
        "avisos": [
            "Simulacao informativa, sujeita a analise de credito; nao e oferta de credito.",
            "Nao inclui indexador (ex.: TR) nem seguros alem do valor informado.",
        ],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
