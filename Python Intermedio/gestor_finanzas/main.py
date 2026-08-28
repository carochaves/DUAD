import FreeSimpleGUI as sg

from interfaces import (
    create_main_window,
    create_category_window,
    create_movement_window
)

from models import FinanceManager

from persistence import (
    save_categories,
    load_categories,
    save_movements,
    load_movements
)


manager = FinanceManager()


# Cargar datos guardados
load_categories(manager)
load_movements(manager)


window = create_main_window()


def update_main_window():
    movements_data = []

    for movement in manager.get_movements():

        if movement.type == "income":
            movement_type = "Ingreso"

        else:
            movement_type = "Gasto"

        movements_data.append([
            movement.title,
            movement.amount,
            movement.category,
            movement_type
        ])

    window["movements_table"].update(
        values=movements_data
    )

    window["income_total"].update(
        manager.calculate_income()
    )

    window["expense_total"].update(
        manager.calculate_expenses()
    )

    window["balance_total"].update(
        manager.get_balance()
    )


# Mostrar datos cargados al abrir
update_main_window()


while True:
    event, values = window.read()

    # SALIR
 
    if event == "Salir" or event == sg.WIN_CLOSED:

        save_categories(manager)
        save_movements(manager)

        break

    # AGREGAR CATEGORÍA

    if event == "Agregar Categoría":

        category_window = create_category_window()

        category_event, category_values = (
            category_window.read()
        )

        if category_event == "Guardar":

            category_name = (
                category_values["category_name"]
            )

            try:
                manager.add_category(
                    category_name
                )

                save_categories(manager)

                sg.popup(
                    "Categoría agregada correctamente"
                )

            except ValueError as error:
                sg.popup_error(
                    str(error)
                )

        category_window.close()

    # AGREGAR GASTO

    if event == "Agregar Gasto":

        categories = [
            category.name
            for category
            in manager.get_categories()
        ]

        if not categories:
            sg.popup_error(
                "Debe agregar una categoría primero."
            )

            continue


        movement_window = create_movement_window(
            "Gasto",
            categories
        )

        movement_event, movement_values = (
            movement_window.read()
        )


        if movement_event == "Guardar":

            try:
                title = (
                    movement_values["title"]
                )

                amount = float(
                    movement_values["amount"]
                )

                category = (
                    movement_values["category"]
                )


                manager.add_movement(
                    title,
                    amount,
                    category,
                    "expense"
                )


                save_movements(manager)

                update_main_window()


                sg.popup(
                    "Gasto agregado correctamente"
                )


            except (ValueError, TypeError) as error:

                sg.popup_error(
                    str(error)
                )


        movement_window.close()

    # AGREGAR INGRESO

    if event == "Agregar Ingreso":

        categories = [
            category.name
            for category
            in manager.get_categories()
        ]

        if not categories:
            sg.popup_error(
                "Debe agregar una categoría primero."
            )

            continue


        movement_window = create_movement_window(
            "Ingreso",
            categories
        )

        movement_event, movement_values = (
            movement_window.read()
        )


        if movement_event == "Guardar":

            try:
                title = (
                    movement_values["title"]
                )

                amount = float(
                    movement_values["amount"]
                )

                category = (
                    movement_values["category"]
                )


                manager.add_movement(
                    title,
                    amount,
                    category,
                    "income"
                )


                save_movements(manager)

                update_main_window()


                sg.popup(
                    "Ingreso agregado correctamente"
                )


            except (ValueError, TypeError) as error:

                sg.popup_error(
                    str(error)
                )


        movement_window.close()


window.close()