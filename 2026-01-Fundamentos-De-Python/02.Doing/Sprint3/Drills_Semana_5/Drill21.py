# DRILL 1: EL CONTADOR REGRESIVO DE SOFÍA

# TODO 1: Crea una variable 'dias_restantes' que empiece en 7.
# TODO 2: Usa un while que repita mientras dias_restantes sea mayor que 0.
# TODO 3: Dentro del bucle, imprime con f-string: "Faltan {dias_restantes} días para SonidoLibre".
# TODO 4: Dentro del bucle también, decrementa dias_restantes en 1 (usa -= 1).
# TODO 5: Fuera del bucle (sin indentación), imprime "¡Hoy arranca el festival!".

dias_restantes = 7
while dias_restantes > 0:
    print(f"Faltan {dias_restantes} días para SonidoLibre")
    dias_restantes -= 1

print("¡Hoy arranca el festival!")