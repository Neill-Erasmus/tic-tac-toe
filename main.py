import  board, player, sys

Board      = board.Board()
Player_One = player.Player(1)
Player_Two = player.Player(2)

def GetRow(player : player.Player) -> int:
    return int(input(f"{player.GetName()}: Which row would you like to play?: "))

def GetColumn(player : player.Player) -> int:
    return int(input(f"{player.GetName()}: Which column would you like to play?: "))

def EndRound(player : player.Player) -> None:
    print(f"{player.GetName()} won!")
    if input("Would you like to play again? (Y/n): ").lower() == 'y':
        Board.ResetBoard()
    else:
        input("Press any key to exit the application...")
        sys.exit(0)

def main():
    while True:
        Board.UpdateBoard(player=Player_One, row=GetRow(player=Player_One), column=GetColumn(player=Player_One))
        if Board.CheckWin(player=Player_One):
            EndRound(player=Player_One)
        Board.UpdateBoard(player=Player_Two, row=GetRow(player=Player_Two), column=GetColumn(player=Player_Two))
        if Board.CheckWin(player=Player_Two):
            EndRound(player=Player_Two)

if __name__ == "__main__":
    main()