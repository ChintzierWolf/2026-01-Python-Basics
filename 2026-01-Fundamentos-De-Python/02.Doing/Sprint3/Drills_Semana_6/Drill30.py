# DRILL 10: EL CONTEO SELECTIVO DE CHECO

# TODO 1: Antes del bucle, crea un acumulador 'contador_aforo = 0'.

# TODO 2: Usa 'for credencial in range(1, 21):' para recorrer del 1 al 20.
# Dentro del bucle:
#   - Si 'credencial' es múltiplo de 5 (pista: módulo % devuelve el residuo,
#     un número es múltiplo de 5 cuando el residuo es 0), usa 'continue'
#     para saltar el resto de esta vuelta.
#   - Si no, suma 1 al contador_aforo e imprime con f-string:
#     "Credencial {credencial} contada -- aforo actual {contador_aforo}".

# TODO 3: Fuera del bucle, imprime:
# "Aforo oficial del día: {contador_aforo} personas (cortesías excluidas)."

contador_aforo = 0

for credencial in range(1,21):
    if credencial % 5 == 0:
        continue
    else:
        contador_aforo += 1
        print(f"Credencial {credencial} contada -- aforo actual {contador_aforo}")

print(f"Aforo oficial del día: {contador_aforo} personas (cortesías excluidas).")