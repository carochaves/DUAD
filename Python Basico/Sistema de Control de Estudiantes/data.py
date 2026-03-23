import csv

def export_to_csv(students):

    if not students:
        print("No hay datos para exportar.")
        return

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["name", "section", "spanish", "english", "social", "science"])

        for student in students:
            writer.writerow([
                student["name"],
                student["section"],
                student["spanish_grade"],
                student["english_grade"],
                student["social_grade"],
                student["science_grade"]
            ])

    print("Datos exportados correctamente.")


def import_from_csv():

    try:
        students = []

        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish_grade": float(row["spanish"]),
                    "english_grade": float(row["english"]),
                    "social_grade": float(row["social"]),
                    "science_grade": float(row["science"])
                }

                students.append(student)

        print("Datos importados correctamente.")
        return students

    except FileNotFoundError:
        print("No existe el archivo para importar.")
        return None