class Pokemon:
    def __innit__(self, name, type, stats, moves):
        """
        Initialize a Pokemon instance. 

        Parameters:
        name (str): Name of Pokemon.
        type (str): Pokemon Type.
        stats (list): List of Pokemon's moves.
        moves (list): list of Pokemon's moves. 
        """
        self.name = name
        self.type = type
        self.stats = stats 
        self.moves = moves

    def __str__(self):
        """
        Returns a string with the following information:
            - Pokemon's name
            - Pokemon's type
        """
        return (f"Your Pokemon, {self.name}, is a {self.type} Pokemon!")
