import player
class Board():
    def __init__(self) -> None:
        self.board : list[list[str]] = [["-"] * 3 for _ in range(3)]

    def ResetBoard(self) -> None:
        self.board = [["-"] * 3 for _ in range(3)]

    def DisplayBoard(self) -> None:
        for row in self.board:
            print(row)

    def UpdateBoard(self, player: player.Player) -> None:
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
        for row in self.board:
            for pos in row:
                if pos == '-':
                    return False
        return True

    def ResetIfFull(self) -> None:
        if self.CheckFull():
            print("The board is full. It's a draw!")
            self.ResetBoard()