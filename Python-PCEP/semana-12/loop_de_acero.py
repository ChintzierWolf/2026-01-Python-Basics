while True:
    try:
        monto = float(input("Ingrese el monto: "))
        resultado = 1 / monto
    except ZeroDivisionError:
        print("Error: El monto no puede ser cero")
    except ValueError:
        print("Error: El monto debe ser un número")
print(resultado)
print(type(resultado))