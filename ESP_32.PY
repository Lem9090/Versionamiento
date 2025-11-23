def calcular_promedio(lecturas):
    if len(lecturas) == 0:
        return 0  # evitar división por cero
    return sum(lecturas) / len(lecturas)
