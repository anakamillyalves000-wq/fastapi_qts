def classificar_frete(peso_kg: float, regiao: str, premium: bool) -> str:
    # Validação do peso
    if peso_kg <= 0:
        return "invalido"
    
    # Validação da região
    regioes_validas = ["local", "estadual", "nacional"]
    if regiao not in regioes_validas:
        return "regiao invalida"
    
    # Regra para usuários premium com dados válidos
    if premium:
        return "frete gratis"
    
    # Regras para usuários não premium (premium == False)
    if regiao == "local":
        return "frete reduzido"
    else:
        return "frete padrao"