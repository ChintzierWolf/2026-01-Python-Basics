# CONTEXTO: Sistema de Control de Acceso Corporativo

# Una empresa necesita un script de validación para su sistema de seguridad física.
# El guardia ingresa los datos del empleado y el sistema determina qué nivel de acceso corresponde.

# Variables de entrada:
#  · ID del empleado (texto)
#  · Nivel de acceso asignado (entero 1-5)
#  · Departamento (Tecnología / Finanzas / RRHH / Operaciones / Dirección)
#  · Autorización especial vigente (si/no)
#  · Hora de ingreso (entero 0-23)

# Reglas de negocio (las construiremos en orden):
#  Regla 1: Horario laboral = entre las 8:00 y las 20:00 hrs.
#  Regla 2: Nivel 5 O autorización especial → acceso completo (con registro fuera de horario)
#  Regla 3: Nivel 3-4 en horario en depto. crítico → acceso a área restringida
#  Regla 4: Nivel 2-4 en horario → acceso a área general
#  Regla 5: Cualquier otro caso → acceso denegado

# Archivo: sistema_acceso.py
print("\n")
empleado_id = input("Introduce tu ID de empleado: \n")
nivel_acceso =  int(input("\nNivel de acceso (1-5): \n"))
departamento = input("\nDepartamento: \n")
autorización = input ("\n¿Tiene autorización especial vigente? (sí/no): \n")
hora_ingreso = int(input("\nHora de ingreso (0-23): \n"))

en_horario =  (hora_ingreso >= 8 and hora_ingreso <= 20)

# Fase 3 Regla de nivel máximo y atorización especial

if nivel_acceso == 5 or autorización == "sí":
    if en_horario:
        print(f"Acceso concedido - EMPLEADO: {empleado_id} área completa\n")
    else:
        print(f"Acceso fuera de horario - EMPLEADO: {empleado_id} acceso completo con registro de alerta\n")

# Fase 4: Acceso restringido por nivel y departamento
elif nivel_acceso >= 3 and en_horario:
    depto_critico = departamento == "Tecnología" or departamento == "Finanzas" or departamento == "Dirección"
    if depto_critico:
        print(f"ACCESO CONCEDIDO — Empleado {empleado_id}: área restringida ({departamento}).\n")
    else:
        print(f"ACCESO PARCIAL — Empleado {empleado_id}: área general solamente (departamento sin permisos ampliados).\n")

# Fase 5: Aceso general y denegación
elif nivel_acceso >= 2 and en_horario:
    print(f"ACCESO CONCEDIDO — Empleado {empleado_id}: área general")

#Fase 6: Denegaciones
elif not en_horario:
    print(f"ACCESO DENEGADO - Empleado: {empleado_id} - Fuera de horario laboral")
else:
    print(f"ACCESO DENEGADO - Empleado: {empleado_id} - Nivel de acceso insuficiente\n")