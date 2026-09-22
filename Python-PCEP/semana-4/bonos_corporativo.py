# Código plano - sin sangría

#categoría = input("categoría del empleado (A/B/C): ")
#anios_servicio = input("años de servicio: ")
#evaluacion = float(input("Calificación de evaluación (0-100): "))

#if categoria == "A":
#if anios_servicio >= 5:
#if evaluacion >= 80:
#print("Bono máximo: 20%")
#else:
#print("Bono estándar: 10%")
#else:
#print("Sin elegibilidad aún (menos de 5 años)")
#elif categoria == "B":
#if evaluacion >= 90:
#print("Bono por desempeño excepcional: 15%")
#else:
#print("Bono base: 5%")
#else:
#print("Categoría sin esquema de bonos definido")

#------------Corrección de ejercicio--------------------------------#

#Meta - El programa debe imprimir para estos inputs:
#categoría='A' años=6, evaluacion=85 => "Bono máximo: 20%"
#categoría='A' años=3, evaluacion=70 => "Sin elegibilidad aún (menos de 5 años)"
#categoría='B' años=cualquiera, evaluacion=92 => "Bono por desempeño excepcional: 15%"
#categoría='C' cualquier cosa => categoría sin esquema de bonos definido

categoria = input("categoría del empleado (A/B/C): ")
anios_servicio = int(input("años de servicio: "))
evaluacion = int(input("Calificación de evaluación (0-100): "))

if categoria == "A":
    if anios_servicio >= 5:
        if evaluacion >= 80:
            print("Bono máximo: 20%")
        else:
            print("Bono estándar: 10%")
    else:
        print("Sin elegibilidad aún (menos de 5 años)")
elif categoria == "B":
    if evaluacion >= 90:
        print("Bono por desempeño excepcional: 15%")
    else:
        print("Bono base: 5%")
else:
    print("Categoría sin esquema de bonos definido")
