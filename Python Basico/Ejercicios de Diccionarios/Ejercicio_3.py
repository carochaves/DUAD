#Cree un programa que use una lista para eliminar keys de un diccionario.
employee = {
    'name': 'John',
    'email': 'john@ecorp.com',
    'access_level': 5,
    'age': 28
}

keys_to_delete = ['access_level', 'age']

for key in keys_to_delete:
    employee.pop(key)

print(employee)
