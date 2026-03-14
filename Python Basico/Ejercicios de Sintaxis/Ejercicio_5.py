#Dada n cantidad de notas de un estudiante, calcular:
#Cuantas notas tiene aprobadas (mayor a 70).
#Cuantas notas tiene desaprobadas (menor a 70).
#El promedio de las aprobadas.
#El promedio de las desaprobadas.

n = int(input("Ingrese la cantidad de notas: "))

total_sum = 0
approved_sum = 0
disapproved_sum = 0
approved_count = 0
disapproved_count = 0

for i in range(n):
    grade = float(input(f"Ingrese la nota {i + 1}: "))

    total_sum += grade

    if grade >= 70:
        approved_sum += grade
        approved_count += 1
    elif grade < 70:
        disapproved_sum += grade
        disapproved_count += 1

average_total = total_sum / n

if approved_count > 0:
    average_approved = approved_sum / approved_count
else:
    average_approved = 0

if disapproved_count > 0:
    average_disapproved = disapproved_sum / disapproved_count
else:
    average_disapproved = 0

print("\nResultados:")
print("Notas aprobadas:", approved_count)
print("Notas desaprobadas:", disapproved_count)
print("Promedio total:", average_total)
print("Promedio aprobadas:", average_approved)
print("Promedio desaprobadas:", average_disapproved)