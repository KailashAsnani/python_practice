import random

again = True

while again:
    print(random.randint(1,6))
    Again_Roll = input("Do you want to play again(yes/no)")
    if Again_Roll.upper()=="YES":
        continue
    else:
        break

