import menu
import actions
import data


def main():

    students = []
    
    while True:

        menu.show_menu()
        option = menu.get_menu_option()

        if option == 1:
            actions.get_student_info(students)

        elif option == 2:
            actions.show_students_info(students)

        elif option == 3:
            actions.prom_each_student(students)

        elif option == 4:
            actions.average_all_students(students)

        elif option == 5:
            actions.top_3_students(students)

        elif option == 6:
            data.export_to_csv(students)

        elif option == 7:
            students_imported = data.import_from_csv()

            if students_imported is not None:
                students = students_imported

        elif option == 8:
            print("Saliendo del programa...")
            break


if __name__ == "__main__":
    main()