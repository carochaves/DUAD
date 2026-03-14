#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

my_string = "Costa Rica"

for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])