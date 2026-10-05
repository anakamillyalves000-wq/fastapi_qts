import pytest
from app.credito.credito import classificar_credito


@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito",
    [
        (0, "local", True, "invalido"),
        (-1, "estadual", False, "invalido"),
        (5, "internacional", False, "regiao invalida"),
        (2, "local", True, "frete gratis"),
        (3, "local", False, "frete reduzido"),
        (3, "estadual", False, "frete padrao"),
        (3, "nacional", False, "frete padrao"),
    ],
)
def test_classificar_frete_caixa_preta(
    peso_kg, regiao, premium, retorno_esperado
):
    assert classificar_frete(peso_kg, regiao, premium) == retorno_esperado