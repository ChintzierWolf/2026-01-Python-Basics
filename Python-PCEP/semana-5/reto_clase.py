"""
ESPECIFICACIÓN — procesador_lotes.py

CONTEXTO
Trabajas en el área de procesamiento batch de una financiera. Cada noche,
el sistema procesa N lotes pendientes. Cada lote contiene M transacciones
del mismo monto. Tu programa debe procesar todos los lotes, acumular el
total, y emitir una alerta cada vez que el acumulado cruza el umbral.

VARIABLES DE ENTRADA (declaradas al inicio del archivo — NO uses input())
  lotes_pendientes        = 5         # número de lotes a procesar
  transacciones_por_lote  = 3         # transacciones que contiene cada lote
  monto_por_transaccion   = 1200.50   # monto fijo de cada transacción
  umbral_alerta           = 10000     # umbral para emitir alerta

COMPORTAMIENTO ESPERADO
  
Procesa los lotes uno por uno con un loop while.
Por cada lote, procesa sus transacciones con un loop for + range().
Imprime una línea por cada transacción:"[Lote X | Trans Y] Monto: $1200.5 | Acumulado: $XXXX.XX"
Cada vez que el acumulado supere el umbral_alerta y la línea anterior
no lo superaba, imprime UNA SOLA VEZ:"[ALERTA] Umbral de $10000 excedido en lote X, transacción Y"
Al finalizar todos los lotes, imprime un resumen:"Total procesado: $XXXXX.XX""Lotes procesados: X""Transacciones procesadas: X"

REGLAS DE CONSTRUCCIÓN
  
El while exterior controla los lotes pendientes.
El for interior controla las transacciones dentro del lote.
PROHIBIDO usar: break, continue, while True, def, return, listas, dicts.
Numera los lotes empezando en 1, no en 0.
Numera las transacciones empezando en 1, no en 0.

VALORES ESPERADOS (con la configuración base)
  
Total procesado: $18007.5
Lotes procesados: 5
Transacciones procesadas: 15
La alerta debe aparecer UNA SOLA VEZ (cuando se cruza por primera vez)
"""

# Variables de entrada (declaradas al inicio del archivo — NO uses input())
lotes_pendientes        = 5         # número de lotes a procesar
transacciones_por_lote  = 3         # transacciones que contiene cada lote
monto_por_transaccion   = 1200.50   # monto fijo de cada transacción
umbral_alerta           = 10000     # umbral para emitir alerta

# Inicializar contadores
acumulado_general = 0.0
lotes_procesados = 0
transacciones_procesadas = 0

# Controlar si la alerta ya se disparó (solo una vez)
alerta_disparada = False

# Loop principal para procesar lotes
while lotes_pendientes > 0:
    # Procesar transacciones del lote actual
    for i in range(1, transacciones_por_lote + 1):
        # Acumular el monto
        acumulado_general += monto_por_transaccion
        
        # Incrementar contador de transacciones
        transacciones_procesadas += 1
        
        # Imprimir detalle de la transacción
        print(f"[Lote {lotes_pendientes} | Trans {i}] Monto: ${monto_por_transaccion:.2f} | Acumulado: ${acumulado_general:.2f}")
        
        # Evaluar si se supera el umbral
        if acumulado_general > umbral_alerta and not alerta_disparada:
            print(f"\n[ALERTA] Umbral de ${umbral_alerta} excedido en lote {lotes_pendientes}, transacción {i}\n")
            alerta_disparada = True
    
    # Incrementar contador de lotes
    lotes_pendientes -= 1
    lotes_procesados += 1

# Imprimir resumen final
print("=" * 60)
print(f"Total procesado: ${acumulado_general:.2f}")
print(f"Lotes procesados: {lotes_procesados}")
print(f"Transacciones procesadas: {transacciones_procesadas}")
print("=" * 60 + "\n")