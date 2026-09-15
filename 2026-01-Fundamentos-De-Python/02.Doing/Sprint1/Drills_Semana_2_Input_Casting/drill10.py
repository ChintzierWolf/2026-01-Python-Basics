# DRILL 5: EL SISTEMA VIP DE SONIDOLIBRE

# TODO 1: Usa input() con int() para pedir la edad del asistente.
# Guárdala en una variable llamada 'edad'.

# TODO 2: Usa input() con float() para pedir el dinero que trae.
# Guárdalo en una variable llamada 'dinero'.

# TODO 3: Crea una variable llamada 'acceso_vip'.
# Asígnale una evaluación que verifique si la edad es mayor o igual a 18
# AND si el dinero es mayor o igual a 500.

# TODO 4: Usa una f-string para mostrar el resultado.
# Ejemplo de salida:
# "Acceso VIP: [acceso_vip]"

edad = int(input("Introduce tu edad: "))
dinero = float(input("Introduce la cantidad de dinero que traes: "))
acceso_vip = edad >= 18 and dinero >= 500

print(f"Acceso VIP: {str(acceso_vip)}")
