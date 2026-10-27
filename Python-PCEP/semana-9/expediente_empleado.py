"""
CONTEXTO: Expediente Digital de Empleado
RRHH está migrando los expedientes de papel a un sistema de consola.
Cada empleado es un expediente con campos rotulados. Hoy construimos
el manejo de un expediente; la procima fase será el directorio completo

Campos del expediente:
+ nombre            (str)
+ departamento      (str)
+ salario_mensual   (float)
+ nivel_acceso      (int, 1-5)
+ activo            (str: "si"/"no")

Archivo: expediente_empleado.py

Ana Garcia, Finanzas, 45000.00, nivel: 4, activo: si

"""

empleado = {
    "nombre": "Ana Garcia",
    "departamento": "Finanzas",
    "salario_mensual": 45000.00,
    "nivel_acceso": 4,
    "activo": "si"
}

print(empleado)

# Fase 2: Leer un campo específico

print("Empleado: ", empleado["nombre"])
print("Salario actual: ", empleado["salario_mensual"])

# Actualizar: a Ana le subieron el sueldo 10%
empleado["salario_mensual"] = empleado["salario_mensual"] * 1.1
print("Salario tras el aumento: ", empleado["salario_mensual"])

