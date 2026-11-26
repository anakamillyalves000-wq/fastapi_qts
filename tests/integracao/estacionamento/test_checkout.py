import pytest
from app.estacionamento.checkout import emitir_ticket_saida


@pytest.mark.parametrize(
    "tipo_veiculo, horas, convenio, valor_esperado, ticket_valido",
    [
        ("carro", 3, "mercado", 17.60, True),
        ("moto", 2, "farmacia", 7.20, True),
        ("caminhao", 2, "nenhum", 0.0, False),
        ("carro", 0, "mercado", 0.0, False),
    ],
)
def test_processar_checkout_cenarios(
    tipo_veiculo, horas, convenio, valor_esperado, ticket_valido
):
    resultado = emitir_ticket_saida(tipo_veiculo, horas, convenio)
    assert resultado["valido"] == ticket_valido
    if ticket_valido:
        assert resultado["total_a_pagar"] == valor_esperado