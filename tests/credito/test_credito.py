import pytest
from app.credito.credito import classificar_credito


@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 500, False, "renda invalida"),       
        (2500, -50, False, "score invalido"),
        (2500, 1200, False, "score invalido"),   
        (2500, 700, True, "reprovado"),      
        (2500, 700, False, "aprovado premium"),
    ],
)
def test_classificar_credito_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado