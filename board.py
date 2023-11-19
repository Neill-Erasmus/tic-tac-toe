import player

class Board():
    def __init__(self) -> None:
        self.board : list[list[str]] = self.ResetBoard()

    def ResetBoard(self) -> list[list[str]]:
        return [["-"] * 3 for _ in range(3)]

    def DisplayBoard(self) -> str:
        for row in self.board:
            print(row)

    def UpdateBoard(self, player : player.Player, row : int, column : int) -> None:
        self.board[row - 1][column - 1] = player.GetSymbol()

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