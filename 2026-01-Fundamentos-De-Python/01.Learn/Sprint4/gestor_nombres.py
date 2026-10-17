# GESTOR DE NOMBRES — ÍNDICES, SLICING Y BÚSQUEDA

# TODO 1: Crea una lista 'nombres' con estos 7 strings, en este orden:
#   "Ana", "Luis", "Carlos", "María", "Pedro", "Sofía", "Diego".

# TODO 2: Imprime un encabezado "=== Lista Completa ===" seguido
# de la lista entera, y después el total usando len(nombres).

# ===== ACCESO POR ÍNDICE =====

# TODO 3: Imprime tres cosas con f-strings (encabezado "=== Acceso por Índice ==="):
#   - el primer nombre (índice 0)
#   - el último nombre (usa índice negativo -1, NO 'nombres[6]')
#   - el tercer nombre (recuerda: índice 2, porque empiezan en 0)

# ===== SLICING =====

# TODO 4: Imprime cuatro sublistas con encabezado "=== Slicing ===":
#   - los primeros 3 nombres con nombres[:3]
#   - los últimos 2 con nombres[-2:]
#   - del 2º al 5º con nombres[1:5]
#   - todos menos el primero y el último con nombres[1:-1]

# ===== BÚSQUEDA =====

# TODO 5: Encabezado "=== Búsqueda ===". Crea una variable
# 'buscar = "Carlos"'. Usa 'if buscar in nombres:' para verificar
# si existe en la lista. Si está, usa nombres.index(buscar) para
# obtener su posición e imprímela. Si no, imprime que no está.

# TODO 6: Crea una variable 'nuevo = "Roberto"'. Usa 'if nuevo not in nombres:'
# para verificar que NO está antes de agregarlo. Si no estaba,
# agrégalo con .append() e imprime la lista actualizada.
# Si ya estaba, avisa que ya existe.


nombres = ["Ana", "Luis", "Carlos", "María", "Pedro", "Sofía", "Diego"]

print("=== Lista Completa ===")
print(nombres)
print(len(nombres))

print("\n=== Acceso por Índice ===")
print(f"Primer nombre nombres[0]: {nombres[0]}")
print(f"Último nombre nombres[-1]: {nombres[-1]}")
print(f"Tercer nombre nombres[2]: {nombres[2]}")

print("\n=== Slicing ===")

print(f"Primeros 3 nombres nombres[:3]: {nombres[:3]}")
print(f"Últimos 2 nombres nombres[-2:]: {nombres[-2:]}")
print(f"Del 2º al 5º nombres[1:5]: {nombres[1:5]}")
print(f"Todos menos el primero y el último nombres[1:-1]: {nombres[1:-1]}")

print("\n=== Búsqueda ===")
buscar = "Carlos"

if buscar in nombres:
    print(f"'Carlos' está en la lista en la posición {nombres.index(buscar)}")
else:
    print(f"'Carlos' NO está en la lista")

nuevo = "Roberto"

if nuevo not in nombres:
    nombres.append(nuevo)
    print(f"Se agregó '{nuevo}' a la lista")
    print(f"Lista actualizada: {nombres}")
else:
    print(f"'{nuevo}' ya existe en la lista")
