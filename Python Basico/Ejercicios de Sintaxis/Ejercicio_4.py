#Cree un programa que le pida tres números al usuario y muestre el mayor.

number_1 = int(input("Ingrese un numero"))
number_2 = int(input("Ingrese un numero"))
number_3 = int(input("Ingrese un numero"))
greatest_number = max(number_1,number_2,number_3)
print(f"El numero mayor es: {greatest_number}")