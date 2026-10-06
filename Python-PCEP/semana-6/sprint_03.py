"""
REQUERIMIENTOS OBLIGATORIOS:
Archivo guardado como menu_inadaptado.py en clase-06/
El menú muestra EXACTAMENTE estas 4 opciones, numeradas:
Crear
Ver lista
Actualizar
Salir
Motor while True: como único bucle del programa
Validación de opción inválida con continue (mensaje + volver al menú)
Opciones 1, 2, 3 muestran mensaje placeholder:"--- [Función] en construcción ---"
Opción 4 muestra "Cerrando aplicación..." y termina con break
Comparaciones del input como strings ("1", "2", "3", "4")
UN SOLO break en todo el archivo, exclusivamente en la opción 4

CRITERIOS DE VERIFICACIÓN (correr el programa y validar):
☐ ¿El programa sigue corriendo después de elegir 1, 2 o 3?
☐ ¿El programa termina limpiamente solo con la opción 4?
☐ ¿Una letra (ej. "hola") muestra el mensaje de error y vuelve al menú?
☐ ¿Un número fuera de rango (ej. "9") muestra el mensaje de error y vuelve al menú?
☐ ¿Enter en blanco muestra el mensaje de error y vuelve al menú?
☐ ¿La opción inválida usa continue (NO break)?
☐ ¿Está el break únicamente en la opción 4?
"""

while True:
    print("\n=== MENÚ INADAPTADO ===\n")
    print("1. Crear")
    print("2. Ver lista")
    print("3. Actualizar")
    print("4. Salir\n")
    
    opcion = input("Selecciona una opción: ")

    # Validar que la opción sea válida dentro del rango de opciones 1 a 4
    # Si no es válida, mostrar mensaje y volver al menú con continue
    if opcion not in ["1", "2", "3", "4"]:
        print(F"\n*** {opcion} no es una opción válida. Intenta de nuevo. ***\n")
        continue

    # Crear
    elif opcion == "1":
        print("--- Crear en construcción ---")
        continue

    # Ver lista
    elif opcion == "2":
        print("--- Ver lista en construcción ---")
        continue

    # Actualizar
    elif opcion == "3":
        print("--- Actualizar en construcción ---")
        continue

    # Salir
    elif opcion == "4":
        print("Cerrando aplicación...\n")
        break
