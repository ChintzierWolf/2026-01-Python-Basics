# DRILL 3: ATRAPANDO MÚLTIPLES AMENAZAS

# TODO 1: Abre un bloque try.
# Dentro:
#   - Pide al usuario el número de cables disponibles (int).
#   - Pide al usuario el número de escenarios (int).
#   - Calcula y muestra cuántos cables le tocan a cada escenario
#     (cables / escenarios).

try:
    cables = int(input("Cables disponibles: "))
    escenarios = int(input("Escenarios: "))
    print(f"Cables por escenario: {cables / escenarios}")


    
# TODO 2: Agrega un except ValueError con un mensaje específico
# para problemas de tipo de dato:
# "Error: uno de los valores no es un número entero."

except ValueError:
    print("Error: uno de los valores no es un número entero.")

# TODO 3: Agrega un except ZeroDivisionError con un mensaje específico
# para división entre cero:
# "Error: no hay escenarios registrados todavía."

except ZeroDivisionError:
    print("Error: no hay escenarios registrados todavía.")

# TODO 4: Prueba el programa tres veces:
# Caso 1: cables=12, escenarios=3 → debe funcionar
# Caso 2: cables=hola, escenarios=3 → debe disparar el ValueError
# Caso 3: cables=12, escenarios=0 → debe disparar el ZeroDivisionError
