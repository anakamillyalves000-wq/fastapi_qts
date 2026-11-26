CUPONS_VALIDOS = {
    "ESTUDANTE10": {"percentual": 0.10, "valor_minimo": 0.0},
    "MEGA20": {"percentual": 0.20, "valor_minimo": 50.0},
}

def _resposta(valido: bool, motivo: str, desconto: float = 0.0) -> dict:
    return {
        "valido": valido,
        "motivo": motivo,
        "desconto": round(desconto, 2),
    }

def checar_cupom(codigo: str, montante_pedido: float) -> dict:
    if not codigo or not isinstance(codigo, str) or not codigo.strip():
        return _resposta(False, "codigo_invalido")

   
    if montante_pedido <= 0:
        return _resposta(False, "valor_invalido")

    codigo_normalizado = codigo.strip().upper()

    
    if codigo_normalizado not in CUPONS_VALIDOS:
        return _resposta(False, "cupom_inexistente")

    regra = CUPONS_VALIDOS[codigo_normalizado]

   
    if montante_pedido < regra["valor_minimo"]:
        return _resposta(False, "valor_insuficiente")

   
    desconto = montante_pedido * regra["percentual"]
    return _resposta(True, "sucesso", desconto)