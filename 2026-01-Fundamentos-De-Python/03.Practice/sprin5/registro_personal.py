# REGISTRO DE PERSONAL — directorio de empleados como lista de diccionarios
# La lista da el orden; cada diccionario es un expediente con campos rotulados.

# TODO 1: Crea la lista vacia que contendra a todos los empleados.
# CUIDADO: debe vivir FUERA del bucle de alta. Si la creas dentro,
# se reinicia en cada vuelta y solo guardas al ultimo empleado.

# ── OPERACION 1: ALTA con input() y casting ──────────────────
# TODO 2: Usa un while que repita mientras el usuario responda "si".
# En cada vuelta pide los cuatro datos con input() y castea:
#   - nombre          -> texto (input directo)
#   - departamento    -> texto (input directo)
#   - salario_mensual -> float(input(...))   # llega como texto, debe ser numero
#   - nivel_acceso    -> int(input(...))      # nivel 1-5
# Arma el diccionario con esas 4 claves y agregalo COMPLETO con .append().
# Al final de cada vuelta pregunta: "Agregar otro empleado? (si/no): "

# ── OPERACION 2: LISTADO numerado con caso vacio ─────────────
# TODO 3: Imprime "=== DIRECTORIO DE EMPLEADOS ===".
# Si la lista esta vacia, avisa "No hay empleados registrados.".
# Si no, recorre con un for por fuera (lleva un contador "numero")
# y un for con .items() por dentro para imprimir cada campo.

# ── OPERACION 3: BUSQUEDA por nombre con guardia anti-KeyError ─
# TODO 4: Pide un nombre con input() y una bandera encontrado = False.
# Recorre el registro; usa la guardia:
#   if "nombre" in empleado and empleado["nombre"] == buscado:
# para no reventar si algun expediente viene incompleto.
# Si lo encuentras, imprime su expediente con .items() y pon encontrado = True.
# Si al terminar el for la bandera sigue en False, imprime "Empleado no encontrado.".


#TODO 1
empleados = [ ]

# ── OPERACION 1: ALTA con input() y casting ──────────────────
#TODO 2
while True:
    nombre = input("Ingrese el nombre del empleado: ").strip()
    departamento = input("Ingrese el departamento del empleado: ").strip()
    salario_mensual = float(input("Ingrese el salario mensual del empleado: ").strip())
    nivel_acceso = int(input("Ingrese el nivel de acceso del empleado: ").strip())
    empleados.append({
        "nombre": nombre,
        "departamento": departamento,
        "salario_mensual": salario_mensual,
        "nivel_acceso": nivel_acceso
    })
    respuesta = input("¿Desea agregar otro empleado? (si/no): ").strip().lower()
    if respuesta != "si":
        break

# ── OPERACION 2: LISTADO numerado con caso vacio ─────────────
# TODO 3
print("\n === DIRECTORIO DE EMPLEADOS ===")

if len(empleados) == 0:
    print("No hay empleados registrados.")
else:
    numero = 1
    for empleado in empleados:
        print(f"\n Empleado #{numero} ")
        for clave, valor in empleado.items():
            print(f" {clave} : {valor}")
        numero += 1

# ── OPERACION 3: BUSQUEDA por nombre con guardia anti-KeyError ─
# TODO 4
bus_nombre = input("Ingrese el nombre del empleado a buscar: ").strip()
encontrado = False

for empleado in empleados:
    if "nombre" in empleado and empleado["nombre"] == busc_nombre:
        print(f"\n Empleado encontrado: ")
        for clave, valor in empleado.items():
            print(f" {clave} : {valor}")
        encontrado = True
        break

if not encontrado:
    print("Empleado no encontrado.")