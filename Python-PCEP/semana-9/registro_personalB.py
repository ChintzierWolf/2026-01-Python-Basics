"""
RETO AUTÓNOMO: registro_personal.py (50 minutos de construcción + 25 de QA)

Un área de RRHH necesita un registro en consola para dar de alta empleados,
listarlos y buscarlos. Los empleados se guardan en UNA lista; cada empleado
es UN diccionario.

── ESTRUCTURA DE DATOS ─────────────────────────────────────────────
  registro = []                      # la lista que contendrá los expedientes
  cada empleado es un dict con las claves:
     "nombre"           (str)
     "departamento"     (str)
     "salario_mensual"  (float)
     "nivel_acceso"     (int, 1-5)

── OPERACIÓN 1: ALTA ───────────────────────────────────────────────
  Pedir los 4 datos por input() con el casting correcto.
  Construir el diccionario del empleado.
  Agregarlo a la lista con .append().
  El sistema debe permitir dar de alta AL MENOS 3 empleados.
  (Sugerencia: usa un bucle que pregunte "¿Agregar otro? (si/no)")

── OPERACIÓN 2: LISTADO ────────────────────────────────────────────
  Recorrer la lista con for.
  Por cada empleado, imprimir sus campos de forma legible.
  Numerar cada expediente (Empleado 1, Empleado 2, ...).
  Si la lista está vacía, avisar "No hay empleados registrados"
  (NO debe reventar ni imprimir una lista vacía silenciosa).

── OPERACIÓN 3: BÚSQUEDA POR NOMBRE ────────────────────────────────
  Pedir un nombre.
  Recorrer la lista buscando un empleado cuyo "nombre" coincida.
  Si lo encuentra: imprimir su expediente completo.
  Si NO lo encuentra: imprimir "Empleado no encontrado" (sin reventar).
  GUARDIA OBLIGATORIA: leer empleado["nombre"] de forma que NO lance
  KeyError aunque algún expediente esté incompleto (usa in o .get()).

── FORMATO DE SALIDA (mínimo) ──────────────────────────────────────
  Empleado 1
    nombre: Ana García
    departamento: Finanzas
    salario_mensual: 45000.0
    nivel_acceso: 4

── BONUS (solo si terminas; NO obligatorio) ───────────────────────
  Bonus A: contar cuántos empleados hay por departamento.
  Bonus B (marcado CLASE 10, no lo hagas aún): normalizar el nombre
           con .strip() y .lower() antes de buscar. Se trabaja la próxima clase.

Archivo: registro_personal.py
"""

# Lista principal que contendrá los expedientes (diccionarios) de cada empleado
registro = []

# Tupla con las opciones válidas del menú para validar la entrada del usuario
OPCIONES_VALIDAS = ("1", "2", "3", "4")

def mostrar_menu():
    """Muestra en consola las opciones del menú principal."""
    print("\n===== Registro de empleados =====")
    print("=================================")
    print("1. Realizar ALTA de empleado")
    print("2. Listar la lista de empleados")
    print("3. Buscar empleado por nombre")
    print("4. Salir")

def funcion_alta():
    """
    Operación 1: Solicita los 4 datos con el casting requerido, construye
    el diccionario y lo añade a la lista 'registro'.
    Permite registrar varios empleados seguidos gracias a una condición de salida.
    """
    # Bucle que permite registrar uno o varios empleados consecutivos
    while True:
        print("\n--- Alta de Empleado ---")
        var_nombre = input("Introduce el nombre a agregar: ")
        var_departamento = input("Introduce el departamento al que pertenece: ")
        var_salario_mensual = float(input("Introduce el Salario Mensual: "))
        var_nivel_de_acceso = int(input("Ingresa el nivel de acceso (1-5): "))
        
        # Construcción del diccionario con las claves exactas especificadas en el reto
        empleado = {
            "nombre": var_nombre,
            "departamento": var_departamento,
            "salario_mensual": var_salario_mensual,
            "nivel_acceso": var_nivel_de_acceso
        }

        # Agregamos el diccionario a la lista 'registro' usando .append()
        registro.append(empleado)
        print(f"Empleado '{var_nombre}' registrado con éxito.")

        # Control de salida: pregunta al usuario si desea continuar o volver al menú principal
        # Evita que el programa se quede atrapado en un bucle infinito
        respuesta = input("\n¿Deseas agregar otro empleado? (s/n): ")
        if respuesta.lower() not in ("s", "si"):
            # Si el usuario ingresa 'n' o cualquier otra respuesta, rompemos el ciclo y volvemos al menú
            break

def funcion_listar():
    """
    Operación 2: Recorre la lista de empleados y muestra cada campo numerado.
    Si la lista está vacía, muestra un mensaje informativo sin causar errores.
    """
    print("\n--- Listado de Empleados ---")
    # Validación: verificar si la lista 'registro' no tiene elementos
    if len(registro) == 0:
        print("No hay empleados registrados")
        return

    # Si hay elementos, recorremos la lista con un contador para numerar cada empleado (1, 2, 3...)
    contador = 1
    for empleado in registro:
        print(f"\nEmpleado {contador}")
        
        for llave, valor in empleado.items():
            print(f"Empleado numero {contador}")
        contador += 1

def funcion_buscar():
    """
    Operación 3: Solicita un nombre y busca si existe en la lista de empleados.
    Utiliza .get() como guardia para evitar KeyError si una clave faltase.
    """
    print("\n--- Búsqueda de Empleado ---")
    nombre_a_buscar = input("Introduce el nombre a buscar: ")

    # Bandera booleana para rastrear si encontramos alguna coincidencia
    encontrado = False

    # Recorremos la lista de empleados buscando coincidencia en el nombre
    for empleado in registro:
        # GUARDIA OBLIGATORIA: uso de .get('nombre') para no lanzar KeyError
        if empleado.get("nombre") == nombre_a_buscar:
            print("\nExpediente encontrado:")
            print(f"  nombre: {empleado.get('nombre')}")
            print(f"  departamento: {empleado.get('departamento')}")
            print(f"  salario_mensual: {empleado.get('salario_mensual')}")
            print(f"  nivel_acceso: {empleado.get('nivel_acceso')}")
            encontrado = True
            break  # Detenemos la búsqueda al encontrar la coincidencia

    # Si la bandera sigue en False tras recorrer toda la lista, no existe ese registro
    if not encontrado:
        print("Empleado no encontrado")

def funcion_salir():
    """Muestra un mensaje de salida al usuario."""
    print("\nSaliendo del sistema... ¡Hasta luego!")

# Ciclo principal del programa que mantiene el menú activo
while True:
    mostrar_menu()
    opcion = input("\nElige una opción (1-4): ")

    # Validación de entrada: verificamos que la opción ingresada esté en OPCIONES_VALIDAS
    if opcion not in OPCIONES_VALIDAS:
        print("\n[!] Opción no válida. Por favor, selecciona un número del 1 al 4.")
        continue

    # Ejecución de la función según la opción seleccionada
    if opcion == "1":
        funcion_alta()
    elif opcion == "2":
        funcion_listar()
    elif opcion == "3":
        funcion_buscar()
    elif opcion == "4":
        funcion_salir()
        break  # Rompe el ciclo while principal y finaliza el programa
    opcion = input("\nElige una opción (1-4): ")
