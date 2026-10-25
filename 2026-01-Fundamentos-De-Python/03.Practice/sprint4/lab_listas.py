incidentes = [
            "TKT-101, red caida en el piso 3", 
            "TKT-102, Impresora sin toner", 
            "TKT-103, usuario sin acceso a CRM", 
            "TKT-104, Solicitud de accesoVPN", 
            "TKT-105, Solicitud de licencia de software"]

print("Lista de incidentes: ", incidentes)

#Acceder a los elementos de la lista
print(incidentes[0]) #Imprime el primer incidente, índice 0, TKT-101, red caida en el piso 3
print(incidentes[1]) #Imprime el segundo incidente, índice 1, TKT-102, Impresora sin toner
print(incidentes[4]) #Imprime el quinto incidente, índice 4, TKT-105, Solicitud de licencia de software
print(incidentes[-1]) #Imprime el último incidente, índice -1, TKT-105, Solicitud de licencia de software

print(len(incidentes)) #Imprime la cantidad de elementos en la lista, que es 5
print("Indice máximo válido: ", len(incidentes) -1)

print("\n ---- Incidentes Abiertos ---- \n")

for i in range(len(incidentes)):
    print("Incidente ", i+1, ": ", incidentes[i])

print("\n-----------------------------------------------------")
print(f"La cantidad total de incidentes es: {len(incidentes)}")