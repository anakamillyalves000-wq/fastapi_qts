from app.cupons.validador import checar_cupom


def test_codigo_vazio_ou_nulo_retorna_codigo_invalido():
    # Regra: código vazio, com apenas espaços ou nulo deve ser rejeitado
    esperado = {"valido": False, "motivo": "codigo_invalido", "desconto": 0.0}
    assert checar_cupom(codigo="", montante_pedido=50.0) == esperado
    assert checar_cupom(codigo="   ", montante_pedido=50.0) == esperado
    assert checar_cupom(codigo=None, montante_pedido=50.0) == esperado


def test_valor_pedido_zero_ou_negativo_retorna_valor_invalido():
    # Regra: pedidos com valor menor ou igual a zero são inválidos
    esperado = {"valido": False, "motivo": "valor_invalido", "desconto": 0.0}
    assert checar_cupom(codigo="ESTUDANTE10", montante_pedido=0.0) == esperado
    assert checar_cupom(codigo="ESTUDANTE10", montante_pedido=-25.0) == esperado


def test_cupom_estudante10_concede_dez_por_cento_de_desconto():
    # 80 reais com 10% de desconto = 8.0 reais
    resultado = checar_cupom(codigo="ESTUDANTE10", montante_pedido=80.0)
    assert resultado == {"valido": True, "motivo": "sucesso", "desconto": 8.0}


def test_cupom_estudante10_ignora_espacos_e_maiusculas_minusculas():
    # Espaços extras e letras minúsculas devem funcionar normalmente
    resultado = checar_cupom(codigo="  estudante10 ", montante_pedido=80.0)
    assert resultado == {"valido": True, "motivo": "sucesso", "desconto": 8.0}


def test_cupom_mega20_concede_vinte_por_cento_com_valor_suficiente():
    # 100 reais (acima do mínimo de 50) geram 20% = 20.0 reais
    resultado = checar_cupom(codigo="MEGA20", montante_pedido=100.0)
    assert resultado == {"valido": True, "motivo": "sucesso", "desconto": 20.0}


def test_cupom_mega20_com_pedido_abaixo_do_minimo_retorna_valor_insuficiente():
    # 40 reais é menor que o mínimo exigido de 50.0 reais
    resultado = checar_cupom(codigo="MEGA20", montante_pedido=40.0)
    assert resultado == {
        "valido": False,
        "motivo": "valor_insuficiente",
        "desconto": 0.0,
    }


def test_cupom_nao_cadastrado_retorna_cupom_inexistente():
    # Qualquer código desconhecido deve ser rejeitado
    resultado = checar_cupom(codigo="PROMO50", montante_pedido=100.0)
    assert resultado == {
        "valido": False,
        "motivo": "cupom_inexistente",
        "desconto": 0.0,
    }