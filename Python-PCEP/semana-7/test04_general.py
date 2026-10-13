tickets = ["TKT-101", "TKT-102", "TKT-103", "TKT-104", "TKT-105"]

print(len(tickets[1:3]), "Length de la lista, del rango posicion 1 a 3, es decir 2 elementos, que son \n")
# length de la lista, del rango posicion 1 a 3, es decir 2 elementos, que son 
# tickets[1] y tickets[2].
print(tickets[-2], "elemento en la posicion 3, contando desde atras, es decir, el penultimo elemento.\n")
print(tickets[3], "elemento en la posicion 3, sería TKT-104, el cuarto elemento\n")
# elemento en la posicion 3, sería TKT-104, el cuarto elemento

a = tickets.pop(2)
print(a)
print(tickets, "La lista se modifica al usar pop(). Y resulta ser mas corta, la lista final es: ['TKT-101', 'TKT-102', 'TKT-104', 'TKT-105']\n")
# La lista se modifica al usar pop(). Y resulta ser mas corta, la lista final es: ['TKT-101', 'TKT-102', 'TKT-104', 'TKT-105']

b = tickets.remove("TKT-104")
print("La lista se modifica al usar remove(). Y resulta ser mas corta, la lista final es:\n")
print(tickets, "None\n")
# La lista se modifica al usar remove(). Y resulta ser mas corta, la lista final es: ['TKT-101', 'TKT-102', 'TKT-105']

incidentes = ["TKT-106: red caida", "TKT-107: impresora descompuesta", "TKT-108: usuario sin acceso a CRM", "TKT-109: laptop averiada"]

print(type(incidentes), "string")
# string
print(len(incidentes), "Length de la lista")
# length de la lista
print(incidentes[1:3], "Length de la lista, del rango posicion 1 a 3, es decir 2 elementos, que son\n")
# length de la lista, del rango posicion 1 a 3, es decir 2 elementos, que son 
# incidentes[1] y incidentes[2].
print(incidentes[-2], "elemento en la posicion 3, contando desde atras, es decir, el penultimo elemento.\n")
# elemento en la posicion 3, contando desde atras, es decir, el penultimo elemento.
print(incidentes[3], "elemento en la posicion 3, sería TKT-109: laptop averiada, el cuarto elemento\n")
# elemento en la posicion 3, sería TKT-109: laptop averiada, el cuarto elemento

numeros = [10, 20, 30, 40, 50]

print(numeros[1:4])
# Del segundo al cuarto elemento ['20', '30', '40']
print(numeros[0:3])
# Del primer al tercer elemento ['10', '20', '30']
print(numeros[2:5])
# Del tercero al quinto elemento ['30', '40', '50']
print(numeros[-2:4])
# Del penultimo al cuarto elemento

print(f"{'='*30}")

print(numeros[1:])
# De la lista de numeros, me da del segundo elemento hasta el final ['20', '30', '40', '50']
print(numeros[:3])
# De la lista de numeros, me da del primer elemento hasta el tercero ['10', '20', '30']
print(numeros[::2])
# De la lista de numeros, me da del primer elemento hasta el final, de 2 en 2 ['10', '30', '50']
print(numeros[::-2])
# De la lista de numeros, me da del ultimo elemento hasta el primero, de 2 en 2 ['50', '30', '10']
print(numeros[::-1])
# De la lista de numeros, me da del ultimo elemento hasta el primero, ['50', '40', '30', '20', '10']
print(numeros[:4:3])
# Del primer al cuarto elemento, de 3 en 3 ['10', '40']
print(numeros[4:1:-3])
# Del cuarto al primer elemento, de 3 en 3 ['40', '10']
print(numeros[:3:-2])
# Del ultimo al cuarto elemento, saltando de 2 en 2, ['50', '30']
print(numeros[-2:])
# Del penultimo al final, ['40', '50']

print(f"{'='*30}")