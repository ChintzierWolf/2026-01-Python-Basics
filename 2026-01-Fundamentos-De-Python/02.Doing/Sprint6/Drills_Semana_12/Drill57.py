# DRILL 2: EL LOOP DE ACERO

# TODO 1: Abre un bucle while True (infinito a propósito).

while True:
        
# TODO 2: Dentro del bucle, abre un bloque try.
# En el try, pide al usuario el número de baterías con input() y conviértelo
# con int(). Guarda el resultado en una variable llamada 'baterias'.
# Después de la conversión exitosa, usa break para salir del bucle.

    try:
        baterias = int(input("Ingrese el número de baterías: "))
        break

# TODO 3: Agrega un except ValueError que imprima un mensaje pidiendo
# que reintente. Como NO hay break en el except, el bucle vuelve a empezar.
    
    except ValueError:
        print("Por favor reintente.")

# TODO 4: FUERA del bucle (sin indentación), imprime:
# "Baterías registradas: [baterias]"
# Esa línea solo se ejecuta cuando el break se haya disparado.

print(f"Baterías registradas: {baterias}")
