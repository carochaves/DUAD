#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
def total_upper_lower(my_string):
    upper = 0
    lower = 0

    for char in my_string:
        if char.isupper():
                upper += 1
        if char.islower():
                lower += 1

    print(f'Tenemos: "{my_string}". La cantidad de minisculas es:{lower} y de mayusculas es:{upper}')

total_upper_lower("Me gusta el color AZUL")