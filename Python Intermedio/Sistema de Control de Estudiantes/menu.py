def show_menu():
    print("\nMenu")
    print("1. Agregar un estudiante")
    print("2. Mostrar informacion de estudiantes")
    print("3. Mostrar promedio por estudiante")
    print("4. Mostrar promedio general")
    print("5. Top 3 estudiantes")
    print("6. Exportar datos")
    print("7. Importar datos")
    print("8. Salir")


def get_menu_option():
    while True:
        try:
            option = int(input("Seleccione una opcion: "))
            if 1 <= option <= 8:
                return option
            else:
                print("Error: Opcion invalida.")
        except ValueError:
            print("Error: Debe ingresar un numero.")