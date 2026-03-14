#Cree una función que le dé la vuelta a un string y lo retorne.
def turn_over(my_string): 
    reversed_string = ""

    for i in range(len(my_string) - 1, -1, -1):
        reversed_string += my_string[i]

    return reversed_string

print(turn_over("Costa Rica"))