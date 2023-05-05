import random
choices=["rock","paper","scissors"]
while True:

    computer=random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock,paper or scissors:").lower()
    print("computer: ", computer)
    print("payer: ", player)
    if player==computer:
        print("it's a tie!")
    elif(player == "rock"):
        if computer =='paper':
            print("You Lose!")
        else:
            print("you win!")
    elif player=='paper':
        if computer=='rock':
            print('you win!')
        else:
            print('you lose!')
    else:
        if computer=='rock':
            print('you lose!')
        else:
            print('you win!')

    play_again = input("play again?(yes/no)").upper()
    if play_again != "YES":
        break

print("bye bye")
