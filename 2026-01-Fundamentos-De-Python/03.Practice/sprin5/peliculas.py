titulo = "  the dark knight   "
generos = "Accion,Drama,Crimen"
resena = "Una obra maestra absoluta del cine moderno. Sin duda, la mejor"

titulo = titulo.strip().title()
generos = generos.split(",")
resena = resena.replace(". Sin duda, ", ", ")

generos_mostrar = " / ".join(generos)

print(titulo)
print(generos)
print(resena)
print(generos_mostrar)

codigo = "PEL-2008-TDK"

prefijo = codigo[0:3]
año = codigo[4:8]
id = codigo[9:]

print(prefijo)
print(año)
print(id)

print(codigo[-3:])