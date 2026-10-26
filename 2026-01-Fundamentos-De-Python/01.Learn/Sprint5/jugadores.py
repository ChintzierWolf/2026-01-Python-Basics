jugador = {
    "nombre": "Link",
    "juego": "The Legend of Zelda",
    "puntos": 42,
    "activo": True
}

# Acceder a los valores
print("====== Valores Disponibles ======")
print("Nombre: ", jugador["nombre"])
print("Juego: ", jugador["juego"])
print("Puntos: ", jugador["puntos"])
print("¿Está activo?: ", jugador["activo"])

# Acceder a los valores con f-strings
print("====== Valores Disponibles con f-strings ======")
print(f"Nombre: {jugador['nombre']}")
print(f"Juego: {jugador['juego']}")
print(f"Puntos: {jugador['puntos']}")
print(f"¿Está activo?: {jugador['activo']}")

# Otra forma de acceder a los valores
print("====== Valores Disponibles con .get() ======")
print("Nombre: ", jugador.get("nombre"))
print("Juego: ", jugador.get("juego"))
print("Puntos: ", jugador.get("puntos"))
print("¿Está activo?: ", jugador.get("activo"))

# Iterar sobre las claves, sirve para obtener las etiquetas
for clave in jugador.keys():
    print(clave)

print("====== Valores Disponibles ======")

# Iterar sobre los valores, sirve para obtener los valores de esas etiquetas
for valor in jugador.values():
    print(valor)

print("====== Etiquetas Disponibles ======")
for clave in jugador.keys():
    print(clave)

print("====== Etiquetas y Valores Disponibles ======")

# Iterar sobre las claves y valores, sirve para obtener las etiquetas y los valores
for clave, valor in jugador.items():
    print(clave, valor)

# Acceder a los valores con f-strings, sirve para obtener las etiquetas y los valores con f-strings
for clave, valor in jugador.items():
    print(f"{clave}: {valor}")

jugadores = [
    {
        "nombre": "Link",
        "juego": "The Legend of Zelda",
        "puntos": 42,
        "activo": True
    },
    {
        "nombre": "Mario",
        "juego": "Super Mario Bros",
        "puntos": 100,
        "activo": True
    },
    {
        "nombre": "Luigi",
        "juego": "Super Mario Bros",
        "puntos": 69,
        "activo": True
    },
    {
        "nombre": "Peach",
        "juego": "Super Mario Bros",
        "puntos": 84,
        "activo": True
    },
    {
        "nombre": "Yoshi",
        "juego": "Super Mario Bros",
        "puntos": 92,
        "activo": True
    }
]

print("====== Diccionario dentro de una Lista ======")
print(jugadores)

print("====== Lista dentro de un Diccionario ======")

jugador = {
    "nombre": "Link",
    "juego": "The Legend of Zelda",
    "puntos": 42,
    "activo": True
}

print(jugador)