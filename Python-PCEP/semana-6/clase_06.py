#for i in range(1, 6):
#    if i == 3:
#        break
#    print(i)

# El programa imprime los números del 1 al 2. Porque la instrucción 'break' detiene el bucle cuando la variable 'i' es igual a 3.

#for i in range(1, 6):
#    if i == 3:
#        continue
#    print(i)

# El programa imprime los números del 1 al 5, excepto el 3. Porque la instrucción 'continue' salta la iteración actual cuando la variable 'i' es igual a 3.

#for i in range(1, 6):
#    if i == 1:
#        break
#    print(i)

# El programa imprime solo el número 1, porque la instrucción 'break' detiene el bucle cuando la variable 'i' es igual a 1.

while True:
    op = input('Introduce tu opción: ')
    if op == 'a':
        continue
        print("Después de continue")
    elif op == 'A':
        break
    print("Después de if/elif")
print("Fuera del bucle")

# ¿Qué imprime el programa?

# Imprime lo siguiente:
# Introduce tu opción: a
# Después de if/elif
# Introduce tu opción: b
# Introduce tu opción: A
# Fuera del bucle
