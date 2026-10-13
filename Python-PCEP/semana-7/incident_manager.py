""""
ESPECIFICACIÓN DEL RETO

Nombre del archivo: incidentManager.py

Contexto: Eres parte del equipo de mesa de servicio (help desk) de una empresa con 200 empleados. Tu turno es de 8 horas y necesitas un sistema en memoria para registrar, listar, cerrar y buscar incidentes durante tu turno. Cuando termina el turno, el sistema se cierra y los datos se pierden (en sprints futuros aprenderán a guardarlos en disco).
Estructura inicial:
· Una lista incidentes que arranca con 3 tickets pre-cargados (los del turno anterior que quedaron pendientes).
· Un menú dentro de un while True: con 5 opciones:

1. Registrar nuevo incidente
2. Listar todos los incidentes abiertos
3. Cerrar un incidente (por número de posición)
4. Buscar si un incidente existe (por ID exacto)
5. Salir del sistema

Reglas de negocio (todas obligatorias):
   #    | Regla                                                                                                                | Razón
==================================================================================================================================================================
Regla 1 | El menú se muestra numerado del 1 al 5, no del 0 al 4                                                                | Humanos cuentan desde 1
Regla 2 | El reporte de incidentes también se numera del 1 en adelante                                                         | Mismo principio
Regla 3 | Cerrar incidente pide al usuario el NÚMERO HUMANO (1, 2, 3...) y el programa internamente lo convierte a índice (-1) | Conversión explícita
Regla 4 | Si el usuario pide cerrar el número 99 cuando solo hay 3, el programa NO truena. Muestra "Número fuera de rango. Hay X incidentes." | Guardia con if
Regla 5 | Si el usuario pide listar y la lista está vacía, NO se imprime un reporte vacío. Se muestra "No hay incidentes abiertos." | UX profesional
Regla 6 | Buscar por ID usa el operador in. Si existe muestra "Encontrado". Si no, muestra "No se encontró ese ID."              | Patrón profesional
Regla 7 | Si el usuario elige opción inválida (6, 0, "hola"), el programa NO truena. Muestra "Opción inválida" y vuelve al menú. | Aprovecha lo de Clase 6
Regla 8 | Al salir con opción 5, se imprime "Sesión cerrada. Hasta el próximo turno." y se rompe el loop con break               | Cierre limpio

Lo que NO va en este reto (no lo intenten):
· ❌ Funciones (def) — se cubren en Clase 8
· ❌ try/except — se cubren en Sprint 6
· ❌ Diccionarios para los tickets — Sprint 5
· ❌ Persistencia en archivo — Sprint 6
"""

lista_incidentes = ["INC-001: Impresora bloqueada", "INC-002: Correo no envía emails", "INC-003: No puedo conectarme a la red WiFi"]

#---------------------------------------------------------------------------------------------------------------

while True:
    print("MENÚ DE INCIDENTES")
    print("1. Registrar nuevo incidente")
    print("2. Listar todos los incidentes abiertos")
    print("3. Cerrar un incidente (por número de posición)")
    print("4. Buscar si un incidente existe (por ID exacto)")
    print("5. Salir del sistema")
    
    menu = input("Seleccione una opción: ").strip()
    
    if menu not in ["1","2","3","4","5"]:
        print("Opción inválida. Intenta elegir una opción nuevamente")
        continue
    
    # Ingresar nuevo incidente
    if menu == "1":
        incidente_sin_id = input("Ingrese el nuevo incidente: ").strip()
        
        # Generar incidente con ID INC-xxx
        incidente_con_id = f"INC-{len(lista_incidentes) + 1:03d}"
        if not incidente_sin_id:
            print("No se puede registrar un incidente sin descripción")
            continue
        
        # Agregar incidente a la lista
        lista_incidentes.append(incidente_con_id + ": " + incidente_sin_id)
        print(f"Incidente registrado: {incidente_con_id}")
        continue
    
    # Listar incidentes
    if menu == "2":
        if not lista_incidentes:
            print("No hay incidentes abiertos")
        else:
            print("Incidentes abiertos")
            print("-" * 25)
            for i, incidente in enumerate(lista_incidentes, start=1):
                print(f"{i}. {incidente}")
        continue

    # Cerrar incidente
    if menu == "3":
        if not lista_incidentes:
            print("No hay incidentes para cerrar")
            continue
        else:
            pos = int(input("Ingrese el ID del incidente a cerrar: ").strip())
            if pos < 1 or pos > len(lista_incidentes):
                print(f"Número fuera de rango. Hay {len(lista_incidentes)} incidentes.")
                continue
            
            cerrado = lista_incidentes.pop(pos - 1)
            print(f"Incidente {cerrado} cerrado exitosamente.")
            continue

    # Buscar incidente por ID
    if menu == "4":
        if not lista_incidentes:
            print("No hay incidentes para buscar")
        else:
            incidente_buscado = input("Ingrese el ID del incidente a buscar: ").strip()
            encontrado = False
            for ticket in lista_incidentes:
                if incidente_buscado in ticket:
                    encontrado = True
                    break
            if encontrado:
                print("Encontrado", incidente_buscado)
            else:
                print("No se encontró ese ID")
            continue

    # Salir del sistema
    if menu == "5":
        print("Sesión cerrada. Hasta el próximo turno.")
        break

# ==============================================================================
# SUGERENCIAS DE MEJORA Y OBSERVACIONES (REVISIÓN DE REGLAS DE NEGOCIO)
# ==============================================================================
#
# 1. ENTRADA DEL MENÚ Y REGLA 7 (Validación de entrada sin tronar):
#    - Actualmente usas: menu = int(input("Seleccione una opción: "))
#    - Si el usuario ingresa texto como "hola" o presiona Enter en blanco, Python
#      arroja ValueError y el programa se cae ("truena").
#    - Como la especificación prohíbe try/except, la técnica de la Clase 6 es
#      conservar el valor como texto:
#          menu = input("Seleccione una opción: ").strip()
#          if menu not in ["1", "2", "3", "4", "5"]:
#              print("Opción inválida")
#              continue
#      Y luego comparar como strings (menu == "1", etc.). Así nunca se cae.
#
# 2. OPCIÓN 1 (Registrar nuevo incidente) - Formato de ID y validación:
#    - Se genera el ID con: "INC-" + str(len(lista_incidentes) + 1), dando "INC-4".
#    - Para mantener la consistencia con los tickets precargados ("INC-001", "INC-002"...),
#      se puede formatear con ceros a la izquierda usando:
#          incidente_con_id = f"INC-{len(lista_incidentes) + 1:03d}"
#    - Opcionalmente, validar que no registren una descripción vacía con:
#          if not incidente_sin_id: ...
#
# 3. OPCIÓN 3 (Cerrar incidente) - REGLAS 3 Y 4 (Cierre por posición, no por ID):
#    - Actualmente pides el ID y haces: if incidente_cerrado not in lista_incidentes:
#      Al guardar strings completos ("INC-001: Impresora..."), buscar solo el ID
#      no coincide.
#    - Más importante aún, la especificación pide:
#      * Regla 3: Solicitar el NÚMERO HUMANO de posición (1, 2, 3...) y restar 1
#        para obtener el índice de la lista.
#      * Regla 4: Si el número está fuera de rango (ej. 99 habiendo 3 tickets),
#        mostrar: "Número fuera de rango. Hay X incidentes."
#      * Para eliminar por posición, usar pop() visto en la Semana 7:
#          if pos < 1 or pos > len(lista_incidentes):
#              print(f"Número fuera de rango. Hay {len(lista_incidentes)} incidentes.")
#          else:
#              cerrado = lista_incidentes.pop(pos - 1)
#              print(f"Incidente cerrado: {cerrado}")
#
# 4. OPCIÓN 4 (Buscar incidente por ID) - REGLA 6:
#    - La comprobación: if incidente_buscado in lista_incidentes: busca si existe
#      un elemento idéntico. Como los elementos contienen ID + descripción,
#      buscar únicamente "INC-001" da False.
#    - Para evaluar si el ID está dentro de algún ticket usando el operador 'in':
#          encontrado = False
#          for ticket in lista_incidentes:
#              if incidente_buscado in ticket:
#                  encontrado = True
#                  break
#          if encontrado:
#              print("Encontrado")
#          else:
#              print("No se encontró ese ID.")
#
# 5. ESTRUCTURA Y SINTAXIS:
#    - En lugar de usar múltiples 'if' con 'continue' independientes en cada caso,
#      encadenar con 'elif' hace que el flujo sea más legible y convencional.
# ==============================================================================