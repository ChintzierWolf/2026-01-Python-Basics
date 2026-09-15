nombre = input('¿Cuál es tu nombre?: ')
año_nacimiento = int(input('¿Cuál es tu año de nacimiento?: '))
sueldo = float(input('¿Cuál es tu salario deseado?: '))

año_actual = 2026
edad = año_actual - año_nacimiento

print("\n\n######## GAFETE VIRTUAL ########\n")
print(f"         Nombre: {nombre}")
print(f"        Edad: {edad} años")
print(f"Salario deseado: ${sueldo:.2f} MXN mensuales\n")
print(f"     Edad en 10 años: {edad + 10} años")
print("\n######## FIN DEL PROGRAMA ########\n\n")