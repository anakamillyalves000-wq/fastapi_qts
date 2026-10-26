import pytest
from app.estacionamento.tarifas import calcular_tarifa_base


@pytest.mark.parametrize(
    "tipo_veiculo, horas, tarifa_esperada",
    [
        ("moto", 1, 5.0),
        ("moto", 3, 11.0),
        ("carro", 1, 10.0),
        ("carro", 4, 28.0),
        ("aviao", 2, -1.0),
        ("carro", 0, 0.0),
        ("moto", -2, 0.0),
    ],
)
def test_calcular_tarifa_cenarios(tipo_veiculo, horas, tarifa_esperada):
    resultado = calcular_tarifa_base(horas, tipo_veiculo)
    assert resultado == tarifa_esperada