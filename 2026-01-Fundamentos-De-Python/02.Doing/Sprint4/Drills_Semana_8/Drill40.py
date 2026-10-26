# DRILL 5: LA FUNCIÓN-MENÚ DE SOFÍA

# TODO 1: Define una función llamada 'mostrar_menu' que NO recibe parámetros.

# TODO 2: Dentro de la función, imprime el menú principal de SonidoLibre:
#   ============================
#         SONIDOLIBRE 2026
#   ============================
#   1. Registrar banda
#   2. Ver cartel completo
#   3. Buscar banda
#   4. Salir
#   ============================

# TODO 3: Llama a mostrar_menu() tres veces seguidas con un mensaje
# distinto entre cada llamada para simular un sistema en uso:
#   mostrar_menu()
#   print(">> Acción ejecutada: registrar banda")
#   mostrar_menu()
#   print(">> Acción ejecutada: ver cartel")
#   mostrar_menu()
#   print(">> Hasta luego.")

# TODO 1
def mostrar_menu():
    # TODO 2
    print("\n" + "=" * 30)
    print("      SONIDOLIBRE 2026")
    print("=" * 30)
    print("  1. Registrar banda")
    print("  2. Ver cartel completo")
    print("  3. Buscar banda")
    print("  4. Salir")
    print("=" * 30)

# TODO 3
mostrar_menu()
print(">> Acción ejecutada: registrar banda")
mostrar_menu()
print(">> Acción ejecutada: ver cartel")
mostrar_menu()
print(">> Hasta luego.")