import  board, player, sys

Board      = board.Board()
Player_One = player.Player(1)
Player_Two = player.Player(2)

def EndRound(player : player.Player) -> None:
    print(f"{player.GetName()} won!")
    if input("Would you like to play again? (Y/n): ").lower() == 'y':
        Board.ResetBoard()
    else:
        input("Press any key to exit the application...")
        sys.exit(0)

def main():
    while True:
        Board.UpdateBoard(player=Player_One)
        if Board.CheckWin(player=Player_One):
            EndRound(player=Player_One)
        Board.UpdateBoard(player=Player_Two)
        if Board.CheckWin(player=Player_Two):
            EndRound(player=Player_Two)

if __name__ == "__main__":
    main()