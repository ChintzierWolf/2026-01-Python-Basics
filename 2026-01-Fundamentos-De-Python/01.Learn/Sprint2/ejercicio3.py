edad = int(input("¿Cuál es tu edad?: "))
dinero = float(input("¿Cuánto dinero tienes?: "))

acceso_concedido = edad >= 18 and dinero >= 500

print(f'¿Acceso concedido?: {acceso_concedido}')