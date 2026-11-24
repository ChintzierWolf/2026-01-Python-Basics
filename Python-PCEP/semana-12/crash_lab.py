# trash_lab.py - Laboratorio de fallas

pasivos = 80000
patrimonio = 0

#try:
#    razon = pasivos / patrimonio
#    print("La razón de endeudamiento es: ", razon) # ZeroDivisionError
#except ZeroDivisionError:
#    print("[ERROR]: El patrimonio no puede ser cero. Vuelve a revisar el dato.")
#except TypeError:
#    print("[ERROR]: El patrimonio debe ser numérico.")
#finally:
#    print("Fin del programa", razon)


try:
    patrimonio = float(input("Ingrese el patrimonio de la empresa: "))
    pasivos = float(input("Ingrese los pasivos de la empresa: "))

    razon = pasivos / patrimonio
    print("La razón de endeudamiento es: ", razon) # ZeroDivisionError
except ZeroDivisionError:
    print("[ERROR]: El patrimonio no puede ser cero. Vuelve a revisar el dato.")
except ValueError:
    print("[ERROR]: Ambos valores del cálculo deben ser numéricos.")
except TypeError:
    print("[ERROR]: Ambos valores del cálculo deben ser del mismo tipo.")
finally:
    print("Fin del programa.")