# DRILL 7: LA TABLA DE DON BETO

# TODO 1: Crea una variable 'precio_entrada' con el valor 250.

# TODO 2: Usa 'for num_entradas in range(1, 11):' para recorrer del 1 al 10.
# Dentro del bucle calcula el total (num_entradas * precio_entrada)
# e imprime con f-string: "{num_entradas} entradas: {total} pesos".

# TODO 3: Fuera del bucle, imprime "Tabla generada exitosamente."

precio_entrada = 250

for num_entradas in range(1,11):
    total = num_entradas * precio_entrada
    print(f"{num_entradas} entradas: {total} pesos")

print("Tabla generada exitosamente.")