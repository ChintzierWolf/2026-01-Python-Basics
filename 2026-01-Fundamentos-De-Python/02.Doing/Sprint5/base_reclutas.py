# BASE DE RECLUTAS · INADAPTADOS
# Base de talento con menu de 4 opciones.
# Cada recluta es un diccionario con 5 campos:
#   nombre, area, salario_mensual, estatus, email

# Lista de arranque (ya poblada con 3 reclutas).
base_reclutas = [
  {"nombre": "Ana Torres",    "area": "Finanzas",  "salario_mensual": 28500.0,  "estatus": "activo",   "email": "ana.torres@inadaptados.mx"},
  {"nombre": "Luis Quintero", "area": "Logistica", "salario_mensual": 19200.0,  "estatus": "activo",   "email": "luis.quintero@inadaptados.mx"},
  {"nombre": "Mara Ibarra",   "area": "Salud",     "salario_mensual": 133750.0, "estatus": "inactivo", "email": "mara.ibarra@inadaptados.mx"},
]

# TODO: menu con while True (patron del Sprint 3).
# Imprime las 4 opciones, lee la opcion con input().strip()
# y ramifica con if / elif / else.
while True:
  print()
  print("=== BASE DE RECLUTAS · INADAPTADOS ===")
  print("1) Alta de recluta")
  print("2) Listado (reporte)")
  print("3) Buscar por nombre")
  print("4) Salir")
  opcion = input("Elige una opcion: ").strip()

  # TODO 1 (Alta): captura cada campo REASIGNANDO la limpieza.
  #   nombre y area  -> .strip().title()
  #   estatus y email -> .strip().lower()
  #   salario        -> float(input(...).strip())   (truena con coma: ok)
  # Arma el diccionario con los 5 campos y haz append() a base_reclutas.
  # Imprime un mensaje [OK] con el nombre y el total.
  if opcion == "1":
    nombre = input("Nombre: ").strip().title()
    area = input("Area: ").strip().title()
    salario_mensual = float(input("Salario mensual: ").strip())
    estatus = input("Estatus: ").strip().lower()
    email = input("Email: ").strip().lower()
    base_reclutas.append({"nombre": nombre, "area": area, "salario_mensual": salario_mensual, "estatus": estatus, "email": email})
    print(f"[OK] Recluta {nombre} agregada. Total: {len(base_reclutas)}")

  # TODO 2 (Listado): reporte tabular con 4 columnas.
  #   Encabezado: NOMBRE (<18), AREA (<14), ESTATUS (<11), SALARIO (>14)
  #   Separadora: "-" * 57   (18 + 14 + 11 + 14)
  #   Filas: recorre base_reclutas; salario con formato :>14,.2f
  #   Pie: "Total de reclutas: N"
  elif opcion == "2":
    print(f"{'NOMBRE':<18}{'AREA':<14}{'ESTATUS':<11}{'SALARIO':>14}")
    print("-" * 57)
    for recluta in base_reclutas:
      print(f"{recluta['nombre']:<18}{recluta['area']:<14}{recluta['estatus']:<11}{recluta['salario_mensual']:>14,.2f}")
    print(f"Total de reclutas: {len(base_reclutas)}")

  # TODO 3 (Buscar): normaliza el termino con .strip().lower().
  #   Recorre base_reclutas; compara con: termino in recluta["nombre"].lower()
  #   Usa un contador 'encontrados' para avisar si no hubo coincidencias.
  elif opcion == "3":
    termino = input("Nombre: ").strip().lower()
    encontrados = 0
    for recluta in base_reclutas:
      if termino in recluta["nombre"].lower():
        print(f"{recluta['nombre']}: {recluta['area']}")
        encontrados += 1
    if encontrados == 0:
      print("[?] No se encontro ningun recluta.")  

  # TODO 4 (Salir): imprime un mensaje de despedida y usa break.
  elif opcion == "4":
    print("Fin del programa. Hasta luego.")
    break  # reemplaza por tu codigo

  # TODO: opcion invalida -> mensaje de error.
  else:
    print("[!] Opcion invalida. Intenta de nuevo.")
# Resultado: No hay errores y el programa funciona correctamente.
