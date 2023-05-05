name = input('please enter your name')
print('welcome', name, 'to your adventure')

answer=input("you have come to a dirt road. do you want to go to the right or left?").lower()
if answer=="left":
    answer = input('There is a river in front of you , do you want to swim across or walk around?Type swim to swim across and walk to walk around').lower()
    if answer=="swim":
        print("you get a ruby inside the river,you win!")
    elif answer=="walk":
        print("A wild beast sees you walking and caches you.You die!")
    else:
        print("invalid answer, you lose")
elif answer=="right":
    answer = input("there is a bridge in front of you, Do you cross it or turn around(cross/turn)").lower()
    if answer=="cross":
        print("the bridge was very weak and you fall down!")
    elif answer=="turn":
        answer=input("there is a stranger in front of you, do you talk to him or ignore?(talk/ignore)").lower()
        if answer=="talk":
            print("he gives you gold and you win!")
        elif answer=="ignore":
            print("he gets offended and kills you,you lose!")
        else:
            print("wrong answer, you lose!")
    else:
        print("invalid answer you lose!")
else:
    print("invalid answer,you lose")