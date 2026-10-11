# ENTREGABLE SPRINT 3: MENÚ INTERACTIVO

# TODO 1: Importa el módulo random hasta arriba del archivo.

# TODO 2: Crea una variable 'operaciones = 0' fuera del bucle.
# Esta variable debe sobrevivir entre vueltas y contar cuántas operaciones
# útiles realizó el usuario.

# TODO 3: Abre un bucle infinito con 'while True:'.
# Dentro del bucle, imprime un menú con exactamente estas 4 opciones,
# cada una en su propia línea:
#   1. Lanzar dado
#   2. Generar número aleatorio (1-100)
#   3. Ver contador de operaciones
#   4. Salir

# TODO 4: Lee la opción del usuario con input() y guárdala como string
# (NO la conviertas a int — así no se rompe si escribe letras).

# TODO 5: Usa if/elif/else para decidir qué hacer con cada opción:
#   - "1": genera un dado con random.randint(1, 6), imprímelo
#     y suma 1 a 'operaciones'.
#   - "2": genera un número con random.randint(1, 100), imprímelo
#     y suma 1 a 'operaciones'.
#   - "3": imprime el valor actual de 'operaciones'.
#     (NO suma — solo es consulta.)
#   - "4": imprime un mensaje de despedida con el total final
#     de operaciones y usa break para salir del bucle.
#   - Cualquier otro valor (else): imprime un mensaje de opción inválida.
#     El bucle debe volver a mostrar el menú automáticamente.

# TODO 6: Fuera del bucle, imprime un mensaje final como
# "Programa terminado.".

import random
operaciones = 0

while True:
    print("\n--- MENÚ INTERACTIVO ---")
    print("1. Lanzar dado")
    print("2. Generar número aleatorio (1-100)")
    print("3. Ver contador de operaciones")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida. Intenta de nuevo.")
        continue

    if opcion == "1":
        print("Has lanzado el dado.")
        numero_dado = random.randint(1, 6)
        print("El numero es: ", numero_dado)
        operaciones += 1
        continue
    
    elif opcion == "2":
        print("Has generado un número aleatorio.")
        numero_random = random.randint(1, 100)
        print("El numero es: ", numero_random)
        operaciones += 1
        continue
    
    elif opcion == "3":
        print("El contador de operaciones es: ", operaciones)
        continue
    
    elif opcion == "4":
        print("Has salido del programa. Has realizado: ",operaciones," operaciones.")
        break

print("Programa terminado.")