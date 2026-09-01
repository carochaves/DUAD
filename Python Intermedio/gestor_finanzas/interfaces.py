import FreeSimpleGUI as sg


def create_main_window():
    layout = [
        [sg.Text("Gestor de Finanzas")],

        [
            sg.Text("Ingresos:"),
            sg.Text("0", key="income_total")
        ],

        [
            sg.Text("Gastos:"),
            sg.Text("0", key="expense_total")
        ],

        [
            sg.Text("Balance:"),
            sg.Text("0", key="balance_total")
        ],

        [
            sg.Table(
                values=[],
                headings=[
                    "Nombre",
                    "Monto",
                    "Categoría",
                    "Tipo"
                ],
                key="movements_table",
                auto_size_columns=True,
                justification="left",
                num_rows=10
            )
        ],

        [
            sg.Button("Agregar Categoría"),
            sg.Button("Agregar Gasto"),
            sg.Button("Agregar Ingreso")
        ],

        [sg.Button("Salir")]
    ]
    window = sg.Window(
        "Gestor de Finanzas",
        layout,
        finalize=True
    )

    return window


def create_category_window():
    layout = [
        [sg.Text("Nombre de categoría")],

        [
            sg.Input(
                key="category_name"
            )
        ],

        [
            sg.Button("Guardar"),
            sg.Button("Cerrar")
        ]
    ]

    window = sg.Window(
        "Agregar Categoría",
        layout
    )

    return window


def create_movement_window(movement_type, categories):
    layout = [
        [sg.Text(f"Agregar {movement_type}")],

        [
            sg.Text("Nombre"),
            sg.Input(key="title")
        ],

        [
            sg.Text("Monto"),
            sg.Input(key="amount")
        ],

        [
            sg.Text("Categoría"),

            sg.Combo(
                values=categories,
                key="category",
                readonly=True
            )
        ],

        [
            sg.Button("Guardar"),
            sg.Button("Cerrar")
        ]
    ]

    window = sg.Window(
        f"Agregar {movement_type}",
        layout
    )

    return window