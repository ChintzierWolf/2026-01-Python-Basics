# Ejemplo 1

# folio = "RC-2026-0042"
# prin(folio[3:7])
# Imprimel año del folio que es: 2026

# Ejemplo 2

# nombre = "ana"
# nombre[0] = "A"
# print(nombre)

# Imprime error porque las cadenas de caracteres son inmutables

# Ejemplo 3

# nombre = "ana"
# nombre = nombre[0].capitalize() + nombre[1:]

# Imprime el string con resultado de Ana, ya que se le está asignando a la variable un nuevo string con la primera letra en mayúsculas.

# Ejemplo 4

# nombre1 = "ana"
# nombre1 = nombre1.title()
# print(nombre1)

# Ejemplo 5

# nombre2 = "ana"
# print(nombre2.title())

"""
# Ejemplo 6

nombre_sucio = "    ana torres    "
email_sucio = " ANA.Torres@Inadaptados.MX"
area_sucia = "finanzas"
habilidades_raw = "Python, Base de datos   , Analítica, Excel,     Macros"

nombre = nombre_sucio.strip()
print(f"[{nombre}]")

nombre = nombre.replace("   ", " ")
nombre = nombre.title()

print(f"[{nombre}]")

email = email_sucio.strip().lower()

print(email)

area = area_sucia.strip().lower()
print(area)

partes = habilidades_raw.split(",")
print(partes)

partes_limpias = []

for h in partes:
    partes_limpias.append(h.strip().lower())

print(partes_limpias)

habilidades = (", ".join(partes_limpias))
print(habilidades)
"""

base_reclutas = [
    {
        "nombre" : "Ana Torres",
        "area" : "Finanzas",
        "salario_mensual" : 28500.0
    },
    {
        "nombre" : "Luis Quintero",
        "area" : "Logística",
        "salario_mensual" : 19200.0
    },
    {
        "nombre" : "María Ibarra",
        "area" : "Salud",
        "salario_mensual" : 133750.0
    }
]

for recluta in base_reclutas:
    print(f"\nNombre: {recluta.get('nombre')}, Área: {recluta.get('area')}, Salario Mensual: {recluta.get('salario_mensual')}\n")

print(f"{'NOMBRE':<18}{'AREA':<12}{'SALARIO':>12}")
print("-" * 43)

for recluta in base_reclutas:
    print(f"\n{recluta["nombre"][:14]:<18}{recluta["area"]:<12}{recluta["salario_mensual"]:>12,.2f}")