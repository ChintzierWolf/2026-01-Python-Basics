# Funciones

# Función que pide al usuario los datos del vehiculo
def pedir_vehiculos():
    marca       = input("Ingrese la marca del vehiculo           : ")
    modelo      = input("Ingrese el modelo del vehiculo          : ")
    anio        = input("Ingrese el anio del vehiculo            : ")
    kilometraje = int(input("Ingrese los kilometros del vehiculo : "))

    return marca, modelo, anio, kilometraje

# Función que registra el vehiculo
def registrar_vehivulo(flota, marca, modelo, anio, kilometraje):
    vehiculo = {
        "marca": marca,
        "modelo": modelo,
        "anio": anio,
        "kilometraje": kilometraje
    }

    flota.append(vehiculo)
    # .append() sirve para agregar un elemento a una lista y .pop() sirve para quitar un elemento a una lista.
    print(f"\n>>>>>Vehiculo {marca} {modelo} agregado exitosamente!\\n")

# Programa principal
flota = []

marca, modelo, anio, kilometraje = pedir_vehiculos()
registrar_vehivulo(flota, marca, modelo, anio, kilometraje)

print(f"La flota actual es: {flota}")