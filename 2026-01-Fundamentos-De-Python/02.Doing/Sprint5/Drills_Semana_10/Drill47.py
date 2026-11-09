# DRILL 2: CORTAR Y UNIR — MATEO PROCESA EL WHATSAPP

# TODO 1: Crea una variable llamada 'mensaje_whatsapp' con el siguiente texto:
# "Los Granados,Cardumen,La Sierra,Espuma Fría"

mensaje_whatsapp = "Los Granados,Cardumen,La Sierra,Espuma Fría"

# TODO 2: Usa .split(",") para separar el texto en una lista.
# Guarda el resultado en una variable llamada 'bandas'.

bandas = mensaje_whatsapp.split(",")

# TODO 3: Imprime la lista completa para verificar el corte.

print(f"Lista de bandas: {bandas}")

# TODO 4: Imprime cuántas bandas hay usando len().

print(f"Cantidad de bandas: {len(bandas)}")

# TODO 5: Usa .join() con " | " (espacio, barra, espacio) como separador
# para volver a unir la lista en un solo string formateado para el cartel.

cartel = " | ".join(bandas)
print(f"Cartel: {cartel}")