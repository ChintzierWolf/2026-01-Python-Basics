# GESTOR DE TAREAS — SonidoLibre
# Organiza las tareas del festival con listas, tuplas y una función de reporte.
# Más adelante (Video C) esto crece a un menú while True con opciones 1 a 6;
# por ahora construye las piezas en orden con los TODOs.

# TODO 1: Crea una lista con al menos 5 tareas pendientes.
# Ejemplo: "montar escenario principal", "revisar sistema de sonido", etc.

# TODO 2: Crea una tupla con la configuración del festival:
# nombre, año, capacidad máxima, ciudad.

# TODO 3: Imprime la configuración del festival usando tuple unpacking.
# Formato: "Festival: [nombre] [año] | Capacidad: [cap] | Ciudad: [ciudad]"

# TODO 4: Agrega 2 tareas nuevas con append().
# Luego elimina la primera con pop(0).

# TODO 5: Imprime la lista de tareas ordenada alfabéticamente usando sorted().
# Verifica que la lista original NO cambió después de sorted().

# TODO 6: Define una función llamada 'mostrar_reporte' que no reciba parámetros.
# Dentro de la función, imprime el total de tareas y cada tarea con "→ ".
# Llama a la función al final.

# TODO 1:
tareas = ['montar escenario principal', 'revisar sistema de sonido', 'comprar bebidas', 'preparar comida', 'organizar equipo de sonido', 'decorar el lugar']

# TODO 2:
configuracion_festival = ('SonidoLibre', 2025, 5000, 'Bogotá')

# TODO 3:
nombre, año, capacidad, ciudad = configuracion_festival
print(f"\nFestival: {nombre} {año} | Capacidad: {capacidad} | Ciudad: {ciudad}")

# TODO 4:
tareas.append('limpiar área del evento')
tareas.append('coordinar acceso VIP')

tareas.pop(0)

# TODO 5:
tareas_ordenadas = sorted(tareas)
print(f"\nLista ordenada de tareas: {tareas_ordenadas}")
print(f"Lista original de tareas: {tareas}")

# TODO 6:
def mostrar_reporte():
    print(f"\nTotal de tareas: {len(tareas)}")
    for tarea in tareas:
        print(f"→ {tarea}")
    
mostrar_reporte()


