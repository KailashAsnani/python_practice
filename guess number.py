import random
try:
   top_number = int(input("please enter a number:"))
except:
    print('enter number digitally next time')
    quit()
if top_number<1:
    print('please enter a positive number next time')
    quit()

    print(top_number)
variable = random.randrange(top_number)
while True:
    print("Guess a number between 0 to ", top_number)
    player=input()
    player=int(player)
    if variable==player:
        print('you guessed it correctly!')
        response=input("Do you want to play again?(yes/no)").upper()
        if response!= "YES":
            print('thank you')
            break
        else:
            try:
                top_number = int(input("please enter a number:"))
            except:
                print('enter number digitally next time')
                quit()
            if top_number < 1:
                print('please enter a positive number next time')
                quit()

                print(top_number)
            variable = random.randrange(top_number)
            continue
    elif variable<player:
        print('too high, guess again')
    else:
        print('too low,guess again')

