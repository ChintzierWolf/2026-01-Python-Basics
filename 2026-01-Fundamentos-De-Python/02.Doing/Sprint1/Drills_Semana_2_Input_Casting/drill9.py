# DRILL 4: EL CONVERSOR DE VALENTINA

# TODO 1: Usa input() con float() para pedir la temperatura en Celsius
# y guárdala en una variable llamada 'celsius'.

# TODO 2: Aplica la fórmula de conversión: (celsius * 9/5) + 32
# y guarda el resultado en una variable llamada 'fahrenheit'.

# TODO 3: Usa una f-string para mostrar el resultado.
# Ejemplo de salida:
# "[celsius]°C equivale a [fahrenheit]°F"

celsius = float(input("Introduce la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")

