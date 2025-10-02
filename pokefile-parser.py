"""takes a csv file, turns each row into a dictionary to store pokemon information"""

import csv
import Pokemon

def pokedex(infile):
    """
    Define a csv reader that will create a pokedex / list of dictionary entries
    for each pokemon

    infile (csv file): file of pokemon with attributes
    """
    pokemons = []

    with open(infile, newline="") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            name = row["name"]
            type1 = row["type1"]
            type2 = row["type2"] if row["type2"] else None
            stats = [int(row["hp"]), int(row["attack"]), int(row["defense"]),
                    int(row["sp_attack"]), int(row["sp_defense"]), int(row["speed"])]
            move_list = row["moves"].split("|")

            mon = Pokemon(name=name, type1=type1, stats=stats, moves=move_list, type2=type2)
            pokemons.append(mon)

    return(pokemons)

