# JUEGO: ADIVINA EL NÚMERO

# TODO 1: Importa el módulo random hasta arriba del archivo.

# TODO 2: Genera un número secreto entre 1 y 10 con random.randint(1, 10)
# y guárdalo en una variable llamada 'numero_secreto'.

# TODO 3: Crea un contador 'intentos' que empiece en 0
# y una bandera 'adivinado' que empiece en False.

# TODO 4: Escribe un while que se repita MIENTRAS 'adivinado' sea False.
# Dentro del bucle:
#   - Pide un intento con input() y conviértelo a int con int().
#   - Suma 1 al contador de intentos.
#   - Si el intento es igual al número secreto, cambia 'adivinado' a True
#     e imprime cuántos intentos tomó.
#   - Si el intento es menor, imprime una pista: "Muy bajo".
#   - Si el intento es mayor, imprime una pista: "Muy alto".

import random

numero_secreto = random.randint(1, 10)

intentos = 0
adivinado = False

while adivinado == False:
    intento = int(input("Adivina el número (1-10): "))
    intentos += 1
    if intento == numero_secreto:
        adivinado = True
        print("¡Correcto! Has adivinado el número.")
        print("Te tomó", intentos, "intentos.")
    elif intento < numero_secreto:
        print("Muy bajo. Intenta de nuevo.")
    else:
        print("Muy alto. Intenta de nuevo.")