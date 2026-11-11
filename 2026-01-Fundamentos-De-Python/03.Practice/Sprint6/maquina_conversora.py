def a_farenheit(grados_celsius):
    resultado = (grados_celsius * 9/5) + 32
    return resultado

clima = a_farenheit(30)
print(f"30 grados Celsius son {clima} grados fahrenheit")
print(f"0 grados Celsius son {a_farenheit(0)} grados fahrenheit\n")

def a_celsius(grados_fahrenheit):
    resultado = (grados_fahrenheit - 32) * 5/9
    return resultado

clima2 = a_celsius(100)
print(f"100 grados fahrenheit son {clima2} grados celsius")