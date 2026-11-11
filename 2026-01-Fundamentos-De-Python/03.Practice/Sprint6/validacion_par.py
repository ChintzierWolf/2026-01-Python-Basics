def es_par(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("Ingrese un número: "))
print(f"El número {numero} es {es_par(numero)}")