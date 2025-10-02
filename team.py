import Pokemon 

class Team:
    def __innit__(self, pokemons):
        """
        Initiate a Team instance.

        pokemons (list): List of 6 (six) Pokemon objects.
        """
        self.pokemons = pokemons

    def generate_team(self, all_pokemon):
        """
        Create a random team of 6 (six) Pokemon from the list of ALL pokemon.

        all_pokemon (list): list of all Pokemon.
        """
        team = []
        return team