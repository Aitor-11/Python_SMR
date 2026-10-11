# --- Definiciones de funciones ---


# 7. Valor promedio entre 2 números.
def promedio(a, b):
    total = a + b
    print(f"La suma d {a} y {b} es: {total}, calculando la media aritmetica… ")
    media = total / 2
    return media

# 7.bis Valor promedio entre 3 o 4 números llamos por nombre.
def promedio(aaa, bbb, ccc, ddd = 100):
    total = aaa + bbb + ccc + ddd
    print(f"La suma d {aaa}, {bbb}, {ccc} con el valor por defecto {ddd} es: {total}, calculando la media aritmetica… ")
    media = total / 4
    return media

# 77.bis Valor promedio entre 3 o 4 números, y un segundo argumento de salida
def media_y_suma(aaa, bbb, ccc, ddd = 100):
    total = aaa + bbb + ccc + ddd
    print(f"La suma d {aaa}, {bbb}, {ccc} con el ultimo parámetro con valor {ddd} es devuelta como argumento de salida= {total}")
    media = total / 4
    return media, total


# 11. Media geométrica   que consiste en realizar la raíz cuadrada del producto de los dos números
def media_geometrica(a, b):
    producto = a * b
    print(f"Producto entre {a} y {b} es {producto}")
    resultado = producto ** 0.5
    return resultado


# 12. Diferencia cuadrática
def diferencia_cuadratica(a, b):
    diff = a - b
    print(f"Calculando la diferencia entre a={a} y b={b} es {diff}")
    al_cuadrado = diff ** 2
    return al_cuadrado


# --- Llamadas de pruebas

x = 2
y = 8

print(f"Llamar al promedio con argumentos nombrados (bbb = {x}, ccc = 11, aaa = {y})")
numero_salida = promedio(bbb = x, ccc = 11, aaa = y)

print(f"\nel resultado es {numero_salida}")


#print(f"Vamos a llamar a la función de media geometrica de ({x}, {y})")
#numero_salida = media_geometrica(x,y)
#print(f"\nel resultado es {numero_salida}")

print(f"Al llamar a la nueva funcion con argumentos nombrados (bbb = {x}, ccc = 11, aaa = {y},  ddd = 5)")
el_promedio, la_suma = media_y_suma(bbb = x, ccc = 11, aaa = y, ddd = 5)

print(f"\nlos resultados son media= {el_promedio} y suma total= {la_suma}")



#TIMESTAMP: son las 20:40 d v9.1.2026