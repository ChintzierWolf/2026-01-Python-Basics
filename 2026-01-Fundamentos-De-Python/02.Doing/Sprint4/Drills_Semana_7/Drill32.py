# DRILL 2: LA BANDA PRINCIPAL

# Esta lista ya está dada — úsala como punto de partida.

# TODO 1: Guarda en una variable 'headliner' la primera banda de la lista
# usando el índice correcto.

# TODO 2: Guarda en una variable 'sorpresa_cierre' la última banda
# usando el índice -1.

# TODO 3: Imprime ambos resultados con f-strings:
# "Headliner del festival: [headliner]"

bandas_confirmadas = [
  "Los Granados",
  "Cardumen",
  "La Sierra",
  "Voltio Norte",
  "Mareas Altas"
]

headliner = bandas_confirmadas[0]
sorpresa_cierre = bandas_confirmadas[-1]

print(f"Headliner: {headliner}")
print(f"Banda sorpresa de cierre: {sorpresa_cierre}")
