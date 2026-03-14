#Intente acceder a una variable definida dentro de una función desde afuera.
#def example_scope():
#    local_var = 10
#    print("Dentro de la función:", local_var)

#example_scope()

#print("Fuera de la función:", local_var)  


#Intente acceder a una variable global desde una función y cambiar su valor.
x = 5

def change():
    global x
    x = x + 1

change()
print(x)
