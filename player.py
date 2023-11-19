class Player():
    def __init__(self, player : int) -> None:
        """
        Initializes a player with a unique ID and corresponding symbol.

        Args:
            player (int): The player's ID, should be 1 or 2.

        Attributes:
            id (int): The unique ID of the player.
            symbol (str): The symbol associated with the player ('O' or 'X').

        Usage:
            player_one = Player(1)
            player_two = Player(2)
        """
        
        self.id : int = player
        if self.id == 1:
            self.symbol = 'O'
        elif self.id == 2:
            self.symbol = 'X'

    def GetName(self) -> str:
        """
        Gets the name of the player based on their ID.

        Returns:
            str: The name of the player ('Player One' or 'Player Two').

        Usage:
            player_one_name = player_one.GetName()
            player_two_name = player_two.GetName()
        """
        
        if self.id == 1:
            return "Player One"
        elif self.id == 2:
            return "Player Two"
        return ""

    def GetSymbol(self) -> str:
        """
        Gets the symbol associated with the player.

        Returns:
            str: The player's symbol ('O' or 'X').

        Usage:
            player_one_symbol = player_one.GetSymbol()
            player_two_symbol = player_two.GetSymbol()
        """
        
        return self.symbol