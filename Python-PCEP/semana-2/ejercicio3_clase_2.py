# Se debe de crear un programa que pueda elaborar el cálculo y conversión de temperaturas, 
# Se deberá de poder ingresar el valor de una ciudad y la temperatura que tiene en grados centígrados.
#Posteriormente, se debe de convertir la temperatura a grados fahrenheit y kelvin y realizar un reporte del clima
#Ejemplo del reporte
"""En la ciudad de 
    Tijuana la temperatura actual es de 
    17.5 grados centigrados y 
    18.5 grados fahrenheit
    290.65 grados kelvin

    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
"""


ciudad = input("Ingresa el nombre de la ciudad: ")
temperatura_celsius = float(input("Ingresa la temperatura en grados centígrados: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
temperatura_kelvin = temperatura_celsius + 273.15

print(f"""Reporte del clima en la ciudad de: 

{ciudad} 

La temperatura actual es de:

-Grados Celsius: {temperatura_celsius:.2f}
-Grados Fahrenheit: {temperatura_fahrenheit:.2f}
-Grados Kelvin: {temperatura_kelvin:.2f}
""")