import  board, player

Board      = board.Board()
Player_One = player.Player(1)
Player_Two = player.Player(2)

def GetUserInput(player : player.Player) -> tuple[int, int]:
    row    = int(input(f"Player One: Which row would you like to play?: "))
    column = int(input(f"Player One: Which column would you like to play?: "))
    return (row, column)

def main():
    while True:
        pass
        

if __name__ == "__main__":
    main()