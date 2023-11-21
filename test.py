numero_ingresado = int(input("Ingrese un número: "))


def calcular_serie(n, contador=1):
    if contador > n:
        return 0
    else:
        termino_actual = 1 / contador
        return termino_actual + calcular_serie(n, contador + 1)


resultado = calcular_serie(numero_ingresado)
print(resultado)
