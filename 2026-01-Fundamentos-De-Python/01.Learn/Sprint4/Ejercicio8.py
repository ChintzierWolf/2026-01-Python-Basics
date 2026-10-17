"""
tareas  = []

while True:

    print("Opciones: 1. Agregar 2. Ver 3. Borrar 4. Salir")

    opcion = input("Elija una opcion: ")

    if opcion == "1":
        tarea = input("Ingrese la tarea: ")
        tareas.append(tarea)
        print("Tarea agregada. ")

    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas")
        else:
            print("Tareas: ")
            for i, tarea in enumerate(tareas):
                print(f"{i + 1}. {tarea}")

    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas para borrar")
        else:
            print("Tareas: ")
            for i, tarea in enumerate(tareas):
                print(f"{i + 1}. {tarea}")
            try:
                indice = int(input("Ingrese el numero de la tarea a borrar: ")) - 1
                if 0 <= indice < len(tareas):
                    tareas.pop(indice)
                    print("Tarea borrada. ")
                else:
                    print("Indice fuera de rango. ")
            except ValueError:
                print("Entrada invalida. ")

    elif opcion == "4":
        print("Saliendo del programa. ")
        break
    else:
        print("Opcion invalida. ")
"""

tareas  = []

while True:

    print("Opciones: 1. Agregar 2. Ver 3. Borrar 4. Salir")

    opcion = input("Elija una opcion (1-4): ")

    if opcion == "1":
        nueva_tarea = input("Ingrese la tarea: ")
        tareas.append(nueva_tarea)
        print("Tarea agregada. ")

    elif opcion == "2":
        print(tareas)
        
    elif opcion == "3":
        if len(tareas)>0:
            tareas.pop()
            print("Tarea borrada. ")
        else:
            print("No hay tareas para borrar")

    elif opcion == "4":
        print("Saliendo del programa. ")
        break
    
    else:
        print("Opcion invalida.")

print(tareas)

