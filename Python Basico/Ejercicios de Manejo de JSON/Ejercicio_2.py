import json

with open("pokemon.json", "r") as file:
    pokemons = json.load(file)


def add_new_pokemon():

    name = input("Ingrese el nombre del pokemon: ")
    level = int(input("Ingrese el nivel: "))
    type_pokemon = input("Ingrese el tipo: ")

    hp = int(input("Ingrese HP: "))
    attack = int(input("Ingrese Attack: "))
    defense = int(input("Ingrese Defense: "))
    sp_attack = int(input("Ingrese Sp. Attack: "))
    sp_defense = int(input("Ingrese Sp. Defense: "))
    speed = int(input("Ingrese Speed: "))

    new_pokemon = {
        "name": {"english": name},
        "level": level,
        "type": [type_pokemon],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
            }
    }

    return new_pokemon


pokemon_added = add_new_pokemon()

pokemons.append(pokemon_added)


with open("pokemon.json", "w") as file:
    json.dump(pokemons, file, indent=4)

print("Pokemon agregado correctamente.")
