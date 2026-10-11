# CALIBRACIÓN — observa cómo se comporta random

# TODO 1: Importa el módulo random.

# TODO 2: Genera un entero aleatorio entre 1 y 20 con random.randint()
# y guárdalo en una variable 'numero'. Imprímelo.

# TODO 3: Crea una lista con 4 emojis: ["🐶", "🐱", "🐰", "🦊"]
# y usa random.choice() para elegir uno. Imprímelo.

# TODO 4: Crea una lista con los días de la semana
# (["lunes", "martes", "miércoles", "jueves", "viernes"]),
# pásala a random.shuffle() e imprime la lista DESPUÉS del shuffle.
# Nota: shuffle NO devuelve la lista nueva, la mezcla en su lugar.

import random

numero = random.randint(1, 20)
print(numero)

emojis = ["🐶", "🐱", "🐰", "🦊"]
escogido = random.choice(emojis)
print(f"El emoji escogido es: {escogido}")

dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
random.shuffle(dias)
print(f"La lista de días mesclada es: {dias}")