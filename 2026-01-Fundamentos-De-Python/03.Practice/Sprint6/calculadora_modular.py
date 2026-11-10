# Calculadora Modular con Funciones

print("=== CALCULADORA MODULAR ===\n")

# TODO 1: Define cuatro funciones, cada una con dos parámetros (a, b)
# y su respectivo return:
#   - sumar(a, b)       → devuelve a + b
#   - restar(a, b)      → devuelve a - b
#   - multiplicar(a, b) → devuelve a * b
#   - dividir(a, b)     → devuelve a / b

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

# TODO 2: Protege la función dividir: si b es 0, devuelve el string
# "Error: división por cero" ANTES de intentar la división.

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    else:
        return a / b

# TODO 3: Crea dos variables num1 = 20 y num2 = 5, y usa f-strings para
# imprimir el resultado de las cuatro operaciones llamando a tus funciones.
# Ejemplo de salida:
# "Suma: 20 + 5 = 25"
num1 = 20
num2 = 5
print(f"Suma: {num1} + {num2} = {sumar(num1, num2)}")
print(f"Resta: {num1} - {num2} = {restar(num1, num2)}")
print(f"Multiplicacion: {num1} * {num2} = {multiplicar(num1, num2)}")
print(f"Division: {num1} / {num2} = {dividir(num1, num2)}")

# TODO 4: Comprueba tu guardia llamando dividir(10, 0) e imprime el resultado.
print(f"10 / 0 = {dividir(10, 0)}")

# TODO 5: Demuestra que las funciones son reutilizables: llama sumar(100, 250)
# y restar(1000, 750) e imprime ambos resultados.

print(f"Suma: 100 + 250 = {sumar(100, 250)}")
print(f"Resta: 1000 - 750 = {restar(1000, 750)}")