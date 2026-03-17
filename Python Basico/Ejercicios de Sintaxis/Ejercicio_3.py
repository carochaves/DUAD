#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random
random_number = random.randint(1,10)
number = 0
while number != random_number:
    number = int(input("Ingrese un numero entero del 1 al 10: "))
print("Ha adivinado el número!")