"""
Nuevo Contexto. RRHH te pide un reporte que muestre los años de servicio de empleados que entraron entre el año 
2018 y el año 2025 inclusive.
Por cada año, debe imprimir cuántos años de antigüedad acumulan al cierre de 2025
"""

# Reporte de antigüedad -- empleados ingresados 2018-2025
anio_corte = int(input("Ingrese el año de corte: "))
anio_inicio = int(input("Ingrese el año de inicio: "))
anio_fin = int(input("Ingrese el año de fin: "))

print(f"Reporte de antigüedad al cierre de {anio_corte}\n")

for anio_ingreso in range(anio_inicio, anio_fin + 1):
    antiguedad = anio_corte - anio_ingreso
    print(f"Ingreso {anio_ingreso} -> {antiguedad} años de antigüedad")

"""
Ahora me piden algo diferente. Quiero realizar un ejercicio donde pueda imprimir los trimestres del año fiscal.
 Son 4. Quiero que diga "Trimestre 1", "Trimestre 2", "Trimestre 3", "Trimestre 4".
"""

#for trimestre in range(1, 5):
#    print(f"trimestre {trimestre}")

# Pagos Quincenales del año - 15 días, suponiendo 360 días al año
print("\nReporte de pagos quincenales del año:")
for dia_del_anio in range(1, 361, 15):
    print(f"Pago el día {dia_del_anio}")

