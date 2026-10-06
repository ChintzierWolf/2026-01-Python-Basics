"""
while True:
    print("\n=== CAJERO DEL BANCO INADAPTADO ===\n")
    print("1. Consultar Saldo")
    print("2. Retirar Dinero")
    print("3. Salir\n")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Saldo actual: $100")
    elif opcion == "2":
        cantidad = float(input("Cantidad a retirar: $\n"))
        print(f"Retirando ${cantidad}")
    elif opcion == "3":
        print("Gracias por usar el cajero. ¡Adiós!\n")
        break
    else:
        print("Opción no válida. Intenta de nuevo.\n")
"""

# En esta version del programa se puede ingresar cualquier valor y el programa lo detecta como valido
# A menos que se ingrese un valor valido, entonces se ejecuta la accion correspondiente

while True:
    print("\n=== CAJERO DEL BANCO INADAPTADO ===")
    print("1. Consultar Saldo")
    print("2. Retirar Dinero")
    print("3. Relizar Depósito")
    print("4. Salir")
    saldo = 300

    opcion = input("Selecciona una opción: ")
    
    if opcion not in ["1", "2", "3", "4"]:
        print(f"\n*** Opción {opcion} no válida. Intenta de nuevo. ***\n")
    
        continue
    
    if opcion == "1":
        print(f"Saldo actual: {saldo:.2f} $")
    
    elif opcion == "2":
        monto_retiro = float(input("Cantidad a retirar: $\n"))
        if monto_retiro > saldo:
            print("No tienes suficiente saldo para retirar esa cantidad")
        else:
            saldo -= monto_retiro
            print(f"Retirando ${monto_retiro}")
            print(f"Saldo actual: {saldo:.2f} $")

    elif opcion == "3":
        monto_deposito = float(input("Cantidad a depositar: $\n"))
        saldo += monto_deposito
    
        print(f"Depositando ${monto_deposito}")
        print(f"Saldo actual: {saldo:.2f} $")
    
    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Adiós!")
    
        break

# En cambio en esta version del programa no se puede ingresar cualquier valor y el programa lo detecta como valido
# A menos que se ingrese un valor valido, entonces se ejecuta la accion correspondiente
# El not in hace que el programa verifique si el valor ingresado no esta en la lista
# Si el valor no esta en la lista, entonces se ejecuta la accion correspondiente
# Una lista dentro de python es una coleccion de valores 
# los corchetes ["1", "2", "3"] son una lista de valores
# el " in " hace que el programa verifique si el valor ingresado esta en la lista
# Si el valor esta en la lista, entonces se ejecuta la accion correspondiente

