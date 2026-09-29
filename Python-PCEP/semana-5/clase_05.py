"""
# Sistema de auditoría - asignar folios consecutivos a los documentos

ultimo_folio_asignado = 0

for folio in range(1, 100):
    ultimo_folio_asignado = folio


print(f"Último folio asignado: {ultimo_folio_asignado}")
print("Auditoria cerrada con 100 folios procesados.")
"""
print("\nprimer for: de 0 a 9\n")
for x in range (10):
    print(x)

print("\nsegundo for: de 1 a 100 con paso de 2\n")
for n in range (1, 101, 2):
    print(n)

print("\ntercer for: de 10 a 1 con paso de -1\n")
for m in range (10, 0, -1):
    print(m)