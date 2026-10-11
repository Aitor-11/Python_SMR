#!/usr/bin/env python3
"""
Calculadora interactiva sencilla.

Ejecutarla sin argumentos; el programa pedirá los números y la operación
a través de input().
"""

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        print("Error: división por cero")
        return None
    return x / y

# Mapeo de opciones a (función, símbolo)
OPS = {
    "1": (add, "+"),
    "2": (sub, "-"),
    "3": (mul, "*"),
    "4": (div, "/"),
}

def get_number(prompt: str) -> float:
    """Solicita un número válido al usuario."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Introduce un número válido.")

def main() -> None:
    print("=== Calculadora interactiva ===")
    while True:
        print("\nElige operación:")
        print("  1) Sumar (+)")
        print("  2) Restar (-)")
        print("  3) Multiplicar (*)")
        print("  4) Dividir (/)")
        print("  5) Salir")
        opcion = input("Operación (1-5): ").strip()

        if opcion == "5":
            print("¡Hasta luego!")
            break
        if opcion not in OPS:
            print("Operación no válida.")
            continue

        a = get_number("Primer número: ")
        b = get_number("Segundo número: ")

        func, simbolo = OPS[opcion]
        resultado = func(a, b)

        if resultado is not None:
            print(f"{a} {simbolo} {b} = {resultado}")

if __name__ == "__main__":
    main()