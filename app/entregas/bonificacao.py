valor_bonus_ouro = 120.0
limite_minimo_ouro = 50
valor_bonus_padrao = 50.0
limite_minimo_padrao = 20

def calcular_bonus_entregador(total_entregas : int) -> float:
     # Calcula a bonificação financeira de acordo com a quantidade de entregas
     
    if total_entregas < 0:
         return 0.0
     
    if total_entregas >= limite_minimo_ouro:
        return valor_bonus_ouro
    if total_entregas >= limite_minimo_padrao:
        return valor_bonus_padrao
    return 0.0