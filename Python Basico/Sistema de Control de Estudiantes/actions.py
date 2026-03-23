def get_student_info(students):

    name = input("Ingrese su nombre: ")
    section = input("Ingrese su seccion: ")

    spanish_grade = get_valid_grade("Espanol")
    english_grade = get_valid_grade("Ingles")
    social_grade = get_valid_grade("Sociales")
    science_grade = get_valid_grade("Ciencias")

    student = {
        "name": name,
        "section": section,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "social_grade": social_grade,
        "science_grade": science_grade
    }

    students.append(student)

    print("Estudiante agregado correctamente.")

    return student


def get_valid_grade(subject):

    while True:
        try:
            grade = float(input(f"Ingrese la nota de {subject}: "))

            if 0 <= grade <= 100:
                return grade
            else:
                print("Error: la nota debe estar entre 0 y 100.")

        except ValueError:
            print("Error: debe ingresar un numero.")


def show_students_info(students):

    if not students:
        print("No hay estudiantes registrados.")
        return

    for student in students:
        print("\nNombre:", student["name"])
        print("Seccion:", student["section"])
        print("Espanol:", student["spanish_grade"])
        print("Ingles:", student["english_grade"])
        print("Sociales:", student["social_grade"])
        print("Ciencias:", student["science_grade"])


def calculate_average(student):

    return (
        student["spanish_grade"]
        + student["english_grade"]
        + student["social_grade"]
        + student["science_grade"]
    ) / 4


def prom_each_student(students):

    if not students:
        print("No hay estudiantes registrados.")
        return

    for student in students:
        average = calculate_average(student)

        print("\nEstudiante:", student["name"])
        print("Promedio:", average)


def average_all_students(students):

    if not students:
        print("No hay estudiantes registrados.")
        return

    total = 0

    for student in students:
        total += calculate_average(student)

    general_average = total / len(students)

    print("Promedio general de todos los estudiantes:", general_average)


def top_3_students(students):

    if not students:
        print("No hay estudiantes registrados.")
        return

    for student in students:
        student["average"] = calculate_average(student)

    top1 = None
    top2 = None
    top3 = None

    for student in students:

        if top1 is None or student["average"] > top1["average"]:
            top3 = top2
            top2 = top1
            top1 = student

        elif top2 is None or student["average"] > top2["average"]:
            top3 = top2
            top2 = student

        elif top3 is None or student["average"] > top3["average"]:
            top3 = student

    print("\nTop 3 estudiantes:")

    if top1:
        print("1.", top1["name"], "-", top1["average"])

    if top2:
        print("2.", top2["name"], "-", top2["average"])

    if top3:
        print("3.", top3["name"], "-", top3["average"])