def f(x):
    return 2*x
y = f(4)
print(y)

def suma_y_media(a, b, c):
    suma = a+b+c
    media = suma/3
    return (suma, media)
suma, media = suma_y_media(6, 3, 9)
print(media)

def mi_funcion():
    print("Inicio")
    return
    print("Fin")
mi_funcion()

def suma(a, b, c=0):
    return a+b+c
suma(2, 3)

def saludar (nombre="amigo"):
    print("hola", nombre)

def suma(a=3, b=5, c=0):
    return a+b+c
suma(1)
print(suma(1))


def doble(x): 
    return 2*x 
doble(4)

def resta(a, b):
    return a-b
print(resta(b=2, a=5))

def suma(a, b, c=0):
    return a+b+c
suma(2, 3)
print(suma(2, 3))