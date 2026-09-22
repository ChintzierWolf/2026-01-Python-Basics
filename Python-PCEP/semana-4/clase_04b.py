# EL sistemma para que:
# Salario > 50,000 sea Nivel A (20% de bono)
# Salario > 35,000 sea Nivel B (15% de bono)
# Salario > 15,000 sea Nivel C (10% de bono)
# Y cualquier otro sea Junior (5% de bono)

salario = float(input("Ingrese el salario mensual bruto ($): "))

if salario > 50000:
    categoria = "Nivel A - Directivo"
    bono = salario * 0.20 # 20%
elif salario > 35000:
    categoria = "Nivel B - Mid Senior"
    bono = salario * 0.15 # 15%
elif salario > 15000:
    categoria = "Nivel C - Senior"
    bono = salario * 0.10 # 10%
else:
    categoria = "Nivel D - Junior"
    bono = salario * 0.05 # 5%

total_salario = salario + bono

print(f"\n--- Recibo de Nómina ---")
print(f"Salario Bruto Mensual: ${salario:,.2f}")
print(f"Categoría: {categoria}")
print(f"Bono Mensual Asignado: ${bono:,.2f}")
print(f"Salario Total (Bruto + Bono): ${total_salario:,.2f}")