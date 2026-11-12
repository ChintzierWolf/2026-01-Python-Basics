"""
#Variables Locales vs. Variables Globales
def procesar():
    bono_local = 50000
    print("Adentro veo el bono local: ", bono_local)
    return bono_local

bono = procesar()
print("Afuera veo el bono global: ", bono)
"""

tasa_impuesto = 0.10

def usar_tasa_promo():
    tasa_impuesto = 0.05
    return tasa_impuesto

promo_1 = usar_tasa_promo()
print("Usamos la tasa promo: ", promo_1)
print("La tasa global sigue siendo: ", tasa_impuesto)

# Validación que devuelve resultado pero no opina

def es_salario_valido(salario):
    return 8000 <= salario <= 200000

salario = 12000

if es_salario_valido(salario):
    print("El salario es válido: ", salario)
else:
    print("El salario no es válido: ", salario)

print("Usamos el salario: ", es_salario_valido, 5000)
print("Usamos el salario: ", es_salario_valido, 50000)

# Modificar una variable global

velocidad_max = 120

def ajustar_velocidad_max():
    velocidad_max = 150
    print("Dentro cambio la velocidad: ", velocidad_max)
    return velocidad_max

ajuste_1 = ajustar_velocidad_max()
print("Usamos velocidad: ", ajuste_1)
print("La velocidad sigue siendo: ", velocidad_max)

# Modificar una variable global sin crear una local

velocidad_max = 120

def ajustar_velocidad_max():
    global velocidad_max
    velocidad_max = 150
    print("Dentro cambio la velocidad: ", velocidad_max)
    return velocidad_max

ajuste_1 = ajustar_velocidad_max()
print("Usamos velocidad: ", ajuste_1)
print("La velocidad sigue siendo: ", velocidad_max)
