# DRILL 5: EL REPORTE COMPLETO DE SOFÍA

# TODO 1: Reutiliza el diccionario del drill anterior:
# "Ana López" → "Carpa de prensa"
# "Diego Ruiz" → "Backstage"
# "Mara Soto" → "Zona VIP"

# TODO 2: Usa un bucle for con .items() para iterar el diccionario.
# En cada vuelta, imprime una línea con el formato:
# "[nombre] → [zona]"

# TODO 3: Después del bucle (sin indentación), imprime una línea de cierre:
# "Reporte generado correctamente."

acreditaciones = {
    "Ana López": "Carpa de prensa",
    "Diego Ruiz": "Backstage",
    "Mara Soto": "Zona VIP"
}

for nombre, zona in acreditaciones.items():
    print(f"{nombre} → {zona}")

print("Reporte generado correctamente.")
