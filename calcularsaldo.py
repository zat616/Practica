def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    if not depositos:
        return 0.0
    return (calcular_saldo_final(depositos[:-1], tasa_interes) + depositos[-1]) * (1 + tasa_interes)

# Prueba (redondeado a 2 decimales como en el resultado esperado)
print(round(calcular_saldo_final([1000, 2000, 1500], 0.05), 2))