#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

list_3 = [100, 200, 300, 400, 500]
if len (list_3) > 1:
    list_3[0], list_3[-1] = list_3[-1], list_3[0]
print(list_3)