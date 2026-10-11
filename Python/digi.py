import hashlib
import time

# -----------------------------
# Parámetros de la "minería"
# -----------------------------
dificultad = 8  # número de ceros iniciales requeridos en el hash
objetivo = "0" * dificultad

# Bloque ficticio con transacciones
bloque = """
Alice -> Bob : 1.5 BTC
Bob -> Charlie : 0.7 BTC
Charlie -> Dave : 0.2 BTC
"""

nonce = 0
hash_resultado = ""

inicio = time.time()

print("⛏️ Iniciando minería...")
print(f"Dificultad: {dificultad} ceros\n")

# -----------------------------
# Proceso de minería
# -----------------------------
while True:
    contenido = bloque + str(nonce)
    hash_resultado = hashlib.sha256(contenido.encode()).hexdigest()

    if hash_resultado.startswith(objetivo):
        break

    nonce += 1

fin = time.time()

# -----------------------------
# Resultados
# -----------------------------
print("✅ Bloque minado con éxito!\n")
print(f"Nonce encontrado: {nonce}")
print(f"Hash: {hash_resultado}")
print(f"Tiempo empleado: {fin - inicio:.2f} segundos")

