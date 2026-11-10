"""
# nomina_espagueti.py  — PUNTO DE PARTIDA (hay que refactorizar)
# Procesa 3 empleados. La logica esta repetida y mezclada. Funciona, pero es fragil.

# --- empleado 1 ---
sueldo1 = 20000
bono1 = 2000
bruto1 = sueldo1 + bono1
impuesto1 = bruto1 * 0.12
neto1 = bruto1 - impuesto1
print(f"Empleado 1 | Bruto: ${bruto1} | Impuesto: ${impuesto1} | Neto: ${neto1}")

# --- empleado 2 ---
sueldo2 = 25000
bono2 = 0
bruto2 = sueldo2 + bono2
impuesto2 = bruto2 * 0.12
neto2 = bruto2 - impuesto2
print(f"Empleado 2 | Bruto: ${bruto2} | Impuesto: ${impuesto2} | Neto: ${neto2}")

# --- empleado 3 ---
sueldo3 = 500          # OJO: salario sospechoso, pero el espagueti lo procesa igual
bono3 = 100
bruto3 = sueldo3 + bono3
impuesto3 = bruto3 * 0.12
neto3 = bruto3 - impuesto3
print(f"Empleado 3 | Bruto: ${bruto3} | Impuesto: ${impuesto3} | Neto: ${neto3}")
"""

SALARIO_MINIMO = 1000
IMPUESTO = 0.12

def procesar_empleado(numero, sueldo, bono):

    if sueldo < SALARIO_MINIMO:
        print(
            f"Empleado {numero} | "
            f"RECHAZADO: salario fuera de rango ({sueldo:.2f})"
        )
        return False, 0

    bruto = sueldo + bono
    impuesto = bruto * IMPUESTO
    neto = bruto - impuesto

    print(
        f"Empleado {numero} | "
        f"Bruto: ${bruto:.2f} | "
        f"Neto: ${neto:.2f}"
    )

    return True, neto


empleados = [
    (1, 20000, 2000),
    (2, 25000, 0),
    (3, 500, 100)
]

empleados_procesados = 0
empleados_rechazados = 0
total_neto = 0

for numero, sueldo, bono in empleados:

    valido, neto = procesar_empleado(numero, sueldo, bono)

    if valido:
        empleados_procesados += 1
        total_neto += neto
    else:
        empleados_rechazados += 1

print()
print(f"Empleados procesados: {empleados_procesados}")
print(f"Empleados rechazados: {empleados_rechazados}")
print(f"Total neto a depositar: ${total_neto:.2f}")
