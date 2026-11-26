import pytest
from app.estacionamento.convenio import calcular_desconto_convenio


@pytest.mark.parametrize(
    "convenio, valor_original, valor_esperado",
    [
        ("mercado", 100.0, 20.0),   
        ("cinema", 50.0, 0.0),     
        ("vip", 200.0, 0.0),      
        ("mercado", 0.0, 0.0),    
        ("vip", -50.0, 0.0),       
    ],
)
def test_aplicar_desconto_convenio_cenarios(convenio, valor_original, valor_esperado):
    resultado = calcular_desconto_convenio(valor_original, convenio)
    assert resultado == valor_esperado