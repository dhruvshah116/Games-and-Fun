# A simple python script to play the game ROCK-PAPER-SCISSORS with the computer , where you input your choice and the system chooses one of the choices at random and lets you know who won.

import random
def game(user):
    rps=["Rock","Paper","Scissors"]
    computer=rps[random.randint(0,2)]
    if user==computer:
        return "Tie! Computer chose"+computer
    elif user=="Rock":
        if computer=="Paper":
            return "You lose! Computer chose"+computer
        else:
            return "You win!Computer chose"+computer
    elif user=="Paper":
        if computer=="Scissors":
            return "You win!Computer chose "+computer
        else:
            return "You lose! Computer chose"+computer
    elif user=="Scissors":
        if computer=="Rock":
            return "You lose! Computer chose"+computer
        else:
            return "You win!Computer chose"+computer
    else:
        return "Maybe you've made a typo"

x=input("Enter your choice: ")
y=game(x)
print(y)
