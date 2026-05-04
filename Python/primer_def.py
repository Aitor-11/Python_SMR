numero = int(input("Ingresa un número para calcular su cuadrado: "))

def cuadrado(numero):
    return numero ** 2
resultado = cuadrado(numero)
print(f"El cuadrado de {numero} es: {resultado}")