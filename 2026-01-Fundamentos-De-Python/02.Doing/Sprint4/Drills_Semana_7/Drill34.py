# DRILL 4: EL RADAR DE LUCÍA

cartel_oficial = [
  "Los Granados",
  "Cardumen",
  "La Sierra",
  "Espuma Fría",
  "Mareas Altas"
]

# TODO 1: Usa input() para pedirle a Lucía el nombre de una banda.
# Guárdalo en una variable llamada 'consulta'.

# TODO 2: Usa el operador 'in' dentro de un if/else para responder:
#   - Si la banda SÍ está en la lista, imprime:
#     "Confirmado: [consulta] toca en SonidoLibre."
#   - Si NO está, imprime:
#     "[consulta] no figura en el cartel oficial."

consulta = input("Ingrese el nombre de la banda a consultar: ")

if consulta in cartel_oficial:
    print("\n")
    print(f"Confirmado: {consulta} toca en SonidoLibre.")
    print("\n")
else:
    print("\n")
    print(f"{consulta} no figura en el cartel oficial.")
    print("\n")