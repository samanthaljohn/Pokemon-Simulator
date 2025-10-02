class Pokemon:
    def __innit__(self, name, type1, type2, stats, moves):
        """
        Initialize a Pokemon instance. 

        Parameters:
        name (str): Name of Pokemon.
        type1 (str): Pokemon Type.
        type2 (str): Pokemon secondary type.
        stats (list): List of Pokemon's moves.
        moves (list): list of Pokemon's moves. 
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
