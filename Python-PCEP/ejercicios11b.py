"""
Contexto

Nómina tiene una regla: un salario es Válido si este entre 8000 y 200000
(inclusive ambos). Cualquier cosa fuers de ese rango es sospecha (error de captura o fraude) y NO debe procesarse

Necesitamos una función que, dado un salario, responda Si o No
"""

def es_salario_
"""
recordar para que es el doc string dentro de una función 
"""

tasa_impuesto = 0.10

def usar_tasa_promo():
    tasa_impuesto = 0.05
    return tasa_impuesto

print(f"Tasa impuesto: {tasa_impuesto}")
print(f"Tasa Promo: {usar_tasa_promo}")


"""
mini drill 7

salida esperada:
PROCESAR: 20000
RECHAZAR: 500
PROCESAR: 200000
RECHAZAR: 250000
"""

lista_salarios = [20000, 500, 200000, 250000]

for salario in lista_salarios:
    es_valido = es_salario_valido(salario)

    if es_valido:
        print(f"PROCESAR: {salario}")

    else:
        print(f"RECHAZAR: {salario}")