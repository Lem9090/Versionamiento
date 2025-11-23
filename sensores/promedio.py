def calcular_promedio(lecturas):
    if len(lecturas) == 0:
        return 0
    return sum(lecturas) / len(lecturas)
