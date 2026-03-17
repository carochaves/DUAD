#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

list_6 = []
for i in range(10):
    num = int(input(f"Ingrese el numero {i+1}: "))
    list_6.append(num)

greatest_number = max(list_6)

print("Numeros ingresados:", list_6)
print("El numero ingresado mas alto es:", greatest_number)