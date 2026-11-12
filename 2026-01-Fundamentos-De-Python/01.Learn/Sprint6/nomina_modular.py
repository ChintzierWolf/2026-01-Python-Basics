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

# TODO 2: Define calcular_pago_bruto(sueldo_base, bono)
# que devuelva con return la suma de ambos.

# TODO 3: Define calcular_neto(bruto, tasa)
# que devuelva con return bruto - (bruto * tasa).

# TODO 4: Define es_salario_valido(sueldo_base)
# que devuelva True si 8000 <= sueldo_base <= 200000.

# TODO 5: Procesa estos 3 empleados usando las funciones, validando ANTES de calcular:
# emp1: sueldo 20000, bono 2000
# emp2: sueldo 25000, bono 0
# emp3: sueldo 500, bono 100  <-- salario invalido, debe rechazarse

# TODO 6: Agrega un BLOQUE DE RESUMEN.
# Declara procesados = 0, rechazados = 0, total_neto = 0 ANTES del loop.
# Dentro de la rama valida suma procesados += 1 y total_neto += neto.
# Dentro de la rama rechazada suma rechazados += 1.
# Al final del loop imprime:
#   Empleados procesados: <procesados>
#   Empleados rechazados: <rechazados>
#   Total neto a depositar: $<total_neto>

# Salida esperada:
# Empleado 1 | Bruto: $22000 | Neto: $19360.0
# Empleado 2 | Bruto: $25000 | Neto: $22000.0
# Empleado 3 | RECHAZADO: salario fuera de rango (500)
# Empleados procesados: 2
# Empleados rechazados: 1
# Total neto a depositar: $41360.0