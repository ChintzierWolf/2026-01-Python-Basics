# Paso 1: Crear una lista vacía antes del ciclo while.
registro = []

# Paso 2: Creación o inicialización de variables antes del ciclo while.
continua = "si"

while continua == "si":
    nombre = input("Nombre del empleado: ")
    departamento = input("Departamento del empleado: ")
    salario_mensual = input("Salario mensual del empleado ($): ")
    nivel_de_acceso = input("Nivel de acceso del empleado (1-5): ")

    empleado = {
        "nombre": nombre,
        "departamento": departamento,
        "salario_mensual": salario_mensual,
        "nivel_de_acceso": nivel_de_acceso
    }

    # Paso 3: Añadir el diccionario a la lista usando append.
    registro.append(empleado)

    # Paso 4: Preguntar si el usuario quiere continuar y actualizar la variable.
    continua = input("¿Desea continuar? (si/no): ")

    # -- Operación: Listado --

    # Paso 5: Listado de los empleados
    print("\n=== LISTADO DE EMPLEADOS ===")

    if len(registro) == 0:
        print("No hay empleados registrados.")
    else:
        for empleado in registro:
            print(f"Nombre: {empleado['nombre']}")
            print(f"Departamento: {empleado['departamento']}")
            print(f"Salario Mensual: ${empleado['salario_mensual']}")
            print(f"Nivel de Acceso: {empleado['nivel_de_acceso']}")
            print("")

    # -- Operación: Calcular Salario Total --

    # Paso 6: Sumar salarios
    salario_total = 0
    for empleado in registro:
        salario_total += float(empleado['salario_mensual'])
    
    print(f"Salario total: ${salario_total}")

    # -- Operación: Filtrar por Departamento --

    # Paso 7: Filtrar por departamento
    departamento_filtro = input("Departamento a filtrar: ")
    empleados_departamento = []
    for empleado in registro:
        if empleado['departamento'] == departamento_filtro:
            empleados_departamento.append(empleado)
    
    print(f"Empleados del departamento {departamento_filtro}: {empleados_departamento}")

    # -- Operación: Buscar por Nombre --

    # Paso 8: Buscar por nombre
    nombre_buscado = input("Nombre a buscar por nombre: ")
    empleado_encontrado = False

    for empleado in registro:
        if "nombre" in empleado and empleado["nombre"] == nombre_buscado:
            print("\n=== Expediente de empleado encontrado ===")

            for clave, valor in empleado.items():
                print(f"{clave.replace('_', ' ').capitalize()}: {valor}")

            empleado_encontrado = True
            break
    
    if not empleado_encontrado:
        print(f"No se encontró al empleado {nombre_buscado}")

    # -- Operación: Eliminar Empleado --

    # Paso 9: Eliminar empleado
    nombre_eliminar = input("Nombre del empleado a eliminar: ")
    empleado_encontrado = None
    for empleado in registro:
        if empleado['nombre'] == nombre_eliminar:
            empleado_encontrado = empleado
            break
    
    if empleado_encontrado:
        registro.remove(empleado_encontrado)
        print(f"Empleado {nombre_eliminar} eliminado correctamente.")
    else:
        print(f"No se encontró al empleado {nombre_eliminar}")

    # -- Operación: Actualizar Datos --

    # Paso 10: Actualizar datos
    nombre_actualizar = input("Nombre del empleado a actualizar: ")
    empleado_encontrado = None
    for empleado in registro:
        if empleado['nombre'] == nombre_actualizar:
            empleado_encontrado = empleado
            break
    
    if empleado_encontrado:
        print(f"Actualizando datos de {nombre_actualizar}")
        nuevo_salario = input("Nuevo salario mensual: ")
        empleado_encontrado['salario_mensual'] = nuevo_salario
        print(f"Datos actualizados: {empleado_encontrado}")
    else:
        print(f"No se encontró al empleado {nombre_actualizar}")

    # Paso 11: Repetir el proceso
    
    