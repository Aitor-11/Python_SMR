#factorial de los numeros que hay en la lista 
# factorial de varios números
num = int(input("dime un numero: "))
num2 = int(input("dime otro numero : "))
num3 = int(input("dime otro numero mas: "))
num4 = int(input("dime otro numero mas: "))
num5 = int(input("dime otro numero mas: "))
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

numeros = [num, num2, num3]
factoriales = []

for n in numeros:
    fact = factorial(n)
    factoriales.append(fact)
    print(f"El factorial de {n} es {fact}")

print(f"Los números son: {numeros}")


'''
1. Solicitar al usuario que ingrese un número y almacenarlo en 'num'
2. Inicializar 'factorial' en 1 y crear una lista vacía
3. Repetir desde 1 hasta num: multiplicar factorial por cada número (i)
4. Agregar cada número a la lista
5. Mostrar el resultado del factorial de num '''
