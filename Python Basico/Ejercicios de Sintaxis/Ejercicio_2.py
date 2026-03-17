#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("Ingrese su nombre")
last_name = input("Ingrese su apellido")
age = int(input("Ingrese su edad"))
if (age <= 2):
    print("Es un bebe")
elif (3 <= age <= 9):
    print("Es un niño")
elif (10 <= age <= 12 ):
    print("Es un preadolescente")
elif (13 <= age <= 18):
    print("Es un adolescente")
elif (19 <= age <= 30):
    print("Es un adulto joven")
elif (31 <= age <= 74):
    print("Es un adulto")
elif(75 <= age < 120):
    print("Es un adulto mayor")
else:
    print("Numero incorrecto")