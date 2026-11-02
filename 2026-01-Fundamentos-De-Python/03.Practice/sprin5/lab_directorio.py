# Paso 1: Crear la lista antes de cualquier operacion
registro = []

print(f"Directorio creado. Empleados: {len(registro)}")
print(f"Contenido actual: {registro}")

# Paso 2: Crear 3 diccionarios de altas de expedientes

empleado = {
    "Nombre": "Ana García",
    "Departamento": "Finanzas",
    "salario_mensual": 45000.00,
    "nivel_acceso": 4
}

registro.append(empleado)

registro.append({
    "Nombre": "Beto Ruiz",
    "Departamento": "Sistemas",
    "salario_mensual": 38000.00,
    "nivel_acceso": 3
})

registro.append({
    "Nombre": "Carla Méndez",
    "Departamento": "Ventas",
    "salario_mensual": 41000.00,
    "nivel_acceso": 2
})

print(f"\nDirectorio Actualizado. Empleados en el directorio: {len(registro)}")

# Paso 3: Listar el directorio

print("\n === DIRECTORIO DE EMPLEADOS ===")

if len(registro) == 0:
    print("El directorio está vacío")
else:
    numero = 1
    for empleado in registro:
        print(f"\n Empleado #{numero} ")
        for clave, valor in empleado.items():
            print(f" {clave} : {valor}")
        numero += 1