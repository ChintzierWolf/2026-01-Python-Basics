# Sistema de Gestión de Reclutas - Sprint 5 ENTREGABLE

print("=== SISTEMA DE GESTIÓN DE RECLUTAS ===\n")

base_reclutas = [
    {
        "nombre" : "Ana Torres",
        "area" : "Finanzas",
        "salario_mensual" : 28500.0,
        "estatus" : "activo",
        "email": "ana.torres@inadaptados.mx"
    },
    {
        "nombre" : "Luis Quintero",
        "area" : "Logística",
        "salario_mensual" : 19200.0,
        "estatus" : "activo",
        "email": "luis.quintero@inadaptados.mx"
    },
    {
        "nombre" : "María Ibarra",
        "area" : "Salud",
        "salario_mensual" : 133750.0,
        "estatus" : "inactivo",
        "email": "maria.ibarra@inadaptados.mx"
    }
]

"""
Funcionalidades del Sistema
Tu sistema de gestión de reclutas debe tener:

1. Alta de recluta - Agregar nuevo recluta con validación
2. Listar todos - Mostrar tabla formateada de todos los reclutas
3. Buscar por nombre - Filtrar reclutas por nombre
4. Actualizar puntos - Modificar puntos de un recluta existente
5. Estadísticas - Mostrar total de reclutas, promedio de puntos, etc.
"""

while True:
    print("\n === BASE DE RECLUTAS INADAPTADOS === ")
    print("1 Alta de recluta")
    print("2 Listar todos")
    print("3 Buscar por nombre")
    print("4 Actualizar puntos")
    print("5 Estadísticas")
    print("6 Salir del programa")

    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        nombre = input("Nombre: ").strip().title()
        area = input("Area: ").strip().title()
        salario = float(input("Salario mensual: ").strip())
        estatus = input("Estatus: (Activo / Inactivo): ").strip().lower()
        email = input("Email: ").strip().lower()

        recluta = {
            "nombre": nombre,    
            "area": area,
            "salario_mensual": salario,
            "estatus": estatus,
            "email": email
        }

        base_reclutas.append(recluta)
        print("\n ¡Recluta agregado exitosamente!")

    if opcion == "2":    
        print(f"\n{'NOMBRE':<18}{'AREA':<14}{'STATUS':<11}{'SALARIO':>14}")
        print("-" * 57)

        for recluta in base_reclutas:
            print(f"\n{recluta["nombre"]:<18}{recluta["area"]:<14}{recluta["estatus"]:<11}{recluta["salario_mensual"]:>14,.2f}")

        print("-" * 57)
        print(f"Total de reclutas: {len(base_reclutas)}")

    elif opcion == "3":
        termino = input("Buscar nombre: ").strip().lower()
        encontrados = 0

        for recluta in base_reclutas:
            if termino in reclutas["nombre"].lower():
                print(f"-> {recluta[nombre]} | {recluta["area"]} | {recluta["email"]}")
                encontrados += 1
        
        if encontrados == 0:
            print(f"No se encontraron reclutas con el nombre: {termino}")

    elif opcion == "4":
        termino = input("Buscar nombre: ").strip().lower()
        encontrados = 0
        posicion = 0

        for recluta in base_reclutas:
            if termino in recluta["nombre"].lower():
                print(f"-> {recluta["nombre"]} | {recluta["area"]} | {recluta["salario"]}")
                salario_nuevo = float(input("Salario Nuevo: "))
                
                recluta["salario_mensual"] = salario_nuevo
                base_reclutas.pop(posicion)
                base_reclutas.append(recluta)
                
                encontrados += 1
                break

            posicion += 1
        if encontrados == 0:
            print(f"No se encontraron reclutas con el nombre: {termino}")

    if opcion == "6":
        break