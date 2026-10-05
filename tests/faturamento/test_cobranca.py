import pytest
from app.faturamento.cobranca import processar_cobranca  


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, valor_final",
    [
        (0.0, "BASICO", 0, -1.0),
        (10.0, "PREMIUM", 0, 9.0),
        (20.0, "EMPRESARIAL", 5, 21.4),
        (10.0, "BASICO", 31, 38.1),
        (50.0, "  premium  ", 0, 45.0),
        (10.0, "BASICO", 0, 10.0),
        (500.0, "PREMIUM", 60, 745.0),
    ],
)
def test_processar_cobranca(valor_base, plano, dias_atraso, valor_final):
    resultado = processar_cobranca(valor_base, plano, dias_atraso)
    assert resultado == pytest.approx(valor_final)