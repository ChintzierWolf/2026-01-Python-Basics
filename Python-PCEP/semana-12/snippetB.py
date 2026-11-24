# Snippet B - ¿Qué devuelve la función?

#def procesar_nomina(salario):
#    try:
#        return float(salario)
#    except ValueError:
#        return -1
# print(procesar_nomina("treinta"))

# ¿Qué errores genera la siguiente función?

#edad = int("treinta")          # ValueError
#total = 100/0                  # ZeroDivisionError
#mensaje = "salario" + 5000     # TypeError

# primer intento de correcciones respectivas

"""
try:
    edad = int("treinta")
    total = 100/0
    mensaje = "salario" + 5000
except ValueError:
    print("Value error detectado. ")
except ZeroDivisionError:
    print("Se intentó dividir entre 0")
except TypeError:
    print("Existe un error de tipos")
"""

# Se debe de realizar por bloques para evitar que el programa se detenga
# cuando ocurre un error. De esta manera se puede manejar cada error de forma
# independiente.

try:
    edad = int("treinta")
except ValueError:
    print("Value error detectado. ")
except ZeroDivisionError:
    print("Se intentó dividir entre 0")
except TypeError:
    print("Existe un error de tipos")

try:
    total = 100/0
except ValueError:
    print("Value error detectado. ")
except ZeroDivisionError:
    print("Se intentó dividir entre 0")
except TypeError:
    print("Existe un error de tipos")

try:
    mensaje = "salario" + 5000
except ValueError:
    print("Value error detectado. ")
except ZeroDivisionError:
    print("Se intentó dividir entre 0")
except TypeError:
    print("Existe un error de tipos")