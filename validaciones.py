def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print("Ingresa un número igual o mayor que", minimo)
                continue
            if maximo is not None and valor > maximo:
                print("Ingresa un número igual o menor que", maximo)
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Escribe un número entero.")


def pedir_numero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Escribe un número.")
            continue

        if minimo is not None and not valor >= minimo:
            print("Ingresa un número igual o mayor que", minimo)
            continue
        if maximo is not None and not valor <= maximo:
            print("Ingresa un número igual o menor que", maximo)
            continue
        return valor


def pedir_nombre(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor and all(letra.isalpha() or letra == " " for letra in valor):
            return valor
        print("Ingresa solo letras y espacios, sin números ni símbolos.")
