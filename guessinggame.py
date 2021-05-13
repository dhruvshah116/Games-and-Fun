import random

def computerGuess(lowval,highval,randnum,count=0):
    if highval>=lowval:
        guess=lowval+(highval-lowval)//2
        if guess==randnum:
            return count
        elif guess>randnum:
            count=count+1
            return computerGuess(lowval,guess-1,randnum,count)
        else:
            count=count+1
            return computerGuess(guess+1,highval,randnum,count)
    else:
        return -1

randnum=random.randint(1,101)
count=0
guess=-99
while guess!=randnum:
    guess=int(input('Enter Your Guess Bewtween 0 and 100:'))
    if guess>randnum:
        print('lower')
        count=count+1
    elif guess<randnum:
        print('higher')
        count=count+1
    else:
        print('you guessed it!')
        break


print("You took ",count,"guesses")
print('Computer took',computerGuess(1,100,randnum),'Guesses')
