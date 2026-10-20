# DRILL 3: LA CANCELACIÓN DE ÚLTIMO MINUTO

bandas_confirmadas = [
  "Los Granados",
  "Cardumen",
  "La Sierra",
  "Voltio Norte",
  "Mareas Altas"
]

# TODO 1: Usa .remove() para eliminar "Voltio Norte" de la lista.

# TODO 2: Usa .insert() para meter "Espuma Fría" en la posición 3
# (la posición donde estaba Voltio Norte).

# TODO 3: Imprime la lista actualizada.

# TODO 4: Usa .pop() sin argumentos para sacar la última banda
# (la sorpresa de cierre cambió de planes también).
# Guarda el resultado en una variable llamada 'banda_retirada'.

# TODO 5: Imprime un mensaje:
# "Banda retirada del cartel: [banda_retirada]"
# y la lista final.

bandas_confirmadas.remove("Voltio Norte")
bandas_confirmadas.insert(3, "Espuma Fría")

print("\n=== Lista Actualizada ===\n")
for i, banda in enumerate(bandas_confirmadas):
    print(f"{i + 1}. {banda}")

banda_retirada = bandas_confirmadas.pop()

print(f"\nBanda retirada del cartel: {banda_retirada}")

print(f"\n=== Lista Final ===\n")
for i, banda in enumerate(bandas_confirmadas):
    print(f"{i + 1}. {banda}")