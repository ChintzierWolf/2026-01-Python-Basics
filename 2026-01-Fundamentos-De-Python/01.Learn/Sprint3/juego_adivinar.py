"""
import random

secreto = random.randint(1, 10)

intento = 0

while intento != secreto:
    intento = int(input("Adivina el número (1-10): "))
    
    print("Felicidades! Haz adivinado el número")
"""


import random

numero_secreto = random.randint(1, 10)

intento = 0
limite_intentos = 3

while intento < limite_intentos:
    adivinanza = int(input("Adivina el número (1-10): "))
    if adivinanza == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")
        intento += 1

if intento == limite_intentos:
    print("Has agotado tus intentos. El número era", numero_secreto)
