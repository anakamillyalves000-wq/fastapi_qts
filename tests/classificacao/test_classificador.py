from app.classificacao.classificador import classificar_nota


def test_nota_invalida_abaixo_de_zero():
    assert classificar_nota(-1) == "Nota inválida"


def test_nota_invalida_acima_de_dez():
    assert classificar_nota(11) == "Nota inválida"


def test_nota_aprovada():
    assert classificar_nota(8) == "Aprovado"


def test_nota_em_recuperacao():
    assert classificar_nota(5.5) == "Recuperação"


def test_nota_reprovada():
    assert classificar_nota(3) == "Reprovado"