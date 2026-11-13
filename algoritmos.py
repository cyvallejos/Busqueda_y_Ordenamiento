def burbuja_ascendente(lista):
    numeros = lista[:]
    cantidad = len(numeros)

    for pasada in range(cantidad - 1):
        hubo_intercambio = False

        for posicion in range(cantidad - 1 - pasada):
            if numeros[posicion] > numeros[posicion + 1]:
                numeros[posicion], numeros[posicion + 1] = (
                    numeros[posicion + 1],
                    numeros[posicion],
                )
                hubo_intercambio = True

        if not hubo_intercambio:
            break

    return numeros


def burbuja_descendente(lista):
    numeros = lista[:]
    cantidad = len(numeros)

    for pasada in range(cantidad - 1):
        hubo_intercambio = False

        for posicion in range(cantidad - 1 - pasada):
            if numeros[posicion] < numeros[posicion + 1]:
                numeros[posicion], numeros[posicion + 1] = (
                    numeros[posicion + 1],
                    numeros[posicion],
                )
                hubo_intercambio = True

        if not hubo_intercambio:
            break

    return numeros


def busqueda_binaria(lista_ordenada, objetivo):
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista_ordenada[medio] == objetivo:
            return medio
        if lista_ordenada[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


def ordenar_nombres(nombres):
    ordenados = nombres[:]

    for pasada in range(len(ordenados) - 1):
        hubo_intercambio = False

        for posicion in range(len(ordenados) - 1 - pasada):
            if ordenados[posicion].lower() > ordenados[posicion + 1].lower():
                ordenados[posicion], ordenados[posicion + 1] = (
                    ordenados[posicion + 1],
                    ordenados[posicion],
                )
                hubo_intercambio = True

        if not hubo_intercambio:
            break

    return ordenados
