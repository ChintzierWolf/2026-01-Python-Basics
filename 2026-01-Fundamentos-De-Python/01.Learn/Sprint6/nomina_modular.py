# NÓMINA MODULAR — Refactor del espagueti
# Este script espagueti funciona, pero la tasa 0.12 está repetida 3 veces.
# Tu misión: refactorizarlo para que la tasa viva en UN SOLO LUGAR.

# --- ESPAGUETI (no tocar, solo usar de referencia) ---
# emp1_bruto = 20000 + 2000
# emp1_impuesto = emp1_bruto * 0.12
# emp1_neto = emp1_bruto - emp1_impuesto
# print(f"Empleado 1 | Bruto: {emp1_bruto} | Neto: {emp1_neto}")
# (repetido para emp2 y emp3)

# --- TU REFACTOR ---

# TODO 1: Declara tasa_impuesto = 0.12 UNA SOLA VEZ aquí arriba.

tasa_impuesto = 0.12

# TODO 2: Define calcular_pago_bruto(sueldo_base, bono)
# que devuelva con return la suma de ambos.

def calcular_pago_bruto(sueldo_base, bono):
    resultado = sueldo_base + bono
    return resultado

# TODO 3: Define calcular_neto(bruto, tasa)
# que devuelva con return bruto - (bruto * tasa).

def calcular_neto(bruto, tasa):
    resultado = bruto - (bruto * tasa)
    return resultado

# TODO 4: Define es_salario_valido(sueldo_base)
# que devuelva True si 8000 <= sueldo_base <= 200000.

def es_salario_valido(sueldo_base):
    if 8000 <= sueldo_base <= 200000:
        return True
    else:
        return False

# TODO 5: Procesa estos 3 empleados usando las funciones, validando ANTES de calcular:
# emp1: sueldo 20000, bono 2000
# emp2: sueldo 25000, bono 0
# emp3: sueldo 500, bono 100  <-- salario invalido, debe rechazarse

empleados = [
    ("Empleado 1", 20000, 2000),
    ("Empleado 2", 25000, 0),
    ("Empleado 3", 500, 100)
]

# TODO 6: Agrega un BLOQUE DE RESUMEN.
# Declara procesados = 0, rechazados = 0, total_neto = 0 ANTES del loop.
# Dentro de la rama valida suma procesados += 1 y total_neto += neto.
# Dentro de la rama rechazada suma rechazados += 1.
# Al final del loop imprime:
#   Empleados procesados: <procesados>
#   Empleados rechazados: <rechazados>
#   Total neto a depositar: $<total_neto>

procesados = 0
rechazados = 0
total_neto = 0

for nombre, sueldo, bono in empleados:
    if es_salario_valido(sueldo):
        bruto = calcular_pago_bruto(sueldo, bono)
        neto = calcular_neto(bruto, tasa_impuesto)
        print(f"{nombre} | Bruto: ${bruto} | Neto: ${neto}")
        procesados += 1
        total_neto += neto
    else:
        print(f"{nombre} | RECHAZADO: salario fuera de rango ({sueldo})")
        rechazados += 1

# El ejercicio espera que los empleados se procesen dentro de un ciclo for para evitar duplicar código 
# (que es justo lo que el ejercicio llama "refactor del espagueti"). 
# Para ello, en el TODO 5 los 3 empleados deben agruparse en una lista iterable 
# (por ejemplo, una lista de tuplas con el nombre, sueldo y bono).

# Las funciones creadas no se estaban utilizando: 
# Se definieron calcular_pago_bruto, calcular_neto y es_salario_valido, pero no se invocaban en ninguna parte.

# Faltan las impresiones individuales y el símbolo $: 
# En cada iteración del loop se debe mostrar el resultado del empleado o el motivo de rechazo, 
# tal como lo indica la salida esperada al final del archivo:

print(f"Empleados procesados: {procesados}")
print(f"Empleados rechazados: {rechazados}")
print(f"Total neto a depositar: ${total_neto}")

# Salida esperada:
# Empleado 1 | Bruto: $22000 | Neto: $19360.0
# Empleado 2 | Bruto: $25000 | Neto: $22000.0
# Empleado 3 | RECHAZADO: salario fuera de rango (500)
# Empleados procesados: 2
# Empleados rechazados: 1
# Total neto a depositar: $41360.0