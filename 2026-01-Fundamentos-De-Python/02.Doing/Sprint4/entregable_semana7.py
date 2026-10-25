# Pega aquí tu solución del entregable
# Gestor de Tareas V2 — requisitos a validar:
# TODO: una lista global 'tareas' que persista durante toda la sesión
# TODO: funciones agregar_tarea, listar_tareas, eliminar_tarea y buscar_tarea con def
# TODO: validar duplicados y existencia con los operadores 'in' / 'not in'
# TODO: una función con slicing (tareas[:n]) para mostrar las primeras N tareas
# TODO: un menú con while True que despache opciones con if/elif/else y salga con break

tareas = []
print(tareas)

while True:

    print("\nBienvenido al Menu de Tareas")
    print("------------------------------")
    print("\n1. Agregar tarea")
    print("2. Listar tarea")
    print("3. Buscar tarea")
    print("4. Mostrar las primeras N tareas")
    print("5. Eliminar tarea")
    print("6. Salir")
    
    opcion = input("\nSeleccione una opcion: ").strip()

    if opcion not in ["1","2","3","4","5","6"]:
        print("Opcion no valida")
        continue

    #Agregar tarea
    if opcion == "1":
        tareas.append(input("Agregar tarea: "))
        print(tareas)
    
    #Listar tarea
    elif opcion == "2":
        if not tareas:
            print("No hay tareas")
        else:
            for i, tarea in enumerate(tareas):
                print(f"{i + 1}. {tarea}")
        continue
    
    #Buscar tarea
    elif opcion == "3":
        if tareas:
            pos = (input("Buscar tarea: ")).strip()
            if pos in tareas:
                print(f"La tarea '{pos}' esta en la posicion {tareas.index(pos)}")
            else:
                print(f"No existe la tarea '{pos}'")
        else:
            print("No hay tareas")
        continue
    
    #Las primeras N tareas
    elif opcion == "4":
        if not tareas:
            print("No hay tareas")
        else:
            N = int(input("Ingrese el numero de tareas a mostrar: ").strip())
            print(f"Las primeras {N} tareas son: {tareas[:N]}")
        continue

    #Eliminar tarea por valor
    elif opcion == "5":
        if not tareas:
            print("No hay tareas")
        else:
            pos = (input("Ingrese el valor de la tarea a eliminar: ")).strip()
            if pos in tareas:
                tareas.remove(pos)
                print(f"Tarea '{pos}' eliminada correctamente")
            else:
                print(f"No existe la tarea '{pos}'")
        continue

    #Salir
    elif opcion == "6":
        print("Sesión cerrada. Hasta luego.")
        break