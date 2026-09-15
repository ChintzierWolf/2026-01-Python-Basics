edad = int(input("Ingresa tu edad: "))
sueldo = float(input("Ingresa tu sueldo: "))
nombre = input("Ingresa tu nombre: ")

resumen = f"""Mediante ésta carta, confirmamos que el Sr. {nombre.title()} de {edad} años, 
tiene un sueldo de {sueldo:.2f} y un aumento de {sueldo * 0.1:.2f} 
su sueldo con aumento es de {sueldo * 1.1:.2f} pesos"""

resumen2 = "Mediante ésta carta, confirmamos que el Sr. " + nombre.title() + " de " + str(edad) + " años, " + \
"tiene un sueldo de " + str(sueldo) + " y un aumento de " + str(sueldo * 0.1) + " " + \
"su sueldo con aumento es de " + str(sueldo * 1.1) + " pesos"

print(resumen)
print(resumen2)