def pedir_vehiculos():
    marca       = input("Ingrese la marca del vehiculo           : ")
    modelo      = input("Ingrese el modelo del vehiculo          : ")
    anio        = input("Ingrese el anio del vehiculo            : ")
    kilometraje = int(input("Ingrese los kilometros del vehiculo : "))

    return marca, modelo, anio, kilometraje

def registrar_vehivulo(flota, marca, modelo, anio, kilometraje):
    vehiculo = {
        "marca": marca,
        "modelo": modelo,
        "anio": anio,
        "kilometraje": kilometraje
    }

    flota.append(vehiculo)
    print(f"\n>>>>>Vehiculo {marca} {modelo} agregado exitosamente!\\n")

flota = []

marca, modelo, anio, kilometraje = pedir_vehiculos()
registrar_vehivulo(flota, marca, modelo, anio, kilometraje)

print(f"La flota actual es: {flota}")