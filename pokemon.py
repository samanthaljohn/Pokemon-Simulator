class Pokemon:
     def __innit__(self, name, type, stats):
        """
        Initialize a Pokemon instance. 

        Parameters:
        name (str): Name of Pokemon.
        type (str): Pokemon Type.
        stats (list): List of stats of Pokemon.
        """
        self.name = name
        self.type = type
        self.stats = stats 