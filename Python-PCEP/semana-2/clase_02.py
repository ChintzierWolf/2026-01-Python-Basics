# Este ejemplo muestra la concatenacion de strings
print("2" + "2")
# El resultado deverá ser 22

# Este ejemplo muestra la suma de enteros
print(2 + 2)
# El resultado deverá ser 4


# Este ejemplo muestra la suma de un entero y un string, lo cual da error
print(2 + "2")
# El resultado deverá ser un error

# Otro ejemplo de la suma de enteros
print(2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2)
# El resultado deverá ser 20


# Otro ejemplo de la concatenacion de strings
print("ha" * 3)
# El resultado deverá ser "hahaha"

#------------------------------------------------------------------------------------------------#

edad = input("What is your age? ")
print(f"Your age is {edad} years old")
# El resultado deverá ser la edad del usuario ingresada en un formato de string 

# -----------------------------------------------------------------------------------------------#

age = input("What is your age? ")
age = int(age)
age = age + 10
print(f"Your age is {age} years old")
# El resultado deverá ser la edad del usuario ingresada en un formato de entero y se le suman 10 años 

# -----------------------------------------------------------------------------------------------#

edad = input("Ingresa tu edad: ")
print(type(edad))

edad = int(edad)
print(type(edad))

edad = edad + 10
print(type(edad))

print(f"Tu edad es {edad} años")
# El resultado deverá ser la edad del usuario ingresada en un formato de entero y se le suman 10 años

# -----------------------------------------------------------------------------------------------#

# Una manera de reducir el ejercicio anterior a dos líneas podría ser ingresar los datos de la siguiente manera

edad = int(input("Ingresa tu edad: ")) + 10
print(f"Tu edad es {edad} años")
# El resultado deverá ser la edad del usuario ingresada en un formato de entero y se le suman 10 años

# también se puede hacer de la siguiente manera

edad = int(input("Ingresa tu edad: "))
print(f"Tu edad es {edad + 10} años")

#-----------------------------------------------------------------------------------------------#

# Ahora se utilizará ña variable float

precio = float(input("Ingresa el precio: "))
precio_con_descuento = precio * 0.9
print(f"El precio con descuento es: {precio_con_descuento}")
# El resultado deverá ser el precio del producto ingresado en un formato de flotante y se le aplica un descuento del 10%

# -----------------------------------------------------------------------------------------------#

# Utilizando una sola línea

precio = float(input("Ingresa el precio: "))
print(f"El precio con descuento es: {precio * 0.9}")
# El resultado deverá ser el precio del producto ingresado en un formato de flotante y se le aplica un descuento del 10%

#-----------------------------------------------------------------------------------------------#
