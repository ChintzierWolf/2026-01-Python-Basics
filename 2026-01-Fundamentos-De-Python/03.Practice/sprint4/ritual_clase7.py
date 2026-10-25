tickets = ["TKT-101", "TKT-102", "TKT-103", "TKT-104", "TKT-105"]

print(len(tickets[1:3]))
# Imprimirá la longitud del slice [1:3]
# Los elementos son:tickets[1], tickets[2], que son TKT-102, TKT-103, cuyo tamaño es 2

print(tickets[-2])
# Imprimirá el segundo elemento desde el final, que es TKT-104

print(tickets[4])
# Imprimirá el último elemento, que es TKT-105

print(tickets[5])
# Imprimirá un error porque no existe el elemento en el índice 5, ya que la lista tiene 5 elementos, con índices de 0 a 4.

# Recorrer la lista con un bucle for
for ticket in tickets:
    print(ticket)

