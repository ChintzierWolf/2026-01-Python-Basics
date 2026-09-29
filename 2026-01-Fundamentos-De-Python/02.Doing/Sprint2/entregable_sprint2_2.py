# ENTREGABLE SPRINT 2: EL GUARDIÁN DE SONIDOLIBRE

print("=== SISTEMA DE ACCESO — SONIDOLIBRE 2026 ===")

# TODO 1: Crea dos variables con las credenciales fijas del sistema.
# Llámalas 'usuario_correcto' y 'password_correcto'.
# Valores: "admin" y "sonido2026"

# TODO 2: Usa input() para pedir el usuario.
# Guárdalo en una variable llamada 'usuario_ingresado'.

# TODO 3: Usa input() para pedir la contraseña.
# Guárdala en una variable llamada 'password_ingresado'.

# TODO 4: Escribe un if que verifique si usuario_ingresado == usuario_correcto
# AND password_ingresado == password_correcto.
# Dentro de ese bloque:

  # TODO 5: Usa input() para pedir el rol.
  # Guárdalo en una variable llamada 'rol'.
  # Los valores posibles son: "admin" o "staff"

  # TODO 6: Escribe un if/else dentro del bloque anterior que:
  # - Si rol es "admin": imprima "Acceso total concedido. Bienvenido al panel de control."
  # - Si no: imprima "Acceso estándar concedido. Bienvenido, staff de SonidoLibre."

# TODO 7: Fuera del if principal (pegado a la izquierda), escribe un else.
# Dentro, usa if/else para distinguir si el error fue el usuario o la contraseña:
# - Si usuario_ingresado != usuario_correcto: imprima "Usuario no reconocido."
# - Si no: imprima "Contraseña incorrecta. Verifica tus datos."

usuario_correcto = "admin"
password_correcto = "sonido2026"

usuario_ingresado = input("Usuario: ")
password_ingresado = input("Contraseña: ")

if usuario_ingresado == usuario_correcto and password_ingresado == password_correcto:
    rol = input("Rol: ")
    if rol == "admin":
        print("Acceso total concedido. Bienvenido al panel de control.")
    else:
        print("Acceso estándar concedido. Bienvenido, staff de SonidoLibre.")
else:
    if usuario_ingresado != usuario_correcto:
        print("Usuario no reconocido.")
    else:
        print("Contraseña incorrecta. Verifica tus datos.")
