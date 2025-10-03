"""takes a csv file, turns each row into a dictionary to store pokemon information"""

import csv
import random
from pokemon import *

def moves(name):
    """
    Define a function that takes in a pokemon's name,
    and returns a list of four random moves for that pokemon
    
    Parameters:
    name (str): the pokemon's name

    Returns: A list of 4 random moves(or fewer if the pokemon has fewer than 4 moves)
    """
    moves_file = "movesets.csv"
    move_set = []

    with open(moves_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(",")
            pokemon = parts[0]
            all_moves = parts[1:]

            if name.lower() == pokemon.lower():
                if len(all_moves) > 4:
                    move_set = random.sample(all_moves, 4)
                else:
                    move_set = all_moves
                    break
    return move_set


def pokedex(infile):
    """
    Define a csv reader that will create a "pokedex" (list of dictionary entries
    for each pokemon) and return this "pokedex." (list)

    Parameters:
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
            moves_list = moves(name)

            mon = Pokemon(name=name, type1=type1, stats=stats, moves=moves_list, type2=type2)
            pokemons.append(mon)

    return(pokemons)

def pokemon_names(infile, outfile):
    with open(infile, "r") as infile, open(outfile, "w") as outfile:
        lines = infile.readlines()
        for line in lines:
            if line.split(",")[0] == "name":
                continue
            name = (line.split(","))[1]
            outfile.write(name + "\n")

pokemon_names("first151.csv", "movesets.csv")