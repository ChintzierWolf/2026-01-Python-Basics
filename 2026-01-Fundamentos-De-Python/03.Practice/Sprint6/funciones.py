"""
def calcular_pago_bruto(sueldo_base, bono):
    total = sueldo_base + bono
    print("Pago Bruto: ", total)

pago = calcular_pago_bruto(50000, 2000) # Sin return pago es None y da error al imprimir fuera de la funcion
print("El pago a recibir es: ", pago)
"""
# ============================================================================ #
"""
#Retornar un valor
def calcular_pago_bruto(sueldo_base, bono):
    total = sueldo_base + bono
    print("Pago Bruto: ", total)
    return total

# Manera simple de imprimir el retorno
pago = calcular_pago_bruto(50000, 2000)
print("El pago 1 a recibir es: ", pago)

# Manera guardando la variable y luego imprimiendola
pago2 = calcular_pago_bruto(100000, 2000)
print("El pago 2 a recibir es: ", pago2)

# Manera de imprimir el retorno sin guardar la variable
print("El pago 3 a recibir es: ", calcular_pago_bruto(150000, 3000))

"""
# ============================================================================ #
"""
#Retornar  valores
def calcular_pago_bruto(sueldo_base, bono):
    total = sueldo_base + bono
    print("Pago Bruto: ", total)
    return total

# Retornar multiples valores
def calcular_pago_neto(bruto, tasa):
    impuesto = bruto * tasa
    return bruto - impuesto


pago = calcular_pago_bruto(50000, 2000)
bruto = calcular_pago_bruto(50000, 0.12)

print(f"El pago bruto a recibir es: {pago}")
print(f"El pago neto a recibir es: {bruto}")
print(f"El pago con impuestos a recibir es: {calcular_pago_neto(pago, 0.12)}")
"""
# ============================================================================ #
