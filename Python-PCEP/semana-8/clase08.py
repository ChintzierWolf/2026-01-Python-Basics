# Iteración y orden inmutable

#sorted(): Ordena elementos de cualquier iterable (lista, tupla, string)
#devuelve una NUEVA lista
# no modifica el original

# sort() método de listas
# Ordena la lista en la que se aplica
# no devuelve nada (None)
# sí modifica el original

# sorted(iterable, key=None, reverse=False)
# key=funcion para extraer la llave de ordenamiento
# reverse=True para ordenamiento descendente
# sorted(iterable, key=len)
# sorted(iterable, key=str.lower)
# sorted(iterable, key=lambda x: x[1]) #Ordena por el segundo elemento

# tuplas ()
# Inmutables (no se pueden modificar), ejemplo: (4,6,2,1,3,5)
# Ordenables (tienen orden natural), ejemplo; 4,6,2,1,3,5
# Iterables (se pueden recorrer con for) ejemplo; for i in (4,6,2,1,3,5):
# Se pueden ordenar con sorted() (devuelve lista)
# Se pueden usar como claves de diccionario (si son inmutables), ejemplo; tupla_unica = (1, 2, 3); dict[tupla_unica] = "valor"

#binario

"""
pendientes: list[str] = ["fuga de datos", "caida del servidor", "ticket vencido"]
pendientes_ordenados: None = pendientes.sort()
for p in pendientes_ordenados:
    print("- ", p)

# El resultado de pendientes_ordenados es None porque el método sort() modifica la lista original y no devuelve nada.
# Para ordenar la lista y obtener una nueva lista, se debe usar el método sorted()

# correccion

pendientes: list[str] = ["fuga de datos", "caida del servidor", "ticket vencido"]
pendientes_ordenados: list[str] = sorted(pendientes)
for p in pendientes_ordenados:
    print("- ", p)


ventas = [120, 340, 90, 150, 110]
top = sorted(ventas, reverse=True)
print("Original:", ventas)
print("Top ventas:", top[:3])



tupla = (1, 2, [3, 4], (5,6))

tupla1 = (2, 3, 4, 3, 5)
tupla1[3].append(10)
print(tupla1)



#Fase 2: dos listas paralelas + filtrado

incidencias = ["impresora bloqueada", "correo no envía emails", "no puedo conectarme a WiFi", "fuga de datos", "caída del servidor", "ticket vencido"]
prioridades = ["critica", "critica", "media", "alta", "baja", "baja"]

print("\n --- REPORTE DE INCIDENCIAS CRITICAS ---")

posicion = 0

for incidencia in incidencias:
    if prioridades[posicion] == "critica":
        print(f"[!] {incidencias[posicion]}")
    posicion = posicion + 1

# Fase 3 acumuladores

horas = [8, 12, 3, 6, 1, 3]

total_horas = 0
total_criticas = 0
posicion = 0

total_incidentes_criticas = 0

for incidencia in incidencias:
    total_horas = total_horas + horas[posicion]
    if prioridades[posicion] == "critica":
        total_criticas = total_criticas + horas[posicion]
        total_incidentes_criticas = total_incidentes_criticas + 1
    posicion = posicion + 1

print("Total de horas de backlog: ", total_horas)
print("Total de horas solo criticas: ", total_criticas)
print("Total de incidencias criticas: ", total_incidentes_criticas)

# Fase 4 Orden de incidencias por alfabeto

incidencia_ordenadas = sorted(incidencias)
for posicion, incidencia in enumerate(incidencia_ordenadas, start=1):
    print(posicion, incidencia)

# Fase 5 orden de incidencias por horas

incidencias_horas = []

for r in range(len(incidencias)):
    incidencia = incidencias[r]
    horas_incidencias = horas[r]
    incidencias_horas.append((incidencia, horas_incidencias))

print(incidencias_horas)
incidencias_horas.sort(key=lambda x: x[1], reverse=True)

for elemento in incidencias_horas:
    print(elemento)

#incidencias_ordenadas_por_horas = sorted(zip(incidencias, horas), key=lambda x: x[1], reverse=True)
#for incidencia, horas in incidencias_ordenadas_por_horas:
#    print(incidencia, horas)

"""

# ¿Cuántos días hábiles mínimos para cerrar todo si el equipo cierra 4 por día? 5/4 = 1.25
# ¿Le decimos a dirección '1.25 días' o necesitamos 2 días reales?
# Dias no se fraccionan: redondeo HACIA ARRIBA

import math

math

total_incidencias = len(incidencias)
por_dia = 4
dias_minimos = math.ceil(total_incidencias / por_dia)
print(f"Para cerrar {total_incidencias} incidencias, se necesitan {dias_minimos} días hábiles.")

