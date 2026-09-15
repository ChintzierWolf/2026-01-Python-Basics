# f-string
# el f-string dentro de python sirve para formatear strings
# el f-string nos permite crear strings con variables dentro de ellos
# la sintaxis es la siguiente: f"texto {variable}"
# donde f es el f-string, "texto" es el texto que queremos imprimir y {variable} es la variable que queremos imprimir

# Revisar el uso del f-string
# https://www.youtube.com/watch?v=8Z3nKx-o_vE

name = "Juan"
age = 25
height = 1.75

#formas distintas de formatear strings

print(f"Name: {name}\n")
print(f"Age: {age}\n")
print(f"Height: {height}\n")

# f-string con saltos de línea
print(f"Name: {name}\nAge: {age}\nHeight: {height}\n")

# f-string sin saltos de línea
print(f"Name: {name} Age: {age} Height: {height}\n")

# Usando .format(), que sirve para lo mismo que el f-string pero con una sintaxis distinta
# esta es una forma mas antigua de formatear strings, pero aun es valida
print("Nombre: {}\nEdad: {}\nAltura: {}\n".format(name, age, height))