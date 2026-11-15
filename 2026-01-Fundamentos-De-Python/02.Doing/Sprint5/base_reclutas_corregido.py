# Sistema de Gestión de Reclutas - Sprint 5 ENTREGABLE

print("=== SISTEMA DE GESTIÓN DE RECLUTAS ===\n")

reclutas = [
  {"nombre": "Ana López", "edad": 25, "email": "ana@example.com", "rango": "Aprendiz", "puntos": 200},
  {"nombre": "Luis García", "edad": 30, "email": "luis@example.com", "rango": "Experto", "puntos": 500},
  {"nombre": "Carlos Ruiz", "edad": 22, "email": "carlos@example.com", "rango": "Novato", "puntos": 100}
]

# TODO 1: Define limpiar_string(texto).
# Retorna el texto sin espacios extremos (.strip()).

def limpiar_string(texto):
    return texto.strip()

# TODO 2: Define validar_email(email).
# Limpia el email con .strip().lower().
# Retorna True si contiene "@" y el dominio (parte después del "@") tiene ".".

def validar_email(email):
    email = email.strip().lower()
    if "@" not in email:
        return False
    domain = email.split("@")[1]
    return "." in domain

# TODO 3: Define dar_alta_recluta().
# Pide: nombre, edad (str), email con input().
# Valida que edad.isdigit() y que 18 <= int(edad) <= 100; si no, imprime error y retorna.
# Valida el email con validar_email(); si no, imprime error y retorna.
# Limpia nombre con limpiar_string().title() y email con .strip().lower().
# Arma el diccionario con nombre, edad (int), email, rango="Novato", puntos=0.
# Agrega a reclutas con .append() e imprime confirmación.

def dar_alta_recluta():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    email = input("Email: ")

    if not edad.isdigit() or not (18 <= int(edad) <= 100):
        print("Error: La edad debe ser un número entero entre 18 y 100.")
        return

    if not validar_email(email):
        print("Error: El email no es válido.")
        return

    nombre = limpiar_string(nombre).title()
    email = email.strip().lower()

    nuevo_recluta = {
        "nombre": nombre,
        "edad": int(edad),
        "email": email,
        "rango": "Novato",
        "puntos": 0
    }
    reclutas.append(nuevo_recluta)
    print(f"Recluta {nombre} dado de alta exitosamente.")

# TODO 4: Define listar_reclutas().
# Si reclutas está vacío, avisa y retorna.
# Imprime encabezado: "#" (4), "Nombre" (20), "Edad" (6), "Rango" (12), "Puntos" (8)
# Imprime separadora de "-" * 52.
# Recorre reclutas con enumerate(reclutas, 1) y muestra cada fila alineada,
# con puntos formateados con :>8, (separador de miles).
# Imprime el total al final.

def listar_reclutas():
    if not reclutas:
        print("No hay reclutas registrados.")
        return

    print("\n=== LISTA DE RECLUTAS ===")
    print(f"{'#':<4}{'Nombre':<20}{'Edad':<6}{'Rango':<12}{'Puntos':>8}")
    print("-" * 52)
    for i, recluta in enumerate(reclutas, 1):
        print(f"{i:<4}{recluta['nombre']:<20}{recluta['edad']:<6}{recluta['rango']:<12}{recluta['puntos']:>8,}")
    print("-" * 52)
    print("Total: {} reclutas".format(len(reclutas)))

# TODO 5: Define buscar_recluta().
# Pide un término con input() y normaliza con .strip().lower().
# Busca el término en recluta["nombre"].lower() usando 'in' (búsqueda parcial).
# Si no encontró nada, avisa. Si sí, imprime nombre, email y rango de cada resultado.

def buscar_recluta():
    termino = input("Término de búsqueda: ").strip().lower()
    resultados = [r for r in reclutas if termino in r["nombre"].lower()]
    if not resultados:
        print("No se encontraron reclutas.")
    else:
        for r in resultados:
            print(f"Nombre: {r['nombre']}, Email: {r['email']}, Rango: {r['rango']}")

# TODO 6: Define actualizar_puntos().
# Muestra la lista numerada de reclutas con sus puntos actuales.
# Pide selección numérica; valida con .isdigit() y que el índice esté en rango.
# Pide puntos a agregar (permite negativos: valida con puntos_str.lstrip("-").isdigit()).
# Suma con += al recluta seleccionado e imprime confirmación.

def actualizar_puntos():
    listar_reclutas()
    if not reclutas:
        return

    seleccion = input("Seleccione el número del recluta: ").strip()
    if not seleccion.isdigit() or not 1 <= int(seleccion) <= len(reclutas):
        print("Selección inválida.")
        return
    puntos_str = input("Ingrese los puntos a agregar (puede ser negativo): ").strip()
    if not puntos_str.lstrip("-").isdigit():
        print("Puntos inválidos.")
        return
    reclutas[int(seleccion) - 1]["puntos"] += int(puntos_str)
    print("Puntos actualizados correctamente.")

# TODO 7: Define mostrar_estadisticas().
# Si reclutas está vacío, avisa y retorna.
# Calcula: total, puntos_totales (usa sum()), promedio.
# Encuentra el top con max(reclutas, key=lambda r: r["puntos"]).
# Cuenta por rango con el patrón: rangos[rango] = rangos.get(rango, 0) + 1
# Imprime todo de forma legible.

def mostrar_estadisticas():
    total = len(reclutas)
    if total == 0:
        print("No hay reclutas para mostrar estadísticas.")
        return

    puntos_totales = sum(r["puntos"] for r in reclutas)
    promedio = puntos_totales / total
    top = max(reclutas, key=lambda r: r["puntos"])

    rangos = {}
    for r in reclutas:
        rangos[r["rango"]] = rangos.get(r["rango"], 0) + 1

    print("\n=== ESTADÍSTICAS ===")
    print(f"Total de reclutas: {total}")
    print(f"Puntos totales: {puntos_totales:,}")
    print(f"Promedio de puntos: {promedio:.2f}")
    print(f"Top recluta: {top['nombre']} ({top['puntos']} puntos)")
    print("Distribución por rango:")
    for rango, cantidad in rangos.items():
        print(f"  {rango}: {cantidad}")

# TODO 8: Implementa el menú principal con while True.
# Imprime 6 opciones: Alta, Listar, Buscar, Actualizar, Estadísticas, Salir.
# Lee la opción con input().strip() y llama a la función correspondiente.
# La opción "6" imprime despedida y hace break.
# Cualquier otra opción muestra un mensaje de error.

while True:
    print("\n === BASE DE RECLUTAS INADAPTADOS === ")
    print("1. Dar de alta un recluta")
    print("2. Listar todos los reclutas")
    print("3. Buscar un recluta")
    print("4. Actualizar puntos")
    print("5. Estadísticas")
    print("6. Salir del programa")
    opcion = input("Seleccione una opción: ").strip()
    if opcion == "1":
        dar_alta_recluta()
    elif opcion == "2":
        listar_reclutas()
    elif opcion == "3":
        buscar_recluta()
    elif opcion == "4":
        actualizar_puntos()
    elif opcion == "5":
        mostrar_estadisticas()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")