from ejercicios import ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5
from validaciones import pedir_entero


def mostrar_menu():
    print("\nPRÁCTICA: BÚSQUEDA Y ORDENAMIENTO")
    print("1. Trazar burbuja y contar operaciones")
    print("2. Ordenar de mayor a menor")
    print("3. Ordenar 10 notas y buscarlas con búsqueda binaria")
    print("4. Ordenar nombres alfabéticamente")
    print("5. Medir tiempos con 1 000, 2 000 y 4 000 elementos")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = pedir_entero("Elige un ejercicio (0 a 5): ", 0, 5)

        if opcion == 0:
            print("Práctica terminada.")
            break
        if opcion == 1:
            ejercicio_1()
        elif opcion == 2:
            ejercicio_2()
        elif opcion == 3:
            ejercicio_3()
        elif opcion == 4:
            ejercicio_4()
        elif opcion == 5:
            ejercicio_5()
        else:
            print("Opción inválida. Elige una opción del menú.")


if __name__ == "__main__":
    main()
