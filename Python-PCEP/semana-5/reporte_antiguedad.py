"""
Nuevo Contexto. RRHH te pide un reporte que muestre los años de servicio de empleados que entraron entre el año 
2018 y el año 2025 inclusive.
Por cada año, debe imprimir cuántos años de antigüedad acumulan al cierre de 2025
"""

# Reporte de antigüedad -- empleados ingresados 2018-2025
anio_corte = 2025

print(f"Reporte de antigüedad al cierre de {anio_corte}\n")

for anio_ingreso in range(2018, 2025 + 1):
    antiguedad = anio_corte - anio_ingreso
    print(f"Ingreso {anio_ingreso} -> {antiguedad} años de antigüedad")