"""
try:
    patrimonio = float(input("Ingrese el patrimonio de la empresa: "))
    pasivos = float(input("Ingrese los pasivos de la empresa: "))

    razon = pasivos / patrimonio

    print("La razón de endeudamiento es: ", round(razon, 2)) # ZeroDivisionError

except ValueError:
    print("[ERROR]: Eso no es un número. Usa solo digitos. Ej: 12000000. Revisa de nuevo.")
except ZeroDivisionError:
    print("[ERROR]: El patrimonio no puede ser cero. Vuelve a revisar el dato.")
except Exception:
    print("[ERROR]: Ocurrió un error inesperado deconocido.")
else:
    print("[OK]: Razon de endeudamiento: ", round(razon, 2), "[SUCCESS]. Calculada exitosamente.")
finally:
    print("[INFO]: Bitacora de calculo registrada.")
"""

# Se debe de realizar el crash voluntario del programa para que se ejecute el type error de manera forzada y se pueda ver el mensaje de error.

"""
try:
    patrimonio = float(input("Ingrese el patrimonio de la empresa: "))
    pasivos = input("Ingrese los pasivos de la empresa: ")

    razon = pasivos / patrimonio

    print("La razón de endeudamiento es: ", round(razon, 2)) # ZeroDivisionError

except ValueError:
    print("[ERROR]: Eso no es un número. Usa solo digitos. Ej: 12000000. Revisa de nuevo.")
except ZeroDivisionError:
    print("[ERROR]: El patrimonio no puede ser cero. Vuelve a revisar el dato.")
except Exception:
    print("[ERROR]: Ocurrió un error inesperado deconocido.")
else:
    print("[OK]: Razon de endeudamiento: ", round(razon, 2), "[SUCCESS]. Calculada exitosamente.")
finally:
    print("[INFO]: Bitacora de calculo registrada.")
"""

# Ahora se realizará la mejora del programa donde el loop se mantendrá activo hasta que el usuario ingrese datos válidos
# Se debe de eliminar el finally, pues no es necesario en este caso. 
# Se debe de agregar un else para que se muestre el mensaje de "Exito" solo si no hay errores.
#

while True:
    try:
        patrimonio = float(input("Ingrese el patrimonio de la empresa: "))
        pasivos = float(input("Ingrese los pasivos de la empresa: "))

        razon = pasivos / patrimonio

        print("La razón de endeudamiento es: ", round(razon, 2)) # ZeroDivisionError

    except ValueError:
        print("[ERROR]: Eso no es un número. Usa solo digitos. Ej: 12000000. Revisa de nuevo.")
    except ZeroDivisionError:
        print("[ERROR]: El patrimonio no puede ser cero. Vuelve a revisar el dato.")
    except Exception:
        print("[ERROR]: Ocurrió un error inesperado deconocido.")
    else:
        print("[OK]: Razon de endeudamiento: ", round(razon, 2), "[SUCCESS]. Calculada exitosamente.")
        break

print("Patrimonio aceptado: ", patrimonio, " Pasivos aceptados: ", pasivos)

# Si por alguna razón se le entraga a la captura de datos el valor de 0,0 el programa debe mostrar el error de ZeroDivisionError
# y el programa debe continuar hasta que se ingrese un valor válido. 0,0 no es válido, ya que los números deben de ser escritos 
# con punto decimal, no coma. Al escribirlos con coma, el progrma lo interpreta como un string y lanza un ValueError.