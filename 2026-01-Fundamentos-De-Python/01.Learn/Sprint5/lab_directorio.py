# Paso 1: Crear la lista antes de cualquier alta

registro = []

print(f"Directorio creado. Empleados: {len(registro)}")

# Paso 2: Crear 3 diccionarios de alta de expedientes
empleado = {
    
    "Nombre": "Ana García",
    "departamento": "Finanzas",
    "salario_mensual": 450000.00,
    "nivel_de_acceso": 4
}
    
registro.append(empleado)

registro.append({
    "nombre" : "Beto Ruiz",
    "departamento" : "Sistemas",
    "salario_mensual" : 380000.00,
    "nivel_de_acceso" : 3
})

registro.append({
    "nombre" : "Carla Méndez",
    "departamento" : "Ventas",
    "salario_mensual" : 410000.00,
    "nivel_de_acceso" : 2
})

print(f"Empleados en el directorio: {len(registro)}")

# Paso 3: Listar el directorio

print("\n=== DIRECTORIO DE EMPLEADOS 1 ===")
print(f"{'ID':<5}{'Nombre':<15}{'Depto':<10}{'Salario':>15}")
print("-" * 55)

print("\n=== DIRECTORIO DE EMPLEADOS 2 ===")

if len(registro) == 0:
    print("El directorio está vacío")
else:
    for i, empleado in registro:
        print(f"\nEmpleado {numero}")
        for clave, valor in empleado.items():
            print(f"{clave}: {valor}")
        numero += 1    
    
# Paso 4 Buscar por nombre

buscado = "Beto Ruiz"
encontrado = False

for i, empleado in registro:
    if "nombre" in empleado and empleado["nombre"] == buscado:
        print(f"\nExpediente encontrado: ")
        for clave, valor in empleado.items():
            print(f"{clave}: {valor}")
        encontrado = True

if not encontrado:
    print(f"\nNo se encontró el expediente de {buscado}")

print("\n=== DIRECTORIO DE EMPLEADOS 3 ===")

if len(registro) == 0:
    print("El directorio está vacío")
else:
    for i, empleado in enumerate(registro, start = 1):
        print(f"\nEmpleado {i}")
        for clave, valor in empleado.items():
            print(f"{clave}: {valor}")