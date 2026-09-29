"""
tabla = int(input("¿Qué tabla de multiplicar quieres ver?: "))

for multiplicador in range(1, 11):
    resultado = tabla * multiplicador
    print(tabla, "x", multiplicador, "=", resultado)
    print(f"{tabla} x {multiplicador} = {resultado}")
"""

tabla = int(input("¿Qué tabla de multiplicar quieres ver?: "))

for i in range(1, 11):
    print(tabla, "x", i, "=", tabla * i)
