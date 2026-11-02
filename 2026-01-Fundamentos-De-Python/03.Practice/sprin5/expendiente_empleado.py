# Fase 1: el expediente como diccionario literal

empleado = {
    "nombre": "Ana García",
    "departamento": "Finanzas",
    "salario_mensual": "450000.00",
    "nivel_acceso": "4",
    "activo": "si"
}

print(f"El diccionario completo de empleado es: {empleado}")

# Fase 2: Ler campo específico
print(f"Empleado: {empleado['nombre']}")
print(f"Departamento: {empleado['departamento']}")
print(f"Salario Mensual: {empleado['salario_mensual']}")
print(f"Nivel de Acceso: {empleado['nivel_acceso']}")
print(f"¿Está activo?: {empleado['activo']}")

# Actualizar: Ana le suberon el sueldo 10%

empleado['salario_mensual'] = float(empleado['salario_mensual']) * 1.10
print(f"El salario tras el aumento es: ${empleado['salario_mensual']:.2f}")

# Actualizar: Ana obtuvo ascenso a "Supervisora de Finanzas"nivel 5

empleado['nivel_acceso'] = '5'
empleado['departamento'] = 'Supervisora de Finanzas'

# Agregar un campo nuevo que no existe dentro del diccionario

empleado['fecha_revision'] = '2026-10-31'
print(empleado)
print(f"La fecha de revision es: {empleado['fecha_revision']}")

# Fase 3: Guardia de entrada -- preguntar antes de leer

campo = input("¿Qué campo deseas consultar? ")

if campo in empleado:
    print(f"{campo}: {empleado[campo]}")
else:
    print(f"Error: {campo} no existe dentro del expediente.")

# Alternativa profesional con .get()

print(f"Teléfono registrado: {empleado.get('telefono', 'No registrado')}")

# Fse 4: Inspección global del expediente

print(f"Lista completa de campos: {list(empleado.keys())}")
print(f"Lista de valores: {list(empleado.values())}")

# Convertir un diccionario a lista
lista_empleado = list(empleado.items())
print(f"Diccionario convertido a lista: {lista_empleado}")
print(f"Elemento en la posicion 0 de la lista: {lista_empleado[0]}")
print(f"Elemento en la posicion 1 de la lista: {lista_empleado[1]}")


# Listar clave-valor

print(f"Recorriendo todo el diccionario:")
for clave, valor in empleado.items():
    print(f"{clave} : {valor}")

# Fase 5: Recorrer la clave y el valor a la vez

# Recorriendo solo las llaves
print("Recorriendo solo las llaves:")
for clave in empleado.keys():
    print(f"{clave}")

# Recorriendo solo los valores
print("Recorriendo solo los valores:")
for valor in empleado.values():
    print(f"{valor}")

    

