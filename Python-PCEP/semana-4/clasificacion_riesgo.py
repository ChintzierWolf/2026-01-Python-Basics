"""
RETO AUTÓNOMO: clasificacion_riesgo.py (20 minutos de construcción)
Estándar ISO 31000 — Gestión de Riesgos Empresariales.
El sistema evalúa un proceso de negocio y lo clasifica según su nivel de riesgo.

── VARIABLES DE ENTRADA ────────────────────────────────────────────────
  nombre_proceso  → str   (nombre del proceso evaluado)
  probabilidad    → int   (1-5: probabilidad de que ocurra el riesgo)
  impacto         → int   (1-5: magnitud del daño si ocurre)
  con_controles   → str   ("si"/"no": ¿existen controles mitigantes vigentes?)

── CÁLCULOS REQUERIDOS (ANTES de los elif) ────────────────────────────
  riesgo_inherente = probabilidad * impacto       (rango: 1-25)
  Si con_controles == "si":
      riesgo_residual = riesgo_inherente * 0.6    (reducción del 40%)
  Si no:
      riesgo_residual = riesgo_inherente

── CLASIFICACIÓN (más restrictivo PRIMERO) ────────────────────────────
  riesgo_residual >= 20  →  CRÍTICO   · "Suspender proceso. Escalar a Dirección."
  riesgo_residual >= 15  →  ALTO      · "Plan de mitigación en menos de 24 horas."
  riesgo_residual >= 10  →  MEDIO     · "Revisión en próxima reunión de riesgos."
  riesgo_residual >= 5   →  BAJO      · "Monitoreo periódico según calendario."
  riesgo_residual < 5    →  MÍNIMO    · "Documentar y revisar en auditoría anual."

── FORMATO DE SALIDA ───────────────────────────────────────────────────
  Debe incluir: nombre del proceso, riesgo inherente, riesgo residual y clasificación.
  Ejemplo: "Proceso de pagos | Inherente: 20 | Residual: 12.0 → MEDIO"
"""

#------------------------- EJERCICIO DE CLASIFICACION DE RIESGO-------------------------#
#Nombre del proceso
nombre_proceso = input("\nNombre del proceso: ")
#Probabilidad de que ocurra el riesgo
probabilidad = int(input("\nProbabilidad de que ocurra el riesgo (1-5): "))
#Magnitud del daño si ocurre
impacto = int(input("\nMagnitud del daño si ocurre (1-5): "))
#Existen controles mitigantes vigentes
con_controles = input("\n¿Existen controles mitigantes vigentes? (si/no): ")
#Calcular el riesgo inherente (rango de 1 - 25)
riesgo_inherente = probabilidad * impacto
#Calcular el riesgo residual
if con_controles == "si":
    riesgo_residual = riesgo_inherente * 0.6
else:
    riesgo_residual = riesgo_inherente
#Clasificar el riesgo
if riesgo_residual >= 20:
    clasificacion = "CRÍTICO"
    accion = "Suspender proceso. Escalar a Dirección."
elif riesgo_residual >= 15:
    clasificacion = "ALTO"
    accion = "Plan de mitigación en menos de 24 horas."
elif riesgo_residual >= 10:
    clasificacion = "MEDIO"
    accion = "Revisión en próxima reunión de riesgos."
elif riesgo_residual >= 5:
    clasificacion = "BAJO"
    accion = "Monitoreo periódico según calendario."
else:
    clasificacion = "MÍNIMO"
    accion = "Documentar y revisar en auditoría anual."

# Imprimir resultados en el formato especificado:
print(f"\n{nombre_proceso} | Inherente: {riesgo_inherente} | Residual: {riesgo_residual:.2f} → {clasificacion}\n")
print(f"{nombre_proceso} | {riesgo_inherente=} | {riesgo_residual=} | {clasificacion=}")
# Al agregar un = a la variable dentro del f-string se muestra el nombre de la variable y su valor.

# Mostrar resultados:
print("\n========= RESULTADO DE LA EVALUACIÓN =========\n")
print(f"Proceso evaluado: {nombre_proceso}")
print(f"Probabilidad (1-5): {probabilidad}")
print(f"Impacto (1-5): {impacto}")
print(f"Controles existentes: {con_controles}")
print(f"Riesgo inherente (probabilidad * impacto): {riesgo_inherente}")
print(f"Riesgo residual (riesgo inherente * 0.6 si con_controles == 'si' o riesgo inherente si no): {riesgo_residual:.2f}")
print(f"Clasificación del riesgo: {clasificacion}")
print(f"Acción recomendada: {accion}\n\n")

