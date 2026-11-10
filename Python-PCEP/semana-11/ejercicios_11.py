tasa_impuesto = 0.10

def recalcular_tasa():
    tasa_impuesto = 0.12
    return tasa_impuesto

recalcular_tasa()
print(f"Tasa vigente del sistema: {tasa_impuesto:.2f}")


"""
Nómina necesita calcular el pago bruto de cualquier empleado:

    pago_bruto = sueldo_base + bono

Hoy hay 4 empleados con sueldos y bonos distintos. Mañana habrá 40
No queremos escribir la suma 40 veces. Queremos una máquina que;
dándole el sueldo y bono, devuelva el bruto
"""

def calcular_pago_bruto(sueldo_base, bono):
    bruto = sueldo_base + bono
    return bruto 

pago = calcular_pago_bruto(20000, 200)
print(f"Pago bruto: ${pago:.2f}")

"""
mini drill 1
Usa la misma función calcular_pago_bruto (no la modifiques)  para calcular el bruto de estos 4 empleados e imprime una línea para cada uno.

emp 101: sueldo 18000, bono 1500
emp 102: sueldo 25000, bono 0
emp 103: sueldo 30000, bono 5000
emp 104: sueldo 12000, bono 800

salida esperada (formato libre, pero deben de verde estos números):
19500, 25000, 35000, 12800
"""

empleados = [
    {"emp": 101, "sueldo": 18000, "bono": 1500},
    {"emp": 102, "sueldo": 25000, "bono": 0},
    {"emp": 103, "sueldo": 30000, "bono": 5000},
    {"emp": 104, "sueldo": 12000, "bono": 800}
]

for persona in empleados:
    bruto = calcular_pago_bruto(persona["sueldo"], persona["bono"])
    print(f"Empleado: {persona["emp"]}")


"""
mini drill 2
Un compañero llamó así s la función:
    pago = calcular_pago_bruto(2000,18000)
y juraba que el empleado 
"""

"""
mini drill 3
Crea una segunda función;

calcular_impuesto(monto, tasa)

que devuelva monto * tasa

Luego, para el emp 103 (bruto 35000) con tass de 0.12, imprime;
    "Impuesto a retener: $4200.0"
usando las dos funciones (primero el bruto, luego el umpirs6sobre ese bruto)
"""

def calcular_impuesto(monto, tasa):
    impuesto = monto * tasa
    return impuesto

bruto = calcular_pago_bruto(30000, 5000)
print(f"Impuesto al sueldo bruto: {bruto}: {calcula,_impuesto(bruto, 0.12)}")

print(calcular_impuesto(calcular_pago_bruto(30000, 5000), 0.12))

"""
def calcular_neto(bruto, tasa):
    return bruto
    impuesto = bruto * tasa
    return bruto - impuesto

print(calcular_neto(35000, 0.12))
"""

