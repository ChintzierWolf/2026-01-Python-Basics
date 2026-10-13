lista = []
print(lista)

while True:

    opcion = input("A)gregar", "I)nsertar", "E)liminar", "B)orrar de lalista", "R)emover por valor", "S)alir")

    if opcion == "A":
        lista.append(input("Agregar elemento: "))
        print(lista)
    elif opcion == "I":
        lista.insert(int(input("Posicion a insertar: ")), input("Elemento a insertar: "))
        print(lista)
    elif opcion == "E":
        lista.pop(int(input("Posicion a eliminar: ")))
        print(lista)
    elif opcion == "B":
        lista.clear()
        print(lista)
    elif opcion == "R":
        lista.remove(input("Elemento a eliminar: "))
        print(lista)
    elif opcion == "S":
        break
