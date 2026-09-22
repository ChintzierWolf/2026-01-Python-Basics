# RETO AUTONOMO 3.2

# Una institución financiera necesita un módulo de pre-evaluación crediticia
# El sistema toma 6 variables de entrada y aplica las relgas de negocio en el orden correcto

#── VARIABLES DE ENTRADA ───────────────────────────────────────────────────
#  nombre                 → str   (nombre completo del solicitante)
#  ingreso_mensual  → float (ingreso neto mensual en pesos)
#  deuda_mensual    → float (total de pagos de deuda actuales por mes)
#  tipo_empleo          → str   ("permanente" / "contrato" / "independiente" / "desempleado")
#  score_crediticio     → int   (score de buró, rango 300-850)
#  antiguedad_años  → int   (años en el empleo actual o en actividad independiente)

#───────────────────────────────────────────────────────────────────────────

print("Programa de evaluación de crédito.")
print("Por favor, responde las siguientes preguntas:")

nombre = input("¿Cuál es tu nombre completo?: ")
ingreso_mensual = float(input("¿Cuál es tu ingreso mensual neto?: "))
deuda_mensual = float(input("¿Cuál es el total de tus deudas mensuales?: "))
tipo_empleo = input("¿Cuál es tu tipo de empleo? (permanente/contrato/independiente/desempleado): ")
score_crediticio = int(input("¿Cuál es tu score de buró? (300-850): "))
antiguedad_años = int(input("¿Cuántos años llevas en tu empleo actual?: "))

#── CÁLCULOS REQUERIDOS (ANTES DE LOS if) ───────────────────────────────────────────────────
ratio_deuda = deuda_mensual / ingreso_mensual
# viabilidad_empleo = True si tipo_empleo está en ["permanente", "independiente"]
viabilidad_empleo = tipo_empleo in ["permanente", "independiente", "contrato", "desempleado"]
# Ejemplo: si ingreso = 30000 y deuda = 9000, ratio = 0.30 = 30%
capacidad_pago = ingreso_mensual - deuda_mensual
# Cuanto le queda disponible después de pagar deudas actuales

#── REGLAS DE NEGOCIO (en este orden exacto) ───────────────────────────────────────────────────

# Regla 1:
if tipo_empleo == "desempleado":
    resultado = "DENEGADO - sin actividad ecónomica activa"
    print(f"Estimado {nombre}, DENEGADO - sin actividad ecónomica activa")
# DENEGADO : sin actividad ecónomica activa

# Regla 2:
elif score_crediticio < 500:
    resultado = "DENEGADO - Score menor a 500"
    print(f"Estimado {nombre}, DENEGADO - Score menor a 500")
# DENEGADO: score en rango de alto riesgo

# Regla 3:
elif ratio_deuda > 0.50:
    resultado = "DENEGADO - más del 50% del ingreso comprometido en deudas"
    print(f"Estimado {nombre}, DENEGADO - más del 50% del ingreso comprometido en deudas")
# DENEGADO: más del 50% del ingreso comprometido en deudas

# Regla 4:
elif tipo_empleo == "independiente" and antiguedad_años < 3:
    resultado = "DENEGADO - actividad independiente con menos de 3 años de antiguedad"
    print(f"Estimado {nombre}, DENEGADO - actividad independiente con menos de 3 años de antiguedad")
# DENEGADO: actividad independiente con menos de 3 años de antiguedad

# Regla 5:
elif score_crediticio >= 750 and ratio_deuda <= 0.25 and tipo_empleo == "permanente":
    resultado = "APROBADO - tasa preferencial (el mejor perfil)"
    print(f"Estimado {nombre}, APROBADO - tasa preferencial (el mejor perfil)")
# APROBADO: tasa preferencial (el mejor perfil)

# Regla 6:
elif score_crediticio >= 600 and ratio_deuda <= 0.40:
    resultado = "APROBADO - tasa estándar."
    print(f"Estimado {nombre}, APROBADO - tasa estándar.")
# APROBADO: tasa estándar

# Regla 7:
elif score_crediticio >= 500 and ratio_deuda <= 0.50:
    resultado = "PENDIENTE - se requiere análisis adicional por un ejecutivo de crédito."
    print(f"Estimado {nombre}, se requiere análisis adicional por un ejecutivo de crédito.")
# PENDIENTE : se requiere análisis adicional por un ejecutivo de crédito

# Regla 8:
else: 
    resultado = "DENEGADO - perfil de alto riesgo"
    print(f"Estimado {nombre}, no se otorga crédito. Perfil de alto riesgo")
# Ninguna condición anterior se cumplió: DENEGADO: perfil de alto riesgo

#── FORMATO DE SALIDA ───────────────────────────────────────────────────
# El mensaje debe incluir: nombre, resultado y los valores calculados relevantes|
# Ejemplo: "APROBADO (preferencial) - Ana García | Score: 790 | Ratio deuda: 18.25 | Ratio: 0.1825"
# Si el resultado es "PENDIENTE", añadir "|" antes del score



print(f"{nombre} {resultado} - Score: {score_crediticio} | Ratio deuda: {ratio_deuda:.2f}")