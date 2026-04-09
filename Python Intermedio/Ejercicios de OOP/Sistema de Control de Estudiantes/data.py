import csv


class Student:
    def __init__(self, name, section, spanish_grade, english_grade, social_grade, science_grade):
        self.name = name
        self.section = section
        self.spanish_grade = float(spanish_grade)
        self.english_grade = float(english_grade)
        self.social_grade = float(social_grade)
        self.science_grade = float(science_grade)

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish_grade": self.spanish_grade,
            "english_grade": self.english_grade,
            "social_grade": self.social_grade,
            "science_grade": self.science_grade
        }


def export_to_csv(students):
    if not students:
        print("No hay datos para exportar.")
        return

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "name",
            "section",
            "spanish_grade",
            "english_grade",
            "social_grade",
            "science_grade"
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:
            writer.writerow(student.to_dict())

    print("Datos exportados correctamente.")


def import_from_csv():
    try:
        students = []

        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    row["name"],
                    row["section"],
                    row["spanish_grade"],
                    row["english_grade"],
                    row["social_grade"],
                    row["science_grade"]
                )
                students.append(student)

        print("Datos importados correctamente.")
        return students

    except FileNotFoundError:
        print("No existe el archivo para importar.")
        return None