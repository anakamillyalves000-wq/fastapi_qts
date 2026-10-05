def calcular_status_pedido(valor_total: float, pago: bool) -> str:
    """Classifica o status do pedido com base em valor e pagamento."""
    if valor_total <= 0:
        return "invalido"
    if not pago:
        return "pendente"
    return "confirmado"