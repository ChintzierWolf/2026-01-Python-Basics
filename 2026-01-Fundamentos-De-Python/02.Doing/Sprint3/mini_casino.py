# MINI CASINO

# TODO 1: Importa el módulo random en la primera línea del archivo.

# === JUEGO 1: Lanzar dos dados ===

# TODO 2: Genera dos números aleatorios entre 1 y 6 (inclusive) con
# random.randint() y guárdalos en 'dado1' y 'dado2'. Calcula su suma
# en una variable 'suma'.

# TODO 3: Imprime los dos dados y la suma con f-string.
# Si la suma es exactamente 7, imprime "¡JACKPOT! Sacaste 7".
# En cualquier otro caso, imprime "Sigue intentando".

# === JUEGO 2: Sorteo de premio ===

# TODO 4: Crea una lista 'participantes' con al menos 5 nombres (strings).
# Usa random.choice(participantes) para elegir un ganador al azar
# y guárdalo en una variable 'ganador'. Imprímelo con f-string.

# === JUEGO 3: Lotería (5 números del 1 al 50) ===

# TODO 5: Crea una lista vacía 'numeros_loteria'.
# Usa un for con range(5) para generar 5 números aleatorios entre 1 y 50
# y agrégalos a la lista con .append(). Imprime la lista completa al final.

# === BONUS (opcional): Contraseña aleatoria de 6 caracteres ===

# TODO 6: Crea una variable 'caracteres' con la cadena
# "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".
# Empieza con 'password = ""'. Usa un for de 6 vueltas para concatenar
# un carácter aleatorio (random.choice(caracteres)) a 'password' en cada
# vuelta. Imprime la contraseña final.

import random

# === JUEGO 1: Lanzar dos dados ===

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2

print(f"Has lanzado dos dados: {dado1} y {dado2}")
print(f"La suma de los dados es: {suma}")
if suma == 7:
    print("¡JACKPOT! Sacaste 7")
else:
    print("Sigue intentando")

# random.randint() -> permite generar números aleatorios enteros entre 1 y 6

# === JUEGO 2: Sorteo de premio ===

participantes = ["Cesar", "Alex", "Ana", "Luis", "Sofia", "Juan"]
ganador = random.choice(participantes)
print(f"El ganador es: {ganador}")

# random.choice() -> permite elegir un elemento aleatorio de una lista

# === JUEGO 3: Lotería (5 números del 1 al 50) ===

numeros_loteria = []
for i in range(5):
    numero = random.randint(1, 50)
    numeros_loteria.append(numero)
print(f"Los números de la lotería son: {numeros_loteria}")

# append() -> permite agregar elementos a una lista

# === BONUS (opcional): Contraseña aleatoria de 6 caracteres ===

caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""
for i in range(6):
    password += random.choice(caracteres)
print(f"La contraseña es: {password}")

# += -> permite agregar elementos a una variable, en este caso, caracteres a la variable password
# random.choice() -> permite elegir un elemento aleatorio de una lista