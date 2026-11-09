# Formulario de Registro - Sprint 5 Práctica

print("=== FORMULARIO DE REGISTRO DE RECLUTA ===\n")

datos_sucios = {
  "nombre": "  CARLOS   RUIZ  ",
  "email": "  CARLOS.RUIZ@EXAMPLE.COM  ",
  "telefono": "555-123-4567",
  "edad": "25",
  "ciudad": "madrid"
}

print("--- DATOS RECIBIDOS (SUCIOS) ---")
for campo, valor in datos_sucios.items():
  print(f"{campo}: '{valor}'")

# TODO 1: Crea un diccionario vacío 'datos_limpios' y limpia cada campo:
#   - nombre: .strip(), luego .split() y " ".join() para quitar espacios dobles,
#             luego .title()
#   - email: .strip().lower()
#   - telefono: elimina "-", "(", ")", ".", " " con .replace() (uno por uno)
#   - edad: .strip()
#   - ciudad: .strip().title()
# Imprime datos_limpios con el mismo formato de arriba.


# TODO 2: Crea una lista vacía 'errores' y valida cada campo:
#   - nombre: len(datos_limpios["nombre"].split()) < 2 → error "Nombre debe incluir apellido"
#   - email: debe contener "@" y "." en el dominio → error si no
#   - telefono: .isdigit() y len() == 10 → error si no
#   - edad: .isdigit() → si pasa, convierte a int y verifica 18 <= edad <= 100
# Por cada campo que pase, imprime "✅ [campo] válido".
# Por cada campo que no pase, agrega el mensaje de error a 'errores'.


# TODO 3: Si 'errores' está vacío, imprime "--- REGISTRO EXITOSO ---"
# y muestra cada campo (nombre a la izquierda en 15 chars, valor en 30 chars).
# Formatea también el teléfono como "(555) 123-4567" usando slicing.
# Si hay errores, imprime "--- REGISTRO RECHAZADO ---" y lista cada error.

datos_limpios = {}

datos_limpios["nombre"] = datos_sucios["nombre"].strip().split()
datos_limpios["nombre"] = " ".join(datos_limpios["nombre"]).title()
datos_limpios["email"] = datos_sucios["email"].strip().lower()
datos_limpios["telefono"] = datos_sucios["telefono"].replace("-", "").replace("(", "").replace(")", "").replace(".", "").replace(" ", "")
datos_limpios["edad"] = datos_sucios["edad"].strip()
datos_limpios["ciudad"] = datos_sucios["ciudad"].strip().title()

print("\n--- DATOS LIMPIOS ---")
for campo, valor in datos_limpios.items():
    print(f"{campo}: '{valor}'")

# TODO 2: Crea una lista vacía 'errores' y valida cada campo:
errores = []

# Validar nombre
if len(datos_limpios["nombre"].split()) >= 2:
    print("✅ nombre válido")
else:
    errores.append("Nombre debe incluir apellido")

# Validar email
if "@" in datos_limpios["email"] and "." in datos_limpios["email"].split("@")[-1]:
    print("✅ email válido")
else:
    errores.append("Email debe contener '@' y '.' en el dominio")

# Validar teléfono
if datos_limpios["telefono"].isdigit() and len(datos_limpios["telefono"]) == 10:
    print("✅ telefono válido")
else:
    errores.append("Teléfono debe tener 10 dígitos")

# Validar edad
if datos_limpios["edad"].isdigit() and 18 <= int(datos_limpios["edad"]) <= 100:
    print("✅ edad válida")
else:
    errores.append("Edad debe ser un número entre 18 y 100")


# TODO 3: Decisión según la lista de errores
if len(errores) == 0:
    print("\n--- REGISTRO EXITOSO ---")
    
    # Formatear el teléfono con slicing
    tel = datos_limpios["telefono"]
    telefono_formateado = f"({tel[:3]}) {tel[3:6]}-{tel[6:]}"
    
    for campo, valor in datos_limpios.items():
        valor_mostrar = telefono_formateado if campo == "telefono" else valor
        print(f"{campo:<15}{str(valor_mostrar):<30}")
else:
    print("\n--- REGISTRO RECHAZADO ---")
    for error in errores:
        print(f"❌ {error}")