"""
INICIO  ·  tareas = []  ·  OPCIONES_VALIDAS = ("1".."6")
while True:
 ├─ mostrar_menu()  ·  opcion = input()
 ├─ "1" → texto = input() → tareas.append(texto)
 ├─ "2" → listar_tareas(tareas)
 ├─ "3" → numero = int(input())  →  indice = numero - 1
 │        ├─ if 0 <= indice < len(tareas): tareas.pop(indice)
 │        └─ else: "Esa tarea no existe"
 ├─ "4" → for t in sorted(tareas): print(t)   (original intacto)
 ├─ "5" → resumen(tareas, 4)
 ├─ "6" → break → FIN
 └─ else → "Opción no válida"

 gestor con menú while True, ≥3 mini-funciones, 
 lista dinámica, ordenamiento bajo demanda, métrica con math, 
 y validación de índice. 
 El QA prueba 11 casos. 
 Qué NO busca: no se usa try/except (Sprint 6) — robustez con if+len(). 
 
 """

import math

tareas = []

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Ordenar tareas")
    print("5. Resumen de tareas")
    print("6. Salir\n")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion not in ("1","2","3","4","5","6"):
        print("Opcion no valida")
        continue
    
    #1 AGREGAR TAREA
    if opcion == "1":
        tarea = input("Ingrese la tarea: ")
        tareas.append(tarea)

    #2 LISTAR TAREAS
    elif opcion == "2":
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}.- {tarea}")

    #3 ELIMINAR TAREA
    elif opcion == "3":
        numero = int(input("Ingrese el numero de la tarea a eliminar: "))
        indice = numero - 1

        #Validamos que el numero sea correcto
        if 0 <= indice < len(tareas):
            # si el numero de la tarea esta en el rango de la lista, se elimina
            tareas.pop(indice)
            #pop() es un metodo que elimina un elemento de una lista dado su indice.
            #len() es la longitud de la lista
            # 0 <= indice < len(tareas) es una validacion que asegura que el indice este dentro del rango de la lista
        else:
            print("Esa tarea no existe")

    #4 ORDENAR TAREAS
    elif opcion == "4":
        for tarea in sorted(tareas):
            #sorted() es una funcion que ordena una lista de forma ascendente por defecto
            print(tarea)

    #5 RESUMEN (tareas, 4)
    elif opcion == "5":
        total_tareas = len(tareas)
        por_dia = 4
        #math.ceil() es una funcion que redondea un numero hacia arriba
        promedio = math.ceil(total_tareas / por_dia)
        #se calcula el promedio redondeado hacia arriba
        print(f"Total de tareas: {total_tareas}")
        #se imprime el promedio redondeado hacia arriba
        print(f"Promedio de tareas por dia: {promedio}")

    #6 SALIR
    elif opcion == "6":
        print("Cerrando el sistema...")
        break

    #7 OPCION INVALIDA
    else:
        print("Opcion no valida dentro del menu. Seleccione una opcion entre 1 y 6")
    