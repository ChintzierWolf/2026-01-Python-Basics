incidentes = [
            "TKT-101: red caida en el piso 3", 
            "TKT-102: Impresora sin toner", 
            "TKT-103: usuario sin acceso a CRM", 
            "TKT-104: Solicitud de licencia de software"]

# -------- Paso 1: .append() y su trampa --------
print("\n" + "="*30)
print("Paso 1: .append() y su trampa")
print("="*30 + "\n")

incidentes.append("TKT-105: VPN Intermitente")
print(incidentes)
print(f"La cantidad de incidentes es: {len(incidentes)}")

resultado = incidentes.append("TKT-106: Reinicio de Router")
print(f"El resultado del append es: {resultado}")
print(incidentes)

# -------- Paso 2: .insert() para urgencias --------
print("\n" + "="*30)
print("Paso 2: .insert() para urgencias")
print("="*30 + "\n")

incidentes.insert(0, "TKT-URGENT: Caída total del servidor")
print(incidentes[0])
print(f"Lista actualizada de incidentes despues de insertar: {incidentes}")
print(f"Total de incidentes despues de insertar: {len(incidentes)}")

# -------- Paso 3: .pop() con posición humana --------
print("\n" + "="*30)
print("Paso 3: .pop()")
print("="*30 + "\n")

cerrado = incidentes.pop()

print(f"Incidente cerrado: {cerrado}")

print("\n" + "="*30)
print("Paso 3: .pop() con posición humana")
print("="*30 + "\n")

pos_humana = 3

if 1 <= pos_humana <= len(incidentes):
    cerrado = incidentes.pop(pos_humana-1)
    print(f"Incidente cerrado en posición: {pos_humana} - {cerrado}")
    print(f"Lista actualizada: {incidentes}")
    print(f"Total de incidentes despues de pop: {len(incidentes)}")
else:
    print(f"Posición inválida para cerrar: {pos_humana}. Intenta de nuevo.")

# -------- Paso 4: .remove() vs .pop() ----------
# (reset de lista demo aislada de remove) 
incidentes = [
            "TKT-101: red caida en el piso 3",
            "TKT-103: usuario sin acceso a CRM", 
            "TKT-104: Solicitud de licencia de software"]

print("\n" + "="*30)
print("Paso 4: .remove() vs .pop() ")
print("="*30 + "\n")

incidentes.remove("TKT-103: usuario sin acceso a CRM")

print(f"Lista actualizada: {incidentes}")
print(f"Total de incidentes despues de remove: {len(incidentes)}")

# -------- Paso 5: in  como guardia universal ----------
print("\n" + "="*30)
print("Paso 5: in  como guardia universal")
print("="*30 + "\n")

incidentes = [
            "TKT-101: red caida en el piso 3",
            "TKT-104: Solicitud de licencia de software"]

consulta = "TKT-101: red caida en el piso 3"

if consulta in incidentes:
    print(f"Incidente encontrado: {consulta}")
    incidentes.remove(consulta)
    print(f"Lista actualizada: {incidentes}")
    print(f"Total de incidentes: {len(incidentes)}")
else:
    print(f"Incidente no encontrado: {consulta}")
    print(f"Lista de incidentes actual: {incidentes}")
    print(f"Total de incidentes: {len(incidentes)}")

# -------- Paso 6: .pop() con índice negativo ----------
print("\n" + "="*30)
print("Paso 6: .pop() con índice negativo")
print("="*30 + "\n")

incidente_urgente = incidentes.pop(-1)
print(f"Incidente eliminado desde el final: {incidente_urgente}")
print(f"Lista actualizada: {incidentes}")
print(f"Total de incidentes despues de pop: {len(incidentes)}")

# -------- Paso 7: .sort() para urgencias ----------
print("\n" + "="*30)
print("Paso 7: .sort() para urgencias")
print("="*30 + "\n")

incidentes.sort()
print(f"Lista ordenada: {incidentes}")