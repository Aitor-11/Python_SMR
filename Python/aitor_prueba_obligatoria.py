'''Ejercicio 1 Se pide
1. Leer el fichero notas.txt.
2. Calcular la nota media del grupo.
3. Contar cuántos alumnos están aprobados (nota mayor o igual a 5).
4. Contar cuántos alumnos están suspensos.
5. Crear un fichero llamado resultado.txt con la siguiente información:'''


notas = []
aprobados = 0
suspensos = 0

# Leer el fichero y procesar datos
with open ('notas.txt', 'r') as file:
    for linea in file:
        nombre, nota = linea.strip().split(',') #eliminamos espacios en blanco y separamos por coma
        nota = float(nota) #tipo de dato float
        notas.append(nota) #añadimos nota a la lista
        
        if nota >= 5:
            aprobados += 1
        else:
            suspensos += 1

# Calcular media
media = sum(notas) / 5

# Mostrar resultados
print(f"Nota media: {media}")
print(f"Aprobados: {aprobados}")
print(f"Suspensos: {suspensos}")

# Crear fichero resultado.txt y escribir resultados con saltos de línea (\n)
with open('resultado.txt', 'w') as resultado:
    resultado.write(f"Nota media: {media}\n")
    resultado.write(f"Alumnos aprobados: {aprobados}\n")
    resultado.write(f"Alumnos suspensos: {suspensos}\n")
    resultado.close()
    

    
    

''' ejercicio 2 Se pide
1. Leer el fichero palabras.txt.
2. Solicitar al usuario un número entero N por teclado.
3. Crear un fichero llamado largas.txt que contenga únicamente las palabras que tengan
más de N caracteres.
4. Mostrar por pantalla cuántas palabras han sido guardadas en el fichero largas.txt'''

# Leer fichero palabras.txt
with open ('palabras.txt', 'r') as f:
    palabras = f.readlines() # leemos todas las líneas y las guardamos en una lista
    N = int(input("Introduce un número entero N: ")) #pedimos una entrada al usuario
    with open ('largas.txt', 'w') as largas: #abrimos el fichero largas.txt y  escribimos en él
        contador = 0
        for palabra in palabras: 
            palabra = palabra.strip() #eliminamos espacios en blanco y saltos de línea
            if len(palabra) > N: #comprobamos si la longitud de la palabra es mayor que N
                largas.write(palabra + '\n') #escribimos la palabra en largas.txt
                contador += 1 
    print(f"Se han guardado {contador} palabras en largas.txt")
