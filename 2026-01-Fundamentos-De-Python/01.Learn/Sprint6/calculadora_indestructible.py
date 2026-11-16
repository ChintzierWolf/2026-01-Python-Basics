# Calculadora Indestructible con Try/Except

print("\n=== CALCULADORA INDESTRUCTIBLE ===\n")

# TODO 1: Define dividir_seguro(a, b): dentro de un try, calcula a / b y
# devuélvelo con return. Captura DOS excepciones específicas:
#   - ZeroDivisionError → devuelve "Error: No puedo dividir entre cero"
#   - TypeError         → devuelve "Error: Los valores deben ser números"

def dividir_seguro(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No puedo dividir entre cero"
    except TypeError:
        return "Error: Los valores deben ser números"

# TODO 2: Define obtener_numero(mensaje): usa un while True que dentro de un
# try convierta input(mensaje) con float() y lo devuelva con return.
# Si el usuario escribe algo inválido (ValueError), imprime
# "❌ Eso no es un número. Intenta de nuevo." y vuelve a pedir.

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Eso no es un número. Intenta de nuevo.")

# TODO 3: Pide dos números con obtener_numero() y guárdalos en num1 y num2.
# (Prueba escribir letras: el programa NO debe romperse.)

num1 = obtener_numero("Ingresa el primer número: ")
num2 = obtener_numero("Ingresa el segundo número: ")

# TODO 4: Imprime con f-strings la suma, resta, multiplicación y división
# de num1 y num2. Para la división usa dividir_seguro().

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {dividir_seguro(num1, num2)}")

# TODO 5: Pruebas de robustez — imprime el resultado de:
#   - dividir_seguro(10, 0)
#   - dividir_seguro('hola', 5)
# Al final imprime "✅ El programa terminó sin romperse".

print(f"\nDivisión con 0: {dividir_seguro(10, 0)}")
print(f"División con letras: {dividir_seguro('hola', 5)}")
print("\n✅ El programa terminó sin romperse")