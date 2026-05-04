#Ejercicico 3
#Escribe un programa que pinte por pantalla una pirámide rellena a base de asteriscos. 
# Labase de la pirámide debe estar formada por 9 asteriscos

for i in range(1, 10, 2):
    espacios = (9 - i) // 2
    print(' ' * espacios + '*' * i + ' ' * espacios)


#ejercicio 4
#Enteros Crea un programa que pida dos números enteros por teclado y muestre todas las
#operaciones básicas (suma, resta, multiplicación, división, resto y potencia)
num = int(input("Introduce un número entero: ")) 
num2 = int(input("Introduce otro número entero: "))
operacion = input("Introduce la operación a realizar (+, -, *, /, % , **): ")

if operacion == "+":
    print( num + num2)
elif operacion == "-":
    print( num - num2)
elif operacion == "*":
    print( num * num2)
elif operacion == "/":
    print( num / num2)    
elif operacion == "%":
    print( num % num2)
elif operacion == "**":
    print( num ** num2)
else:
    print("Operación no válida")

# ejercicio 5
#Escribe un programa que almacene una variable con el valor 1,3 e imprime por
#pantalla el número con 20 decimales. ¿Hay un error por que?
variable = 1.3
print(f"{variable:.20f}")












'''ejercicio 17
Escribe una variable con el valor “En un lugar de la mancha de cuyo nombre no
quiero acordarme …” y realiza las siguientes operaciones'''
nuevotexto = "dijo don quijote"
frase = "En un lugar de la mancha de cuyo nombre no quiero acordarme ..."
type ("mancha" in frase)
print("mancha" in frase)    