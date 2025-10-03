import random

#: List of the 25 possible Pokémon natures.
#: Used to randomly assign a nature to each Pokemon.
NATURES = ["Adamant", "Bashful", "Bold", "Brave", "Calm"
        "Careful", "Docile", "Gentle", "Hardy", "Hasty", 
        "Impish", "Jolly", "Lax", "Lonely", "Mild",
        "Modest", "Naive", "Naughty", "Quiet", "Quirky",
        "Rash", "Relaxed", "Sassy", "Serious", "Timid"]

class Pokemon:
    """ 
    Represents a Pokemon with stats, moves, typing, and nature.
    Each Pokemon instance is assigned a random nature from `NATURES`.
    """

    def __innit__(self, name, type1, stats, moves, type2 = None):
        """
        Initialize a Pokemon instance. 

        Parameters:
        name (str): Name of Pokemon.
        type1 (str): Pokemon Type.
        stats (list): List of Pokemon's moves.
        moves (list): list of Pokemon's moves. 
        type2 (str): Pokemon secondary type - defaults to None.
        """
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.stats = stats 
        self.moves = moves

    def __str__(self):
        """
        Returns a string with the following information:
            - Pokemon's name
            - Pokemon's type
        """
        return (f"Your Pokemon, {self.name}, is a {self.type1} Pokemon!")
    
    def create_mon(self, poke_dict):
        """
        Creates a Pokemon instance from an already constructed dictionary after checking 
        that the right attributes are present.

        Parameters:
        poke_dict (dict): dictionary representing a pokemon
        """

        return Pokemon()
