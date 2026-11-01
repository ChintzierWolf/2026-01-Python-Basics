"""
# BUG 1 Reporte de Npimnia que se detiene a media lista

empleados = [
    {"nombre": "Ana", "salario_mensual": 50000},
    {"nombre": "Luis", "salario_mensual": 60000},
    {"nombre": "Carlos"},
    {"nombre": "Maria", "salario_mensual": 70000}
]

for empleado in empleados:
    print(f"{empleado['nombre']}: deposita $: {empleado['salario_mensual']}")
"""

"""
# BUG 2: El in que busca en el lugar equivocado

empleado = {
    "nombre": "Ana Garcia",
    "departamento": "Finanzas",
    "nivel_acceso": "4"
}

if "Finanzas" in empleado:
    print("Ana pertenece a Finanzas - Acecso a reportes financieros")
else:
    print("Ana NO pertenece a Finanzas - Acceso denegado")
"""
"""
# BUG 3: La clave duplicada que borra un dato en silencio
config = {
    "nombre": "Ana Garcia",
    "nivel_acceso": "2",
    "departamento": "Finanzas",
    "nivel_acceso": "5"
}

print(f"Nivel de acceso asignado a {config['nombre']}: {config['nivel_acceso']}")
"""
"""
# BUG 4: El diccionario que parece lista

usuarios_activos = {
    "Ana": "activo",
    "Luis": "inactivo",
    "Carlos": "activo",
    "Maria": "inactivo"
}

for usuario in usuarios_activos:
    if usuarios_activos[usuario] == "activo":
        print(f"Enviar correo de recordatorio a {usuario}")
"""
"""
# BUG 5: El diccionario que "olvida" a sus hijos

inventario = {
    "manzanas": {
        "cantidad": 200,
        "precio": 100
    },
    "peras": {
        "cantidad": 150,
        "precio": 150
    }
}

fruta = "manzanas"
print(inventario[fruta]["cantidad"])
"""