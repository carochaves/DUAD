import csv

def videogame_info():
    name = (input("Escriba el nombre del videojuego: "))
    gender = (input("Cual es el genero del videojuego: "))
    developer = input("Ingrese el desarrollador del videojuego: ")
    classification = input("Ingrese la clasificacion ESRB: ")
    return name, gender,developer, classification


with open("videogames.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "gender", "developer", "classification"])

    while True:

        name, gender, developer, classification = videogame_info()
        writer.writerow([name, gender, developer, classification])

        response = input("Desea ingresar otro videojuego? (s/n): ")
        if response.lower() != "s":
            break