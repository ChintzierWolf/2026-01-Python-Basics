"""
Contexto real. Trabajas en el área de crédito de un banco. 
Te piden un script que simule lo siguiente: una cuenta empresarial 
tiene un saldo disponible de $1,000. Cada día se le carga un cargo 
fijo de $150 por servicios. 

Tu programa tiene que decirme cuántos días pasan antes de que el saldo 
llegue a cero o se quede en negativo, y cuál es el saldo final.

"""

# Definimos las variables iniciales
dias = 0
cargo = 100
saldo = 1000

while saldo > 0:
    saldo -= cargo
    dias += 1

    print(f"Día {dias}: Saldo actual ${saldo}")

# Imprimimos el resultado
print(f"Días transcurridos: {dias}")
print(f"Saldo final: ${saldo}")

# ----------------- Ejemplo 2 ----------------- 

# Usamos un bucle while para iterar sobre una secuencia de números
# Definimos las variables iniciales
saldo_disponible = 1000
cargo_diario = 150
dias_transcurridos = 0

while saldo_disponible > 0:
    saldo_disponible -= cargo_diario
    dias_transcurridos += 1

    print(f"Día {dias_transcurridos}: Saldo actual ${saldo_disponible}")
    print("Dia", dias_transcurridos, ": Saldo actual", saldo_disponible)

"""
Vuelta │ saldo (antes) │ saldo (después) │ dias_transcurridos │ ¿condición True?
───────┼───────────────┼─────────────────┼────────────────────┼─────────────────
  1    │  1000         │  850            │  1                 │ Sí (1000 > 0)
  2    │  850          │  700            │  2                 │ Sí (850  > 0)
  3    │  700          │  550            │  3                 │ Sí (700  > 0)
  ...  │  ...          │  ...            │  ...               │ ...
  7    │  100          │  -50            │  7                 │ Sí (100  > 0)
  8    │  -50          │  ─              │  ─                 │ No (-50 < 0) → sale
"""

#Tabla de códigos de escape comunes

#Código |  Nombre           |  Qué hace                                                               |  Ejemplo                   |  Resultado|
#_____________________________________________________________________________________________________________________________
#\t     |  Tabulador        |  Inserta un espacio largo (sangría).                                    |  print("Nombre:\tJuan")    |  Nombre:  Juan
#\      |  Barra invertida  |  Imprime una barra invertida sin romper el código.                      | print("Ruta: C:\\Usuario") |  Ruta: C:\Usuario
#'      |  Comilla simple   |  Permite usar comillas simples dentro de un texto con comillas simples. | print('It's basic')        |  It's basic
#"      |  Comilla doble    |  Permite usar comillas dobles dentro de un texto con comillas dobles.   | print("Dijo: "Hola"")      |  Dijo: "Hola"
#\r     |  Retorno de carro |  Mueve el cursor al inicio de la línea actual, borrando lo anterior.    | print("Hola\rMundo")       | Mundo
#\b     |  Retroceso        |  Borra el carácter anterior (como la tecla Backspace).                  | print("Hola\bMundo")       | HolaMundo
#\n     |  Salto de línea   |  Inserta una nueva línea.
print("Hola\nMundo") 
#Hola
#Mundo