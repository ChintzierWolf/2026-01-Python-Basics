# DRILL 4: ACCESO A LA CABINA DE MANDO — BASE ARES

# TODO 1: Usa input() para pedir el comando de voz.
# Guárdalo en una variable llamada 'comando'.

# TODO 2: Crea una variable 'acceso_cabina' que sea True
# si el comando es "activar" OR si el comando es "Activar".

# TODO 3: Usa print() con f-string para mostrar el resultado.
# Ejemplo de salida:
# "¿Comando reconocido?: [acceso_cabina]"

print(f"")
comando = input("¿Cuál es el comando de voz?: ")

acceso_cabina = comando == "activar" or comando == "Activar"

print(f'\n¿Comando reconocido?: {acceso_cabina}\n')

print(f'\n ############################ Fin del programa ############################\n\n')