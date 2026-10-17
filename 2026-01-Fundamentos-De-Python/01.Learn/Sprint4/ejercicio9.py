medallas = ("Oro", "Plata", "Bronce")

natacion = ['Alicia', 'Leo', 'Julian', 'Martha', 'Maria', 'Alan']

corredores = ['Ana', 'Beto', 'Carlos', 'Dani', 'Elena', 'Juan']

salto = ['Rodrigo', 'Diego', 'Valeria', 'Beatriz', 'Alex', 'Gustavo']

ganadores_corredores = corredores[0:3]
ganadores_natacion = natacion[:3]
ganadores_salto = salto[0:3]

print("\n =========PODIUM DE CORREDORES========\n")
print("========================================\n")

for i in range(3):
    print(f"{i+1}. {ganadores_corredores[i]} ({medallas[i]})")

print("\n =========PODIUM DE NATACION========\n")
print("========================================\n")

for i in range(3):
    print(f"{i+1}. {ganadores_natacion[i]} ({medallas[i]})")

print("\n =========PODIUM DE SALTO========\n")
print("========================================\n")

for i in range(3):
    print(f"{i+1}. {ganadores_salto[i]} ({medallas[i]})")

print("\n")