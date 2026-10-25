# COMPARACIÓN: LISTAS VS TUPLAS

# ===== PARTE 1: LISTAS (modificables) =====

# TODO 1: Imprime un encabezado "=== LISTAS (Modificables) ===".

# TODO 2: Crea una lista 'tareas' con tres strings:
#   "estudiar", "ejercicio", "compras".
# Imprímela con f-string para ver el estado inicial.

# TODO 3: Usa .append("leer") para agregar una cuarta tarea.
# Imprime la lista para verificar el cambio.

# TODO 4: Reemplaza la tarea en el índice 1 por "yoga" (asignación directa
# con corchetes: tareas[1] = "yoga"). Imprime la lista.

# TODO 5: Quita "compras" con .remove("compras"). Imprime la lista resultante.

# ===== PARTE 2: TUPLAS (inmutables) =====

# TODO 6: Imprime un encabezado "=== TUPLAS (Inmutables) ===".

# TODO 7: Crea una tupla 'config' con tres valores (servidor, puerto, ambiente):
#   "localhost", 8080, "producción".
# Imprímela.

# TODO 8: Imprime cada elemento por separado accediendo por índice
# (config[0], config[1], config[2]) con f-string.

# TODO 9: Desempaqueta la tupla en tres variables nuevas (servidor,
# puerto, ambiente) en una sola línea: 'servidor, puerto, ambiente = config'.
# Imprime las tres en un f-string para confirmar que el desempaque funcionó.

# TODO 10: Para "cambiar" el puerto a 9000 SIN romper la inmutabilidad,
# crea una NUEVA tupla 'config_nueva' tomando los valores actuales
# de config y reemplazando solo el puerto (pista: config[0], 9000, config[2]).
# Imprime la nueva tupla.

# ===== PARTE 3: CASOS DE USO =====

# TODO 11: Imprime "=== CASOS DE USO ===".

# TODO 12: Crea una TUPLA 'ubicacion' con dos floats representando
# coordenadas GPS (por ejemplo, (19.4326, -99.1332) para CDMX).
# Decide POR QUÉ tupla y no lista: las coordenadas de un punto fijo
# no cambian. Imprímela.

# TODO 13: Crea una LISTA 'compras' con dos strings ("leche", "pan").
# Agrégale "huevos" con .append(). Es lista porque cambia. Imprímela.

# TODO 14: Crea una TUPLA 'DIAS' con los 7 días abreviados de la semana
# ("Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"). En mayúsculas porque
# es una constante. Imprime el día en posición 2 con DIAS[2].

# TODO 1
print("=== LISTAS (Modificables) ===")

# TODO 2
tareas = ['estudiar', 'ejercicio', 'compras']
print(f"\nLista inicial de tareas: {tareas}")

# TODO 3
tareas.append("leer")
print(f"\nLista final después de agregar una tarea: {tareas}")

# TODO 4
tareas[1] = "yoga"
print(f"\nLista final después de reemplazar una tarea: {tareas}")

# TODO 5
tareas.remove("compras")
print(f"\nLista final después de eliminar una tarea: {tareas}")

# ===== PARTE 2: TUPLAS (inmutables) =====

# TODO 6
print("\n=== TUPLAS (Inmutables) ===")

# TODO 7
config = ("localhost", 8080, "producción")
print(f"\nConfiguración inicial: {config}")

# TODO 8
print(f"\nÍndice 1: {config[0]}")
print(f"Índice 2: {config[1]}")
print(f"Índice 3: {config[2]}")

# TODO 9
servidor, puerto, ambiente = config
print(f"\nServidor: {servidor}, Puerto: {puerto}, Ambiente: {ambiente}")

# TODO 10
config_nueva = (config[0], 9000, config[2])
print(f"\nConfiguración final: {config_nueva}")

# ===== PARTE 3: CASOS DE USO =====

# TODO 11
print("\n=== CASOS DE USO ===")

# TODO 12
ubicacion = (19.4326, -99.1332)
print(f"\nUbicación: {ubicacion}")

# TODO 13
compras = ["leche", "pan"]
compras.append("huevos")
print(f"\nLista de compras: {compras}")

# TODO 14
DIAS = ("Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom")
print(f"\nDía en posición 2: {DIAS[2]}")