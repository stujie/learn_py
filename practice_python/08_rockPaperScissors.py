"""
Exercise 8: Make a two-player Rock-Paper-Scissors game.

Rules:
- Rock beats Scissors
- Scissors beats paper
- Paper beats rock
"""
play = str(input("Would you like to play? (Y/N): "))

while (play.casefold() == "y"):
    player1 = str(input("Player 1: Rock, Paper, or Scissors? (R/P/S): "))
    player2 = str(input("Player 2: Rock, Paper, or Scissors? (R/P/S): "))
    
    if player1.casefold() == "r":       # player 1 chooses rock
        if player2.casefold() == "r":   # player 2 chooses rock
            print("It's a tie!")
        elif player2.casefold() == "p": # player 2 chooses paper
            print("Congrats Player 2! You win!")
        else: # player 2 chooses scissors
            print("Congrats Player 1! You win!")
    elif player1.casefold() == "p":       # player 1 chooses paper
        if player2.casefold() == "r":   # player 2 chooses rock
            print("Congrats Player 1! You win!")
        elif player2.casefold() == "r": # player 2 chooses paper
            print("It's a tie!")
        else: # player 2 chooses scissors
            print("Congrats Player 2! You win!")
    else:   # player 1 chooses scissors
        if player2.casefold() == "r":   # player 2 chooses rock
            print("Congrats Player 2! You win!")
        elif player2.casefold() == "p": # player 2 chooses paper
            print("Congrats Player 1! You win!")
        else: # player 2 chooses scissors
            print("It's a tie!")
    
    play = str(input("Would you like to play again? (Y/N): "))

print("Thank you for playing!")