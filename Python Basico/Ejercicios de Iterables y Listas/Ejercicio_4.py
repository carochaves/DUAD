#Cree un programa que elimine todos los números impares de una lista.

list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_5 = []
for num in list_4:
    if num % 2 == 0:
        list_5.append(num)
print(list_5)