choice = ["Rock", "Paper", "Scissors"]

playerOne = input("Player 1: Choose an Option (Rock/Paper/Scissors): ")
playerTwo = input("Player 2: Choose an Option (Rock/Paper/Scissors): ")

if playerOne not in choice:
    print("Wrong input value entered")
elif playerTwo not in choice:
    print("Wrong input value entered")
else:
    if playerOne == playerTwo:
        print("Draw")
    else:   
        if playerOne == choice[0]:
            if playerTwo == choice[1]:
                print("Player 2 Win.")
            elif playerTwo == choice[2]:
                print("Player 1 Win.")
        elif playerOne == choice[1]:
            if playerTwo == choice[0]:
                print("Player 1 Win.")
            elif playerTwo == choice[2]:
                print("Player 2 Win.")
        elif playerOne == choice[2]:
            if playerTwo == choice[0]:
                print("Player 2 Win.")
            elif playerTwo == choice[1]:
                print("Player 1 Win.")
    