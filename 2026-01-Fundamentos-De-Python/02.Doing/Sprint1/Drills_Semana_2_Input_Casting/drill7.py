# DRILL 2: EL DETECTOR DE TIPOS DE LUCÍA

# TODO 1: Usa input() para pedir el nombre del medio de comunicación.
# Guárdalo en una variable llamada 'nombre_medio'.
# Usa print(type(nombre_medio)) para mostrar su tipo de dato.

# TODO 2: Usa input() para pedir el número de credencial de prensa.
# Guárdalo en una variable llamada 'num_credencial'.
# Usa print(type(num_credencial)) para mostrar su tipo de dato.

# TODO 3: Imprime un mensaje que confirme lo que Lucía sospechaba:
# que ambos datos llegaron como texto aunque uno parezca un número.
# Usa una f-string para el mensaje.

nombre_medio = input("Ingrese el nombre del medio de comunicación: ") # Variable de tipo str
num_credencial = input("Ingrese el número de credencial de prensa: ") # Variable de tipo str

print(f"El nombre del medio es {nombre_medio} y es de tipo {type(nombre_medio)}")
print(f"El número de credencial es {num_credencial} y es de tipo {type(num_credencial)}")
print(f"Ambos datos llegaron como texto, aunque uno parezca un número.")

# ¿Qué fue difícil de programar?

# Fue fácil de programar. Solo tuve que usar input() para pedir el nombre del medio de comunicación 
# y el número de credencial de prensa. Luego, usé print(type()) para mostrar su tipo de dato. 
# Finalmente, usé una f-string para imprimir un mensaje que confirmara lo que Lucía sospechaba.

