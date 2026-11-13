import time

from algoritmos import (
    burbuja_ascendente,
    burbuja_descendente,
    busqueda_binaria,
    ordenar_nombres,
)
from utilidades import generar_lista_pseudaleatoria
from validaciones import pedir_entero, pedir_nombre, pedir_numero


def ejercicio_1():
    print("\nEjercicio 1: traza de burbuja para [9, 7, 5, 3, 1]")
    numeros = [9, 7, 5, 3, 1]
    comparaciones = 0
    intercambios = 0

    for pasada in range(len(numeros) - 1):
        print("Pasada", pasada + 1)

        for posicion in range(len(numeros) - 1 - pasada):
            izquierda = numeros[posicion]
            derecha = numeros[posicion + 1]
            comparaciones += 1
            intercambio = izquierda > derecha

            if intercambio:
                numeros[posicion], numeros[posicion + 1] = derecha, izquierda
                intercambios += 1

            resultado = "sí" if intercambio else "no"
            print(
                "  Compara",
                izquierda,
                "y",
                derecha,
                "| intercambia:",
                resultado,
                "| lista:",
                numeros,
            )

    print("Lista ordenada:", numeros)
    print("Comparaciones:", comparaciones)
    print("Intercambios:", intercambios)
    print("Caso: peor caso, porque la lista inicia en orden inverso.")


def ejercicio_2():
    print("\nEjercicio 2: burbuja de mayor a menor")
    numeros = [5, 3, 8, 4, 2]
    print("Lista original:", numeros)
    print("Lista descendente:", burbuja_descendente(numeros))


def ejercicio_3():
    print("\nEjercicio 3: ordenar y buscar una nota")
    notas = []

    for posicion in range(10):
        notas.append(
            pedir_numero(
                "Ingresa la nota " + str(posicion + 1) + " (0 a 100): ",
                0,
                100,
            )
        )

    notas_ordenadas = burbuja_ascendente(notas)
    print("Notas ordenadas:", notas_ordenadas)
    objetivo = pedir_numero("¿Qué nota quieres buscar (0 a 100)?: ", 0, 100)
    posicion = busqueda_binaria(notas_ordenadas, objetivo)

    if posicion == -1:
        print("La nota no existe en la lista.")
    else:
        print(
            "La nota sí existe. Índice:",
            posicion,
            "| posición contando desde 1:",
            posicion + 1,
        )


def ejercicio_4():
    print("\nEjercicio 4: ordenar nombres alfabéticamente")
    cantidad = pedir_entero("¿Cuántos nombres vas a ingresar?: ", 1)
    nombres = []

    for posicion in range(cantidad):
        nombres.append(pedir_nombre("Nombre " + str(posicion + 1) + ": "))

    print("Nombres ordenados:", ordenar_nombres(nombres))
    print(
        "Sí funciona: Python compara las cadenas carácter por carácter. "
        "La comparación ignora mayúsculas aquí; los acentos siguen el orden Unicode."
    )


def ejercicio_5():
    print("\nEjercicio 5: medir burbuja con listas de distintos tamaños")
    semilla = int(time.time() * 1000000) % 2147483648
    if semilla == 0:
        semilla = 1

    tiempos = []

    for cantidad in (1000, 2000, 4000):
        numeros = generar_lista_pseudaleatoria(cantidad, semilla)
        inicio = time.perf_counter()
        burbuja_ascendente(numeros)
        duracion = time.perf_counter() - inicio
        tiempos.append(duracion)

        comparaciones = cantidad * (cantidad - 1) // 2
        print(
            cantidad,
            "elementos:",
            format(duracion, ".4f"),
            "segundos | comparaciones teóricas:",
            comparaciones,
        )

    if tiempos[0] > 0 and tiempos[1] > 0:
        print(
            "Al duplicar de 1 000 a 2 000, el tiempo se multiplicó por:",
            format(tiempos[1] / tiempos[0], ".2f"),
        )
    if tiempos[1] > 0:
        print(
            "Al duplicar de 2 000 a 4 000, el tiempo se multiplicó por:",
            format(tiempos[2] / tiempos[1], ".2f"),
        )

    print(
        "El tiempo real varía según la computadora. Como burbuja es O(n²), "
        "duplicar el tamaño produce aproximadamente cuatro veces más trabajo."
    )
    print("Los datos son seudoaleatorios y se generan sin importar otra biblioteca.")
