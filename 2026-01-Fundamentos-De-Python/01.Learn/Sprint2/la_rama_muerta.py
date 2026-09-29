"""
nivel = 5

if nivel > 0:
    print("Pricipiante")
elif nivel > 3:
    print("Avanzado")
else:
    print("Invalido")
"""

# El código siempre se ejecuta de arriba hacia abajo. Se detiene en cuanto encuentra una condición que se cumple.
# En este caso el error del código es que no se está validando si el nivel es mayor a 0 y menor a 3.
# Por lo tanto, el código siempre se va a ejecutar en la primera condición que se cumple.

# Corrección: Debemos validar si el nivel es mayor a 0 y menor a 3.

nivel_1 = 5

if nivel_1 > 3:
    print("Avanzado")
elif nivel_1 > 0:
    print("Pricipiante")
else:
    print("Invalido")

# Corrección extra

nivel_2 = 5

if nivel_2 > 0 and nivel_2 < 3:
    print("Pricipiante")
elif nivel_2 >= 3 and nivel_2 < 5:
    print("Intermedio")
elif nivel_2 >= 5:
    print("Avanzado")
else:
    print("Invalido")

# Corrección extra 2

nivel = 5
if nivel > 0 and nivel < 3:
    print("Pricipiante")
elif nivel >= 3 and nivel < 5:
    print("Intermedio")
elif nivel >= 5:
    print("Avanzado")
else:
    print("Invalido")
    