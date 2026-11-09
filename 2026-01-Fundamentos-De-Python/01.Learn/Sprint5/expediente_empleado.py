# Fase 1: Expediente como diccionario literal

empleado = {
    "nombre": "Ana García",
    "departamento": "Finanzas",
    "salario_mensual": 45000.00,
    "nivel_de_acceso": 4,
    "activo": si
}

print(empleado)

# Fase 2: Leer campo específico.
print(f"Empleado: {empleado['nombre']}")
print(f"Salario actual: {empleado['salario_mensual']}")

# Actualizar: Ana le subieron el sueldo al 10%

empleado["salario_mensual"] = empleado["salario_mensual"] * 1.10
print(f"El salario tras el auemnto: {empleado['salario_mensual']}")

# Agregar un campo que no eiste en el diccionario
empleado["fecha_revision"] = "2026-06"
print(empleado)

# Fase 3: guardia de entrada -- preguntar antes de leer

campo = input("¿Qué campo quieres consultar?: ")

if campo in empleado:
    print(f"{campo}: {empleado[campo]}")
else:
    print(f"Este expediente no tiene el campo '{campo}'")

# Alternativa profesional con .get()
print(f"Teléfono registrado: {emmpleado.get("teléfono", "No registrado")}")

# Fase 4: Inspección global del expediente
print(f"Campos registrados: {empleado.keys()}")
print(f"Datos registrados: {empleado.values()}")

# Convertir a lista si es necesario

lista_campos = list(empleado.keys())
print(f"Total de campos: {len(listas_campos)}")
print(f"Primer campo: {lista_campos[0]}")

# Fase 5: Recorrer clave y valor a la vez

print(f"\n=== EXPEDIENTE COMLPETO ===")
for clave, valor in empleado.items():
    print(f"{clave} -> {valor}")

# Fase 6: Modificar el nivel de acceso de Ana
empleado['nivel_de_acceso'] = 5
print(f"El nivel de acceso actual es: {empleado.get("nivel_de_acceso", "No registrado")}")
    
