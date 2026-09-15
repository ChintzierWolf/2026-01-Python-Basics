# TALLER SPRINT 1: EL DETECTOR VIP

# TODO 1: Crea una variable llamada 'nombre' y guarda tu nombre como texto.

# TODO 2: Crea una variable llamada 'ciudad' y guarda tu ciudad de origen.

# TODO 3: Crea una variable llamada 'frase_favorita' con una frase que te identifique.

# TODO 4: Usa print() con f-strings para mostrar un mensaje que combine las tres variables.
# Ejemplo de salida: "Hola, soy Ana, vengo de Bogotá y mi frase es: El código no miente.

nombre = "César"
ciudad = "Aguascalientes"
frase_favorita = "Cada puerta que abres hacia la oscuridad, te brinda otra oportunidad de combatirla."

print(f"Hola, soy {nombre}, vengo de {ciudad} y mi frase favorita es: {frase_favorita}")

#-----------------------------------------------------------------------------------#

# Variables
nombre = "César"
numero_favorito = 7
profesion = "programador"

# Imprimir con diferentes métodos
# Usando f-string (moderno y recomendado)
print(f"Hola, mi nombre es {nombre}, mi número favorito es {numero_favorito} y mi profesión es {profesion}")

# Usando el método .format()
print("Hola, mi nombre es {}, mi número favorito es {} y mi profesión es {}".format(nombre, numero_favorito, profesion))

# Concatenando strings
print("Hola, mi nombre es " + nombre + ", mi número favorito es " + str(numero_favorito) + " y mi profesión es " + profesion)

# Usando comas en print (automáticamente añade espacios)
print("Hola, mi nombre es", nombre, ", mi número favorito es", numero_favorito, "y mi profesión es", profesion)