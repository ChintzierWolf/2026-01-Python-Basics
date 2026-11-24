"""
CONTEXTO: Eres analista en el área de riesgo de un banco. Construyes el
motor que calcula indicadores financieros de las empresas solicitantes.
El motor lo van a usar capturistas que cometen errores de tecleo todo el
día. Tu motor NO se puede caer NUNCA.

REQUISITOS FUNCIONALES:
  
Menú con while True y al menos 3 opciones:
    1) Razón de endeudamiento               (pasivos / patrimonio)
    2) Margen sobre nómina                  (utilidad_operativa / costo_nomina)
    3) Salir

Cada operación de cálculo vive en su PROPIA función (ya saben hacerlo).
Todos los inputs numéricos usan el "loop de acero":
no se avanza hasta recibir un número válido (atrapa ValueError).
Toda división está blindada contra denominador 0 (atrapa ZeroDivisionError).

La estructura usa try / except / else / finally:
except ValueError  -> mensaje específico
except ZeroDivisionError -> mensaje específico
else  -> imprime el resultado redondeado a 2 decimales
finally -> registra el intento (en consola o en bitácora .txt)

import os: al iniciar, muestra os.getcwd() y verifica si el archivo
 de bitácora ya existe con os.path.exists().
La opción "Salir" usa break y termina el programa limpiamente.

DATOS DE PRUEBA OFICIALES (para verificar tu Salida Mínima):
  
Razón de endeudamiento con pasivos=80000, patrimonio=40000  -> 2.0
Margen sobre nómina con utilidad=150000, costo_nomina=50000  -> 3.0
Cualquier input de texto ("hola") -> vuelve a pedir, NO se cae
Patrimonio=0 -> mensaje de error claro, NO se cae
"""

import os


def calcular_razon_endeudamiento(pasivos, patrimonio):
    return pasivos / patrimonio


def calcular_margen_nomina(utilidad, nomina):
    return utilidad / nomina


print(f"Directorio actual: {os.getcwd()}")
if os.path.exists("bitacora.txt"):
    print("El archivo de bitácora ya existe.\n")
else:
    print("El archivo de bitácora no existe.\n")

while True:
    print("\n1) Razón de endeudamiento")
    print("2) Margen sobre nómina")
    print("3) Salir")
    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        print("\nRazón de endeudamiento")
        print("=" * 30)
        while True:
            try:
                pasivos = float(input("Ingresa los pasivos: "))
                patrimonio = float(input("Ingresa el patrimonio: "))
                resultado = calcular_razon_endeudamiento(pasivos, patrimonio)
            except ValueError:
                print("Error: Ingresa solo números")
            except ZeroDivisionError:
                print("Error: El patrimonio no puede ser cero")
            else:
                print(f"El resultado es: {resultado:.2f}")
                break
            finally:
                print("Fin del cálculo")

    elif opcion == "2":
        print("\nMargen sobre nómina")
        print("=" * 30)
        while True:
            try:
                utilidad = float(input("Ingresa la utilidad: "))
                costo_nomina = float(input("Ingresa el costo de nómina: "))
                resultado = calcular_margen_nomina(utilidad, costo_nomina)
            except ValueError:
                print("Error: Ingresa solo números")
            except ZeroDivisionError:
                print("Error: El costo de nómina no puede ser cero")
            else:
                print(f"El resultado es: {resultado:.2f}")
                break
            finally:
                print("Fin del cálculo")

    elif opcion == "3":
        print("\nSaliendo del programa...")
        break
    else:
        print("\nError: Opción inválida")
