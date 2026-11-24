# Snippet A - calculadora de razón de endeudamiento

def calcular_razon_endeudamiento(positivos, patrimonios):
    try:
        razon = positivos / patrimonios
        return razon
        #print(f"La razón de endeudamiento es: {razon}")
    except ValueError:
        return "Valor no válido"
    finally:
        print("Cálculo intentado")  

#Probando cada uno de los casos

print(calcular_razon_endeudamiento(5000, 0))
#print(calcular_razon_endeudamiento(5000, 500))
#print(calcular_razon_endeudamiento(1000, "a"))

# Corrección del código
# Se agrega el manejo de la excepción ZeroDivisionError
# Ya que si la variable patrimonios es cero, se lanza una excepción que no 
# se está manejando en el código original y genera un error fatal para el programa

# Al igual que se agrega el manejo de la excepción TypeError
# Ya que si la variable patrimonios es de un tipo de dato que no se puede dividir

def calcular_razon_endeudamiento(positivos, patrimonios):
    try:
        razon = positivos / patrimonios
        return razon
    except ValueError:
        return "Valor no válido"
    except ZeroDivisionError:
        return "El patrimonio no puede ser cero"
    except TypeError:
        return "Los valores deben ser numéricos"
    finally:
        print("Cálculo intentado")

print(calcular_razon_endeudamiento(5000, 0))