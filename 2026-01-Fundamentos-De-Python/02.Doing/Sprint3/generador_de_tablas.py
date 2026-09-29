# GENERADOR DE TABLAS DE MULTIPLICAR

# TODO 1: Usa input() con int() para pedir el número del que se quiere la tabla.
# Guárdalo en una variable llamada 'numero'.

# TODO 2: Imprime un encabezado con f-string que diga "Tabla del [numero]:".

# TODO 3: Escribe un for con range(1, 11) para recorrer del 1 al 10 inclusivo.
# ¡CUIDADO! Si usas range(1, 10) te quedas en el 9 — recuerda que el fin es exclusivo.
# Dentro del bucle, imprime con f-string la línea "[numero] x [i] = [numero * i]".

# TODO 4 (opcional): Después del bucle principal, imprime una segunda tabla
# con formato alineado usando f-string con ancho de campo, por ejemplo:
# f"{numero:2} x {i:2} = {numero * i:3}"

numero = int(input("¿Qué tabla de multiplicar quieres ver?: "))

print(f"Tabla del {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
