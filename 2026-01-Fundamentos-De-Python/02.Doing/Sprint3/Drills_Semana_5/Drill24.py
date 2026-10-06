# DRILL 4: EL MINI-JUEGO DE LUCÍA

# TODO 1: Importa random.
# TODO 2: Guarda en 'secreto' un número aleatorio entre 1 y 10.
# TODO 3: Pide el primer intento con int(input("Adivina el número entre 1 y 10: ")).
# TODO 4: Usa un while que repita MIENTRAS intento sea distinto de secreto.
# TODO 5: Dentro del bucle, vuelve a pedir int(input("No es ese. Intenta de nuevo: ")).
# TODO 6: Fuera del bucle, imprime: f"¡Acertaste! El número era {secreto}.".

import random

secreto = random.randint(1, 10)
intento = int(input("Adivina el número entre 1 y 10: "))

while intento != secreto:
    intento = int(input("No es ese. Intenta de nuevo: "))

print(f"¡Acertaste! El número era {secreto}.")