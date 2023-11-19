class Player():
    def __init__(self, player : int) -> None:
        self.id : int = player
        if self.id == 1:
            self.symbol = 'O'
        elif self.id == 2:
            self.symbol = 'X'
            
    def GetName(self) -> str:
        if self.id == 1:
            return "Player One"
        elif self.id == 2:
            return "Player Two"
        return ""
            
    def GetSymbol(self) -> str:
        return self.symbol