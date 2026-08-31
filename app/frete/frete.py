def classificar_frete(peso_kg: float, regiao: str, premium: bool) -> str:
    
    if peso_kg <= 0:
        return "invalido"
    
    regioes_validas = ["local", "estadual", "nacional"]
    if regiao not in regioes_validas:
        return "regiao invalida"

    if premium:
        return "frete gratis"
    
    if regiao == "local":
        return "frete reduzido"
    
    return "frete padrao"