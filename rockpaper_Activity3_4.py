player1 = input("enter your name:")
player2 = input("enter your name")

while True:
    player1Input = input(player1 + "! enter your option rock, paper or scissors ")
    player2Input = input(player2 + "! enter your option rock, paper or scissors ")

    if (player1Input == "rock"):
        if (player2Input == "scissors"):
            print(player1 + " Wins")
        else:
            print("Paper Wins!")
    elif (player1Input == "scissors"):
        if (player2Input == "paper"):
            print("scissors Win!")
        else:
            print("rock win!")
    elif (player1Input == "paper"):
        if (player2Input == "rock"):
            print("paper wins")
        else:
            print("scissors win")
    elif (player1Input == player2Input):
        print("its a tie")
    conFlag = input("do you want to continue: (Y/N))")
    if conFlag.upper() == "Y":
        pass
    elif conFlag.upper() == "N":
        raise SystemExit
    else:
        print("invalid input")
        raise SystemExit
    