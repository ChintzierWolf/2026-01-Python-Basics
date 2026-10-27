empleado = {
    "nombre": "Ana García",
    "departamento": "Finanzas"
}

print("Procesando pago de: ", empleado["nombre"])
# print("Salario a depositar: ", empleado["salario"])

# Acecso directo: revience si la clave no existe
# empleado["salario"] # Resulta un error al ejecutarse

# Acceso defensivo: NO revienta - devuelve NONE si no existe
# empleado.get["salario"] #NONE

# Acceso defensivo con valor por defecto
print(empleado.get("salario", "no existe")) # 0 el segundo

print("nombre" in empleado)         # Si existe la key, por lo tanto imprime un True
print("departamento" in empleado)   # Si existe la key, por lo tanto imprime un True 

# Agregar un campo NUEVO que no existía
empleado["fecha_revision"] = "2026-10-30" 

print(empleado)

# Fase 3: Guardia de entrada - preguntar ANTES de leer
"""
 campo = input("¿Qué campo quieres consultar?: ")

if campo in empleado:
    print(f"{campo}: {empleado[campo]}")
else:
    print(f"Este expediente no tiene el campo '{campo}'")
"""

# Alternativa profesional con .get()
print("Telefono registrado:", empleado.get("telefono", "No registrado"))

for elemento in empleado:
    print(elemento)

# Fase 4: Inspeccion global del expediente
print("Campos registrados: ", empleado.keys())
print("Datos registrados: ", empleado.values())

# Convertir a lista si necesito indexar o contar
lista_campos = list(empleado.keys())
print("Total de campos", len(lista_campos))
print("Primer campo", lista_campos[0])
print("Len del diccionario: ", len(empleado))

# Fase  5: recorrer clave y valor a la vez
print("\n === Recorrido Completo === ")
for clave, valor in empleado.items():
    print(f"{clave}: {valor}")

# --- Estructura de datos ---

"""
 Operacion 1: Alta
 Pedir los 4 datos por input() con el casting correcto
 Construir el diccionario del empleado
 Agregarlo a la lista con .append()
 El sistema debe

"""