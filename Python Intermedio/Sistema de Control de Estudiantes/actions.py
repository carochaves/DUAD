from data import Student


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


def create_student():
    name = input("Ingrese el nombre del estudiante: ")
    section = input("Ingrese la sección del estudiante: ")
    spanish_grade = get_valid_grade("Español")
    english_grade = get_valid_grade("Inglés")
    social_grade = get_valid_grade("Sociales")
    science_grade = get_valid_grade("Ciencias")

    student = Student(
        name,
        section,
        spanish_grade,
        english_grade,
        social_grade,
        science_grade
    )

    return student


def get_student_info(students):
    student = create_student()
    students.append(student)
    print("Estudiante agregado correctamente.")


def show_students_info(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    for student in students:
        print("\nNombre:", student.name)
        print("Seccion:", student.section)
        print("Espanol:", student.spanish_grade)
        print("Ingles:", student.english_grade)
        print("Sociales:", student.social_grade)
        print("Ciencias:", student.science_grade)


def calculate_average(student):
    return (
        student.spanish_grade
        + student.english_grade
        + student.social_grade
        + student.science_grade
    ) / 4


def prom_each_student(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    for student in students:
        average = calculate_average(student)
        print("\nEstudiante:", student.name)
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

    students_sorted = sorted(students, key=calculate_average, reverse=True)

    print("\nTop 3 estudiantes:")

    for i, student in enumerate(students_sorted[:3], start=1):
        print(f"{i}. {student.name} - {calculate_average(student)}")