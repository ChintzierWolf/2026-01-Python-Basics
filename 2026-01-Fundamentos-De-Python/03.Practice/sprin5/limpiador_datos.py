# Limpiador de Datos de Usuario

print("=== SISTEMA DE LIMPIEZA DE DATOS ===\n")

# TODO 1: Crea 4 variables con datos "sucios" tal como llegarían de un
# formulario (con espacios sobrantes, mayúsculas o guiones):
#   nombre_sucio, email_sucio, telefono_sucio, mensaje_sucio.
# Imprime "--- DATOS ORIGINALES ---" y muéstralas entre comillas.

# TODO 2: Limpia cada dato y guárdalo en una variable nueva:
#   - nombre:   .strip().title()
#   - email:    .strip().lower()
#   - telefono: .replace("-", "")
#   - mensaje:  .strip().capitalize()
# Imprime "--- DATOS LIMPIOS ---" y muestra los resultados.

# TODO 3: Imprime "--- VALIDACIONES ---".
# Valida el email: comprueba que contiene "@" (con 'in') y que
# termina en ".com" (con .endswith()). Imprime ✅ o ❌.

# TODO 4: Valida el teléfono: debe tener 10 caracteres (len()) y ser
# todo dígitos (.isdigit()). Imprime ✅ o ❌.

# TODO 5: Divide el mensaje en palabras con .split() e imprime cuántas
# palabras tiene usando len().

# TODO 6: Separa el nombre completo con .split(). Si tiene 2 o más partes,
# toma la primera como primer_nombre y une el resto con " ".join() como
# apellido. Imprime ambos.

# TODO 7: Genera un username con email_limpio.split("@")[0] e imprímelo.

# TODO 1
nombre_sucio = "   josÉ áNGeL   GARCÍa LOPEZ   "
email_sucio = "email.address@mail.mx   "
telefono_sucio = "123-456-7890"
mensaje_sucio = "   hola, me gustaria recibir mas informacion    "

print("--- DATOS ORIGINALES ---")
print(f'Nombre: "{nombre_sucio}"')
print(f'Email: "{email_sucio}"')
print(f'Teléfono: "{telefono_sucio}"')
print(f'Mensaje: "{mensaje_sucio}"')

# TODO 2
nombre_limpio = nombre_sucio.strip().title()
email_limpio = email_sucio.strip().lower()
telefono_limpio = telefono_sucio.replace("-", "")
mensaje_limpio = mensaje_sucio.strip().capitalize()

print("\n--- DATOS LIMPIOS ---")
print(f'Nombre: "{nombre_limpio}"')
print(f'Email: "{email_limpio}"')
print(f'Teléfono: "{telefono_limpio}"')
print(f'Mensaje: "{mensaje_limpio}"')

# TODO 3
print("\n--- VALIDACIONES ---")
if "@" in email_limpio and email_limpio.endswith(".com"):
    print(f'El {email_limpio} es correcto ✅, contiene "@" y termina en ".com"')
else:
    print(f'El {email_limpio} es incorrecto ❌, no contiene "@" o no termina en ".com"')

# TODO 4
if len(telefono_limpio) == 10 and telefono_limpio.isdigit():
    print(f'El {telefono_limpio} es correcto ✅, tiene 10 caracteres y es un número')
else:
    print(f'El {telefono_limpio} es incorrecto ❌, no tiene 10 caracteres o no es un número')

# TODO 5
print("\n--- MENSAJE ---")
print(f'Mensaje limpio: {mensaje_limpio}')
print(f'El mensaje tiene: {len(mensaje_limpio.split())} palabras')

# TODO 6
print("\n--- NOMBRE ---")
nombre_partes = nombre_limpio.split()
if len(nombre_partes) >= 2:
    primer_nombre = " ".join(nombre_partes[:1])
    apellido = " ".join(nombre_partes[2:])
    print(f'Primer nombre: "{primer_nombre}"')
    print(f'Apellido: "{apellido}"')
else:
    print(f'Nombre completo: "{nombre_limpio}"')

# TODO 7
print("\n--- USERNAME ---")
username = email_limpio.split("@")[0]
print(f'Username: "{username}"')