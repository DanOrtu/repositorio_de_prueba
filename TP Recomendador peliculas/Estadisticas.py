def calcular_promedios(suma: int, contador: int) -> float:
    promedio = suma / contador
    return promedio

def sacar_maximo(contador_general: int, edad: int) -> int:
    maximo_edad = None
    if contador_general == 1 or edad > maximo_edad:
        maximo_edad = edad
    return maximo_edad

def sacar_minimo(edad: int) -> int:
    contador_menores = 0
    min_menores_edad = None
    if edad < 18:
        contador_menores += 1
        if contador_menores == 1 or edad < min_menores_edad:
            min_menores_edad = edad
    return min_menores_edad

def calcular_porcentajes(contador: int, contador_general: int) -> float:
    if contador > 0:
        porcentaje_accion = (contador / contador_general) * 100
    else:
        porcentaje_accion = 0
    return porcentaje_accion 