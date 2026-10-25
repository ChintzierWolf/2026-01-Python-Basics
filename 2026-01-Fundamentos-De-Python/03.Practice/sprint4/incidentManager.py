# GESTOR DE INCIDENTES — SonidoLibre
# Un sistema básico para registrar y resolver incidentes técnicos.

incidentes = []

# TODO 1: Agrega los siguientes 3 incidentes a la lista con append():
# "microfono escenario principal sin señal"
# "generador zona VIP con fluctuación"
# "pantalla LED intermitente"

# TODO 2: Imprime la lista completa y el número de incidentes.

# TODO 3: Sofía resuelve el primer incidente. Elimínalo con pop(0)
# y guarda el resultado en una variable. Imprime qué incidente se resolvió.

# TODO 4: Llega un incidente nuevo: "cable de poder roto en escenario 2".
# Agrégalo. Imprime la lista actualizada.

# TODO 5: El equipo busca si "generador zona VIP con fluctuación" sigue abierto.
# Usa "in" para verificarlo e imprime un mensaje según el resultado.

# TODO 6: Imprime todos los incidentes abiertos con un for loop.
# Formato: "→ [incidente]" por cada uno.

# TODO 1
incidentes.append("microfono escenario principal sin señal")
incidentes.append("generador zona VIP con fluctuación")
incidentes.append("pantalla LED intermitente")

# TODO 2
print(f"\nLista actualizada de incidentes: {incidentes}")
print(f"Total de incidentes: {len(incidentes)}")

# TODO 3
eliminado = incidentes.pop(0)
print(f"\nIncidente eliminado: {eliminado}")

print(f"\nLista actualizada de incidentes: {incidentes}")
print(f"Total de incidentes: {len(incidentes)}")

# TODO 4
incidentes.append("cable de poder roto en escenario 2")
print(f"\nIncidente agregado: {incidentes.append}")
print(f"\nLista actualizada de incidentes: {incidentes}")
print(f"Total de incidentes: {len(incidentes)}")

# TODO 5
buscador = "generador zona VIP con fluctuación"
if buscador in incidentes:
    print(f"\nEl incidente '{buscador}' está abierto.")
else:
    print(f"El incidente '{buscador}' no está abierto.")

# TODO 6
print("\nIncidentes abiertos:")
for incidente in incidentes:
    print(f"→ {incidente}")