tareas = []

def mostar_menu():
    print("\nOpciones: ")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Borrar tarea")
    print("4. Salir")

def agregar_tarea():
    tarea = input("Introduce la tarea: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def ver_tareas():
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("\nLista de tareas pendientes:")
        for indice1, tarea in enumerate(tareas):
            print(f"{indice1 + 1}. {tarea}")

def borrar_tarea():
    if not tareas:
        print("No hay tareas por borrar.")
    else:
        indice2 = int(input("Introduce el numero de la tarea a borrar: ")) - 1
        if 0 <= indice2 < len(tareas):
            tarea_borrada = tareas.pop(indice2)
            print(f"Tarea '{tarea_borrada}' borrada.")
        else:
            print("Numero de tarea invalido.")

while True:
    mostar_menu()

    opcion = int(input("Selecciona una opcion del menú(1-4): "))

    if opcion == 1:
        agregar_tarea()

    elif opcion == 2:
        ver_tareas()
    
    elif opcion == 3:
        borrar_tarea()
    
    elif opcion == 4:
        print("Cerrando el programa...")
        break
    
    else:
        print("Opcion invalida, selecciona una opcion entre 1 y 4.")