# DRILL 9: EL CARTEL DE DANIELA

# TODO 1: Imprime una línea de 20 signos "=" usando "=" * 20.

# TODO 2: Imprime el título centrado visualmente: "  SONIDOLIBRE 25"
# (con dos espacios al inicio).

# TODO 3: Imprime otra línea igual a la del TODO 1.

# TODO 4: Usa 'for fila in range(1, 6):' para imprimir una escalera
# de 5 filas. En cada vuelta imprime "*" multiplicado por 'fila'.

# TODO 5: Después del bucle, imprime otra línea de 20 signos "=".

print("=" * 20)
print("  SONIDOLIBRE 25")
print("=" * 20)
for fila in range(1, 6):
    print("*" * fila)
print("=" * 20)