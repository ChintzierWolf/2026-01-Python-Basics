ciudad = "Aguascalientes"
print(type(ciudad))
print("La cadena es: ", ciudad)
print(ciudad[::-1], "\n")

print(f"{'='*30}")

ciudad1 = ["A", "g", "u", "a", "s", "c", "a", "l", "i", "e", "n", "t", "e", "s"]
print(type(ciudad1))
print("La lista es: ", ciudad1)
print("La lista invertida es: ", ciudad1[::-1], "\n")

print(f"{'='*30}")

ciudad = list(ciudad)
ciudad[3] = 'z'
print("Valor de ciudad: ",ciudad)

ciudad1[3] = 'z'
print("Valor de ciudad1: ",ciudad1, "\n")

print(f"{'='*30}\n")

incidentes = ["TKT-106: red caida", "TKT-107: impresora descompuesta", "TKT-108: usuario sin acceso a CRM", "TKT-109: laptop averiada"]

resultado = incidentes.append("TKT-110: backup del servidor falló anoche")
print("Resultado de append: ", resultado)
print("Lista de incidentes: ", incidentes)

incidentes1 = incidentes.insert(0, "TKT-000: wifi sin acceso")
print(incidentes1, "insert() inserta el elemento en la posicion indicada\n")

incidentes2 = incidentes.insert(2, "TKT-001: wifi sin acceso")
print(incidentes2, "insert() inserta el elemento en la posicion indicada", incidentes, "\n")

incidentes3 = incidentes.pop(0)
print(incidentes3, "pop() elimina el elemento indicado", incidentes, "\n")

# Para imprimir los elementos de la lista de manera de cascada, se puede usar un ciclo for
for incidente in incidentes:
    print(incidente)

print("\n")

# Tambien se puede usar un ciclo while
i = 0
while i < len(incidentes):
    print(incidentes[i])
    i += 1