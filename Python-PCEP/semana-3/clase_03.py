#------------------------------------------------------------ #
#Operadores de asignación

a = 2
a == 2

print(a)
# Al asignar el valor 2 a la variable a, se convierte en un entero. 

print(a == 2)
# Al usar el operador == para comparar a con 2, se está comparando el valor de la variable con el número 2. Como son iguales, la expresión es verdadera.

#------------------------------------------------------------ #
#Sistema de validación de acceso

nivel_requerido = 3
print(nivel_requerido == 5)
# El resultado de la expresión nivel_requerido == 5 es False, ya que el valor de nivel_requerido es 3 y no 5.
#Para que la expresión fuera verdadera, el valor de nivel_requerido debería ser 5.

#------------------------------------------------------------ #

nivel_requerido = 3
print(nivel_requerido == 5)
# El resultado de la expresión nivel_requerido == 5 es False, ya que el valor de nivel_requerido es 3 y no 5.

print(nivel_requerido == 3)
# El resultado de la expresión nivel_requerido == 3 es True, ya que el valor de nivel_requerido es 3.

if nivel_requerido == 3:
    print("Nivel requerido es igual a 3")


# La terminación de archivo .ipynb indica que es un archivo de Jupyter Notebook.
# Es un entorno de desarrollo interactivo que permite ejecutar código en celdas. 
# Para ejecutar código en una celda de Jupyter Notebook, se puede presionar Ctrl + Enter.
# Los archivos .py son archivos de Python que se pueden ejecutar desde la línea de comandos. 
# Para ejecutar un archivo .py desde la línea de comandos, se puede presionar Ctrl + Enter.

# Las ventajas de utilizar .py sobre .ipynb son:
# Los archivos .py son más livianos y rápidos de cargar que los archivos .ipynb. 
# Los archivos .py son más fáciles de compartir y colaborar con otros.
# Los archivos .py son más fáciles de depurar y mantener. 
# Los archivos .py son más fáciles de automatizar y ejecutar en entornos de producción. 

# Python utiliza un sistema de tipos dinámico y fuerte.
# Dinámico: 
#  - No es necesario declarar el tipo de variable
#  - El tipo de variable se infiere en tiempo de ejecución
# Fuerte: 
#  - No se pueden mezclar tipos de variables
#  - No se pueden realizar operaciones entre tipos incompatibles

