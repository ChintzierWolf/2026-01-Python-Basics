# DRILL 5: EL ESCENARIO DE SONIDOLIBRE EN ASCII

# TODO 1: Crea una variable 'nombre_festival' con "SonidoLibre".

# TODO 2: Usa print() para construir un escenario simple con al menos 5 líneas.
# Debe tener luces arriba, estructura del escenario y base.
# Usa caracteres como * | - / \

# TODO 3: La última línea debe usar una f-string para mostrar
# el nombre del festival desde la variable, no escrito a mano.
# Ejemplo de estructura (construye la tuya propia):
#
#   * * * * * * * * *
#   |               |
#   |   ESCENARIO   |
#   |               |
#   |_______________|
#   SonidoLibre 2026

nombre_festival = "SonidoLibre"

print(r"*/\ */\ */\ */\ */\ */\ */\ */\ */\ */")
print("|                                    |")
print("|                 EL                 |")
print("|               GRAN                 |")
print("|             ESCENARIO              |")
print("|                 DE                 |")
print(f"|            {nombre_festival}             |")
print("|____________________________________|")
print(f"      ¡Disfruta de {nombre_festival} 2026!")

#¿Por qué se utiliza r? 
# Se utiliza "r" antes de las comillas para indicar que la cadena es una "raw string" (cadena cruda).
# En una cadena cruda, los caracteres de escape como "\n" (salto de línea) no se interpretan 
# como secuencias de escape, sino que se tratan como caracteres literales. 
# Esto es útil cuando se trabaja con rutas de archivos o expresiones regulares que contienen "\", 
# o cuando se quiere imprimir el carácter "\" sin tener que escaparlo (escribiéndolo como "\\" ).