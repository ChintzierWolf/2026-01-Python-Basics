"""
# SNIPPET A
pendientes =  ["fuga de datos", "caida de servidores", "ticket vencido"]
pendientes_ordenados = pendientes.sort()
for p in pendientes_ordenados:
    print("-", p) 

# SNIPPET B
ventas = [120, 340, 90, 500, 120]
top = sorted(ventas, reverse=True)
print("Original: ", ventas)
print("Top: ", top[0], top[1])

# SNIPPPET C
config = ("v2.4", "produccion", 4)
config[2] = 6
print(config[2])
"""

# Solución

# SNIPPET A
# La solución correcta es:
pendientes = ["fuga de datos", "caida de servidores", "ticket vencido"]
pendientes.sort()
for p in pendientes:
    print("-", p)
# Ya que el método .sort() ordena la lista en su lugar y la función sorted() devuelve una nueva lista ordenada.
# .sort() modifica la lista original y no devuelve nada (None), por lo tanto, al asignarlo a pendientes_ordenados
# pendientes_ordenados sería None y el bucle for no se ejecutaría.
# Para ordenar la lista en su lugar:
# pendientes.sort()

# SNIPPET B
# La solución correcta es:
ventas = [120, 340, 90, 500, 120]
top = sorted(ventas, reverse=True)
print("Original: ", ventas)
print("Top: ", top[0], top[1])
# Ya que la función sorted() devuelve una nueva lista ordenada y no modifica la original.
# sorted(ventas, reverse=True) ordena la lista en su lugar y la función sorted() devuelve una nueva lista ordenada.
# top = sorted(ventas, reverse=True) ordena la lista en su lugar y la función sorted() devuelve una nueva lista ordenada.

# SNIPPPET C
# La solución correcta es:
config = ("v2.4", "produccion", 4)
#config[2] = 6 # Esto daría error porque las tuplas son inmutables
print(config[2])

# El error es un TypeError: 'tuple' object does not support item assignment
# Esto se debe a que las tuplas son inmutables, es decir, no se pueden modificar después de su creación.
# En cambio, las listas son mutables y se pueden modificar.
