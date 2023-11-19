import player
class Board():
    """
    Represents the Tic-Tac-Toe board.

    Attributes:
        board (list): A 3x3 grid representing the state of the Tic-Tac-Toe board.

    Methods:
        __init__: Initializes a new instance of the Board class.
        ResetBoard: Resets the board to its initial state.
        DisplayBoard: Displays the current state of the board.
        UpdateBoard: Updates the board with a player's move.
        CheckWin: Checks if the specified player has won the game.
        CheckFull: Checks if the board is full.
        ResetIfFull: Resets the board if it's full, declaring a draw.
    """
    
    def __init__(self) -> None:
        """
        Initializes a new instance of the Board class.

        The board is a 3x3 grid with each cell initialized to '-'.

        Usage:
            board = Board()
        """
        
        self.board : list[list[str]] = [["-"] * 3 for _ in range(3)]

    def ResetBoard(self) -> None:
        """
        Resets the board to its initial state.

        Usage:
            board.ResetBoard()
        """
        
        self.board = [["-"] * 3 for _ in range(3)]

    def DisplayBoard(self) -> None:
        """
        Displays the current state of the board.

        The board is displayed as a 3x3 grid.

        Usage:
            board.DisplayBoard()
        """
        
        for row in self.board:
            print(" ".join(row))

    def UpdateBoard(self, player: player.Player) -> None:
        """
        Updates the board with a player's move.

        The player is prompted to enter the row and column where they want to place their symbol.
        The board is updated if the chosen cell is valid and unoccupied.

        Args:
            player (Player): The player making the move.

        Usage:
            board.UpdateBoard(player)
        """
        
        while True:
            try:
                row    = int(input(f"{player.GetName()}: Which row would you like to play?: "))
                column = int(input(f"{player.GetName()}: Which column would you like to play?: "))
                if (1 <= row <= 3) and (1 <= column <= 3):
                    if self.board[row - 1][column - 1] == "-":
                        self.board[row - 1][column - 1] = player.GetSymbol()
                        self.DisplayBoard()
                        break
                    else:
                        print("This cell is already taken. Try again.")
                else:
                    print("Invalid row or column. Please enter values between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def CheckWin(self, player : player.Player) -> bool:
        """
        Checks if the specified player has won the game.

        The method checks for a winning combination in rows, columns, and diagonals.

        Args:
            player (Player): The player to check for a win.

        Returns:
            bool: True if the player has won, False otherwise.

        Usage:
            result = board.CheckWin(player)
        """
        
        for row in self.board:
            if all(cell == player.symbol for cell in row):
                return True
        for column in range(3):
            if all(self.board[row][column] == player.symbol for row in range(3)):
                return True
        if all(self.board[i][i] == player.symbol for i in range(3)) or all(self.board[i][2 - i] == player.symbol for i in range(3)):
            return True
        return False

    def CheckFull(self) -> bool:
        """
        Checks if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.

        Usage:
            result = board.CheckFull()
        """
        
        for row in self.board:
            for pos in row:
                if pos == '-':
                    return False
        return True

    def ResetIfFull(self) -> None:
        """
        Resets the board if it's full, declaring a draw.

        The method checks if the board is full. If it is, it prints a draw message,
        displays the current state of the board, and resets the board to its initial state.

        Usage:
            board.ResetIfFull()
        """
    
        if self.CheckFull():
            print("The board is full. It's a draw!")
            self.DisplayBoard()
            self.ResetBoard()