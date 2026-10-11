def saludar (nombre="amigo"):
    print("hola", nombre)
    return 
    
    
    '''Calcula la media aritmética de los dos números de entrada.'''
def media (x, y, z= 8):
    return (x + y) /2
    
    
    
    
'''llamadas '''
a = 5
b = 10
vmedia = media(a,b)
print(f"la media de los dos numero es: {vmedia}")


saludar()

vmedia = media(y=100, z=50)
print(f"la media de los dos numero es: {vmedia}")