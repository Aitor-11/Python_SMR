'''Eleva el primer número a la potencia indicada por el segundo.'''
def potencia(x, y):
    print(f"primer parametro {x}")
    print(f"segundo parametro {y}")
    return x ** y 

y = 2
x = 10
resultado = potencia(y, x)
print(f"{y} elevado a {x} es: {resultado}")



'''Devuelve el número más grande entre dos valores pasados por parámetro'''
def maximo (x, y):
    if x > y:
        return x
    else:
        return y
y = int(input("dime un número : "))
x = int(input("dime un número : "))
maximo = maximo(y, x)
print(f"El máximo entre {y} y {x} es: {maximo}")



'''Calcula la media aritmética de los dos números de entrada.'''
def media (x, y):
    return (x + y) /2

media = media(x,y)
print(f"la media de los dos numero es: {media}")



'''Devuelve el número más pequeño entre los dos valores.'''
def minimo(x, y):
    if x < y: 
        return x 
    else :
        return y
minimo = minimo(y,x)
print(f"el minimo entre {y} y {x} es: {minimo}")


'''Obtiene el resto de la división del primer número entre el segundo'''
def resto (x ,y):
    return x % y 

resto = resto(x,y)
print(f"el resto de la division es: {resto}")



'''Calcula la distancia absoluta entre los dos números en una recta.'''
def distancia(x, y):
    return abs(x - y)
distancia = distancia(x,y)
print(f"la distancia en absoluta entre los numeros es {distancia}")
