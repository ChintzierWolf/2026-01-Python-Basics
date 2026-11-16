# Sistema de Login con Validación Total

# TODO 1: Define obtener_usuario(): con un while True pide
# input("Usuario (min 3 caracteres): ").strip() y valida:
#   - Si tiene menos de 3 caracteres → imprime error y continue.
#   - Si contiene espacios (" " in usuario) → imprime error y continue.
#   - Si pasa ambos filtros → return usuario.

def obtener_usuario():
    while True:
        usuario = input("Usuario (min 3 caracteres): ").strip()
        if len(usuario) < 3:
            print("Error: El usuario debe tener al menos 3 caracteres.")
        elif " " in usuario:
            print("Error: El usuario no puede contener espacios.")
        else:
            return usuario

# TODO 2: Define obtener_edad() con el patrón try/except/else:
#   - try: convierte input("Edad (13-100): ") con int().
#   - except ValueError: imprime "❌ La edad debe ser un número" y continue.
#   - else: si edad < 13 o edad > 100 imprime el error correspondiente;
#     si es válida, return edad.

def obtener_edad():
    while True:
        try:
            edad = int(input("Edad (13-100): "))
        except ValueError:
            print("❌ La edad debe ser un número.")
            continue
        else:
            if edad < 13 or edad > 100:
                print("Error: La edad debe estar entre 13 y 100 años.")
            else:
                return edad

# TODO 3: Define obtener_email(): pide el email con .strip() y valida que
# contenga "@" y "." — si no, imprime error y vuelve a pedir; si sí, return.

def obtener_email():
    while True:
        email = input("Email: ").strip()
        if "@" not in email or "." not in email:
            print("Error: El email debe contener '@' y '.'")
        else:
            return email

# TODO 4: Define crear_cuenta() usando try/except/else/finally:
#   - try: llama a las tres funciones anteriores imprimiendo un ✅ por cada dato.
#   - except KeyboardInterrupt: avisa que se canceló el registro y return None.
#   - else: arma el diccionario cuenta con "usuario", "edad" y "email",
#     imprime "🎉 ¡Cuenta creada exitosamente!" y devuélvelo.
#   - finally: imprime "--- Proceso de registro finalizado ---" (SIEMPRE corre).

def crear_cuenta():
    try:
        usuario = obtener_usuario()
        print("✅ Usuario válido")
        edad = obtener_edad()
        print("✅ Edad válida")
        email = obtener_email()
        print("✅ Email válido")
    except KeyboardInterrupt:
        print("\nSe canceló el registro.")
        return None
    else:
        cuenta = {
            "usuario": usuario,
            "edad": edad,
            "email": email
        }
        print("🎉 ¡Cuenta creada exitosamente!")
        return cuenta
    finally:
        print("--- Proceso de registro finalizado ---")

# TODO 5: Llama crear_cuenta(), guarda el resultado y:
#   - Si hay cuenta → imprime sus datos.
#   - Si es None → imprime "No se creó ninguna cuenta".

cuenta = crear_cuenta()
if cuenta:
    print("Datos de la cuenta:")
    print(cuenta)
else:
    print("No se creó ninguna cuenta.")

# Tu código implementa correctamente la mayoría de la funcionalidad, 
# pero tiene un problema crítico en obtener_edad(): 
# el bloque else no tiene un while True envolvente, 
# así que si el usuario ingresa una edad fuera del rango 13-100, imprime el error pero no vuelve a pedir.
# Además, en crear_cuenta() falta imprimir los ✅ por cada dato validado como pide el TODO 4. 
# Estos fallos impiden que el sistema funcione como se especificó.