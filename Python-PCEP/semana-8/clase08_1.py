def duplica(numero):
    valor_intermedio = numero + numero
    return valor_intermedio

edad = duplica(24)
print(edad)

# Lambda es una funcion anonima que no tiene nombre
# lambda argumentos: expresion

duplica = lambda numero: numero + numero
edad = duplica(24)
print(edad)

# Ejemplos con lambda como argumento de sorted()

lista = [1, 2, 3, 4, 5]
lista_ordenada = sorted(lista, key=lambda x: -x)
print(lista_ordenada)

lista1 = [(1, 2), (3, 4), (5, 6)]
lista1_ordenada = sorted(lista1, key=lambda x: x[1])
print(lista1_ordenada)

# lambda es util cuando se necesita una funcion simple por poco tiempo
# y no se quiere definir una funcion con def.

# En cambio def se usa para funciones mas complejas o que se reutilizan en el codigo.
# En este ejemplo con lambda es mas limpio y conciso que con def.

