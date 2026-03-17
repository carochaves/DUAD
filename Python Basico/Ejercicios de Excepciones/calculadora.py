def get_first_value():
    while True:
        try:
            return int(input("Ingrese el primer valor: "))
        except ValueError:
            print("Error: Numero invalido.")


def show_menu():
    print("\nMenu")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado")
    print("6. Salir")


def get_second_value():
    while True:
        try:
            return int(input("Ingrese el segundo valor: "))
        except ValueError:
            print("Error: Numero invalido.")


def sum_values(a, b):
    return a + b


def subtract_values(a, b):
    return a - b


def mult_values(a, b):
    return a * b


def div_values(a, b):
    if b == 0:
        print("Error: No se puede dividir entre 0.")
        return None
    return a / b


def reset_result():
    print("Borrando resultado...")
    return 0


first_value = get_first_value()

while True:

    show_menu()

    try:
        option = int(input("Seleccione la operacion que desea realizar: "))
    except ValueError:
        print("Error: Opcion invalida.")
        continue

    if option < 1 or option > 6:
        print("Error: Opcion invalida.")
        continue

    if option == 6:
        print("Saliendo...")
        break

    if option == 5:
        first_value = reset_result()
        print("Resultado actual:", first_value)
        continue

    second_value = get_second_value()

    if option == 1:
        result = sum_values(first_value, second_value)

    elif option == 2:
        result = subtract_values(first_value, second_value)

    elif option == 3:
        result = mult_values(first_value, second_value)

    elif option == 4:
        result = div_values(first_value, second_value)

    if result is None:
        continue

    first_value = result
    print("Resultado:", first_value)
