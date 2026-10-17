# INVENTARIO DINÁMICO

# TODO 1: Crea una variable 'inventario' que sea una lista vacía.

# TODO 2: Imprime un encabezado, por ejemplo "=== Inventario Dinámico ===".

# TODO 3: Usa .append() tres veces seguidas para agregar:
#   "Laptop", "Mouse", "Teclado" (en ese orden).
# Imprime la lista después: "Inventario actual: [valor]".

# TODO 4: Usa .insert(0, "Monitor") para agregar "Monitor" en la PRIMERA
# posición de la lista. Imprime la lista para verificar.

# TODO 5: Usa .pop() (sin argumentos) para eliminar el ÚLTIMO elemento
# y guarda lo que devuelva en una variable 'ultimo'.
# Imprime qué se eliminó y cómo quedó la lista.

# TODO 6: Usa .remove("Mouse") para quitar el "Mouse" por su nombre
# (no por posición). Imprime la lista resultante.

# TODO 7: Imprime el total de productos restantes usando len(inventario).

# TODO 8: Recorre la lista con un bucle 'for producto in inventario:'
# e imprime cada producto en su propia línea con un prefijo "- ".

inventario = []

while True:
    
    print("\n=== INVENTARIO DINÁMICO ===")
    print("1. Agregar nuevo producto")
    print("2. Ver todos los productos")
    print("3. Insertar un producto al inicio")
    print("4. Eliminar el ultimo producto")
    print("5. Eliminar un producto por su nombre")
    print("6. Salir\n")

    opcion = input("Elija una opcion (1-6): ")

    if opcion == "1":
        producto = input("Ingrese el producto que desea agregar: ")
        inventario.append(producto)
        print(f"Producto {producto} agregado exitosamente")
        
    elif opcion == "2":
        if len(inventario) == 0:
            print("No hay productos")
        else:
            print(inventario)

    elif opcion == "3":
        producto = input("Ingrese el producto: ")
        inventario.insert(0, producto)
        print(f"Producto {producto} agregado al inicio")
        
    elif opcion == "4":
        if len(inventario) == 0:
            print("No hay productos")
        else:
            producto = inventario.pop()
            print(f"Producto eliminado: {producto}")

    elif opcion == "5":
        producto = input("Ingrese el producto a eliminar: ")
        if producto in inventario:
            inventario.remove(producto)
            print(f"Producto {producto} eliminado exitosamente.")
        else:
            print(f"El producto {producto} no existe en el inventario.")

    elif opcion == "6":
        print("Usted salio del programa")
        break

    else:
        print("Opcion invalida.")

print("\n===== INVENTARIO FINAL =====")
for i, producto in enumerate(inventario):
    print(f"{i + 1}. {producto}")

print("Total de productos: ", len(inventario))