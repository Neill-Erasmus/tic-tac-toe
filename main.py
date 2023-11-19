import  board, player, sys

Board      = board.Board()
Player_One = player.Player(1)
Player_Two = player.Player(2)

def EndRound(player : player.Player) -> None:
    """
    End the round and ask the player if they want to play again.

    Parameters:
        player (player.Player): The player who won the round.
    """
    
    print(f"{player.GetName()} won!")
    if input("Would you like to play again? (Y/n): ").lower() == 'y':
        Board.ResetBoard()
    else:
        input("Press any key to exit the application...")
        sys.exit(0)

def main():
    """
    The main function to run the Tic-Tac-Toe game.

    This function manages the flow of the game, taking turns between Player One and Player Two
    until there is a winner or the board is full. It utilizes the Board class and Player class
    to update the game state and determine the winner.

    The game continues indefinitely until players choose not to play again.

    Usage:
        1. Players take turns making moves on the Tic-Tac-Toe board.
        2. The game checks for a winner after each move.
        3. If a player wins, the round ends, and players are prompted to play again.
        4. If the board is full and there is no winner, the game declares a draw.
    """
    
    while True:
        Board.UpdateBoard(player=Player_One)
        if Board.CheckWin(player=Player_One):
            EndRound(player=Player_One)
        Board.UpdateBoard(player=Player_Two)
        if Board.CheckWin(player=Player_Two):
            EndRound(player=Player_Two)

if __name__ == "__main__":
    main()