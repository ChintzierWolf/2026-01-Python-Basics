print ("Inicio")

if True:
    print ("Paso 1")
    if False:
        print ("Paso 2")
    else:
        print ("Paso 3")
print ("Fin")

# En este caso el error del código es que no se está validando si el nivel es mayor a 0 y menor a 3.
# Por lo tanto, el código siempre se va a ejecutar en la primera condición que se cumple.