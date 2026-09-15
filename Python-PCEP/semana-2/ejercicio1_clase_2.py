# Se debe de elaborar un ejercicio donde deba de ingresar el dato del nombre de la persona, la edad 
# y el resultado de un sueldo con el aumento del 10% del total con 2 decimales totales.

nombre = input("Ingresa el nombre de la persona: ")
edad = int(input("Ingresa la edad de la persona: \n"))
sueldo = float(input("Ingresa el sueldo de la persona: \n"))

aumento_sueldo = sueldo * 0.1
sueldo_con_aumento = sueldo + aumento_sueldo

print("\n")
print("-------------- Gafete Virtual 1 ---------------")
# .title() es una funcion que convierte la primera letra de cada palabra en mayuscula
print(f"Nombre: {nombre.title()}")
# .2f es una funcion que convierte un flotante a un formato con 2 decimales
print(f"Edad: {edad}")
print(f"Sueldo: {sueldo:.2f}")
print(f"Aumento: {aumento_sueldo:.2f}")
print(f"Sueldo con aumento: {sueldo_con_aumento:.2f}")
print("---------------------------------------------")

print("\n")
print("--------------- Gafete Virtual 2 ------------------")
# En el gafete virtual 2, se muestra el uso de la funcion .title()
# Ademas muestra el uso de la funcion de asignacion (=)
# finalmente muestra el uso de la funcion de formateo (f)
print(f"{nombre=}\n{edad=}\n{sueldo=}\n{aumento_sueldo=}\n{sueldo_con_aumento=}")

print("\n")
print("--------------- Gafete Virtual 3 ------------------")
# En el gafete virtual 3, se muestra el uso de la funcion .title()
# Ademas muestra el uso de la funcion de asignacion (=)
# finalmente muestra el uso de la funcion de formateo (f)
print(f"{nombre.title()}\n{edad=}\n{sueldo=:.2f}\n{aumento_sueldo=:.2f}\n{sueldo_con_aumento=:.2f}")