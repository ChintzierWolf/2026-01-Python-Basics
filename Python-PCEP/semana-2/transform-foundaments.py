# Los 3 principales operadores de transformation o transformaciones de datos 
# son: str(), int(), float()

# str() convierte un valor en un string
# int() convierte un valor en un entero
# float() convierte un valor en un flotante

print(str(123))
print(int("123"))
print(float("123"))

# Un ejemplo de cuando usar estas transformaciones

age = "25"
print(type(age))

age = int(age)
print(type(age))

age = str(age)
print(type(age))

# El siguiente ejemplo muestra el uso de los 3 operadores de transformation

name = input("What is your name? ")
age = input("What is your age? ")
height = input("What is your height? ")

print("Name: " + name + "\n" + "Age: " + age + "\n" + "Height: " + height + "\n")

# Con este comando podemos ver la informacion sobre una variable
print(type(name))
print(type(age))
print(type(height)) 

# Otro ejemplo del uso de los operadores de transformation

print("Name: " + name + "\n" + "Age: " + str(age) + "\n" + "Height: " + str(height) + "\n")

# Otro ejemplo del uso de los operadores de transformation

print("Name: " + name + "\n" + "Age: " + str(age) + "\n" + "Height: " + str(height) + "\n")