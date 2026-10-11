while True:
    print("\n==== Cajero Automático ====")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion not in ["1", "2", "3", "4"]:
        print("\nOpción inválida, intente de nuevo")
        continue

    if opcion == "1":
        print("\nSaldo actual: $", saldo)
    
    elif opcion == "2":
        cantidad = float(input("\nIngrese la cantidad a retirar: "))
        if cantidad > saldo:
            print("\nSaldo insuficiente")
        else:
            saldo -= cantidad
            print("\nRetiro exitoso")
    
    elif opcion == "3":
        cantidad = float(input("\nIngrese la cantidad a depositar: "))
        saldo += cantidad
        print("\nDepósito exitoso")
    
    elif opcion == "4":
        print("\nGracias por usar el cajero")
        break
    