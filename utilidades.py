def generar_lista_pseudaleatoria(cantidad, semilla):
    numeros = []

    for _ in range(cantidad):
        semilla = (1103515245 * semilla + 12345) % 2147483648
        numeros.append(semilla % 100000)

    return numeros
