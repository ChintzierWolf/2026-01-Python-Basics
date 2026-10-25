# DRILL 5: EL FLYER REDUCIDO DE SOFÍA

cartel_completo = [
  "Los Granados",
  "Cardumen",
  "La Sierra",
  "Espuma Fría",
  "Aurora Doble",
  "Vento Sur",
  "Tornillos",
  "Lumbre Lenta"
]

# TODO 1: Usa slicing para sacar las primeras 3 bandas (headliners)
# y guárdalas en una variable llamada 'headliners'.

# TODO 2: Usa slicing para sacar las últimas 3 bandas (emergentes)
# y guárdalas en una variable llamada 'emergentes'.

# TODO 3: Imprime ambos grupos con un encabezado:
# "🎤 HEADLINERS: [headliners]"
# "🎸 EMERGENTES: [emergentes]"

# TODO 4: Verifica que la lista original NO cambió.
# Imprime cartel_completo y comprueba que sigue teniendo las 8 bandas.

headliners = cartel_completo[0:3]
emergentes = cartel_completo[-3:]

print(f"\n🎤 HEADLINERS: {headliners}")
print(f"🎸 EMERGENTES: {emergentes}")

print(f"\nCartel completo: {cartel_completo}\n")
