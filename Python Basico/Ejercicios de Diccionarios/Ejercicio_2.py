#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
keys = ['color', 'shape', 'size']
values = ['red', 'circle', 'big']
my_first_dictionary = {}
for i in range(len(keys)):
    my_first_dictionary[keys[i]] = values[i]
print(my_first_dictionary)