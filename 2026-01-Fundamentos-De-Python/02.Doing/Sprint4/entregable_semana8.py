# ENTREGABLE SPRINT 4: GESTOR DE TAREAS V2
# Integra todo el sprint: listas, funciones, ordenamiento, math y validación de índice.

# TODO 1: Importa el módulo math al inicio (lo necesitas para math.ceil más abajo).

# TODO 2: Crea una lista vacía 'tareas' al nivel global (antes de las funciones).
# Vive aquí para sobrevivir entre vueltas del menú.

# TODO 3: Crea una tupla 'OPCIONES_VALIDAS' con los strings "1" a "6".
# Es tupla porque el catálogo de opciones no cambia.

# ===== FUNCIONES =====

# TODO 4: Define 'mostrar_menu()' sin parámetros. Imprime las 6 opciones:
#   1. Agregar tarea   2. Listar tareas   3. Eliminar tarea
#   4. Ordenar A-Z (vista)   5. Resumen (días mínimos)   6. Salir

# TODO 5: Define 'listar_tareas(lista)' que reciba la lista como parámetro.
# - Si está vacía, imprime "No hay tareas registradas."
# - Si no, imprime cada tarea numerada desde 1 (usa una variable que crezca en el for).

# TODO 6: Define 'resumen(lista, por_dia)'.
# - Si la lista está vacía, avisa que son 0 días.
# - Si no, calcula los días con math.ceil(total / por_dia) e imprímelos.

# ===== MENÚ PRINCIPAL =====

# TODO 7: Abre un bucle 'while True:'. Al inicio de cada vuelta llama a mostrar_menu()
# y lee la opción con input() como STRING (no la conviertas a int).

# TODO 8: opción "1" → pide el texto de la tarea con input() y agrégalo con .append().
# Imprime confirmación con el total actual.

# TODO 9: opción "2" → llama a listar_tareas(tareas).

# TODO 10: opción "3" → eliminar por número CON validación de índice.
# - Si la lista está vacía, avisa y no hagas nada más.
# - Si no, lista las tareas, pide el número, conviértelo a índice (numero - 1)
#   y valida con 'if indice >= 0 and indice < len(tareas):' antes de .pop(indice).
# - Si el índice no es válido, imprime que la tarea no existe (NO debe tronar).

# TODO 11: opción "4" → vista A-Z con sorted(tareas), numerada.
# Después confirma que la lista original NO cambió de orden.

# TODO 12: opción "5" → llama a resumen(tareas, 4).

# TODO 13: opción "6" → imprime despedida y usa break para salir del bucle.

# TODO 14: cualquier otra opción → imprime "Opción no válida. Elige del 1 al 6."

# TODO 1
import math

# TODO 2
tareas = []

# TODO 3
OPCIONES_VALIDAS = ("1", "2", "3", "4", "5", "6")

# ===== FUNCIONES =====

# TODO 4
def mostrar_menu():
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Ordenar A-Z (vista)")
    print("5. Resumen (días mínimos)")
    print("6. Salir")

# TODO 5
def listar_tareas(lista):
    if not lista:
        print("No hay tareas registradas.")
    else:
        for indice1, tarea in enumerate(lista):
            print(f"{indice1 + 1}. {tarea}")

# TODO 6
def resumen(lista, por_dia):
    if not lista:
        print("No hay tareas registradas. Son 0 días.")
    else:
        total = len(lista)
        dias = math.ceil(total / por_dia)
        print(f"Se necesitan {dias} días para completar {total} tareas, haciendo {por_dia} al día.")

# ===== MENÚ PRINCIPAL =====

# TODO 7
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-6): ")

# TODO 8
    if opcion == "1":   
        tarea = input("Introduce la tarea a agregar: ")
        tareas.append(tarea)
        print(f"Tarea agregada. Total: {len(tareas)}.")

# TODO 9
    elif opcion == "2":
        listar_tareas(tareas)

# TODO 10
    elif opcion == "3":
        if not tareas:
            print("No hay tareas registradas.")
        else:
            listar_tareas(tareas)
            try:
                num = int(input("Teclea el número de tarea a eliminar: "))
                indice = num - 1
                if 0 <= indice < len(tareas):
                    tarea_eliminada = tareas.pop(indice)
                    print(f"Eliminada: {tarea_eliminada}.")
                else:
                    print("Esa tarea no existe.")
            except ValueError:
                print("Entrada inválida.")

# TODO 11
    elif opcion == "4":
        vista_ordenada = sorted(tareas)
        listar_tareas(vista_ordenada)
        print("La lista original no cambió de orden.")

# TODO 12
    elif opcion == "5":
        resumen(tareas, 4)

# TODO 13
    elif opcion == "6":
        print("Adiós, nos vemos pronto.")
        break

# TODO 14
    else:
        print("Opción no válida. Elige del 1 al 6.")
