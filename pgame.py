import tkinter
import random


#list of colours
colours=["Red","Blue","Green","Pink","Black","Yellow","Orange","White","Purple","Brown"]

score=0

#initially game time left

timeleft=30

#function that will start the game
def startGame(event):
    if timeleft==30:
        countdown()
        #start the countdown timer

    #run function to choose the next colour
    nextcolour()

def nextcolour():
    #use the globally declared variables above
    global score
    global timeleft

    #if a game is currently in play:
    if timeleft>0:
        #make the text entry box active
        #focus_set() is used to set focus on desired widget iff the master window is focused
        e.focus_set()

        #if colour typed is equal to the colour of text
        if e.get().lower()==colours[1].lower():
            score=score+1

        #clear the text entry box
        e.delete(0,tkinter.END)

        random.shuffle(colours)

        #change the colour to type, by changing the text and colour to a random value
        label.config(fg=str(colours[1]),text=str(colours[0]))

        #update the score
        scoreLabel.config(text="Score:"+str(score))

def countdown():
    global timeleft
    #if game is in play ,decrement the timer
    if timeleft>0:
        timeleft-=1

        #update the timeleft label
        timeLabel.config(text='Time Left: '+str(timeleft))

        #run the fuction again after 1 second
        timeLabel.after(1000,countdown)


#create a GUI window
root=tkinter.Tk()

#set the title
root.title("Colour Game")

#set the size
root.geometry("375x200")

#add an instructions label
instruction=tkinter.Label(root,text="Type in the colour of the words , and not line word text:",
                          font=("Halvetica",12))
instruction.pack()

#add a score label
scoreLabel=tkinter.Label(root,text="Press Enter to start",font=("Halvetica",12))
scoreLabel.pack()

#add a time left label
timeLabel=tkinter.Label(root,text="Time Left:"+str(timeleft),font=("Halvetica",12))
timeLabel.pack()

#add a label for displaying colours
label=tkinter.Label(root,font=("Halvetica",12))
label.pack()

#add a text entry for typing in colours
e=tkinter.Entry(root)

#run the startgame() when enter key is pressed
root.bind('<Return>',startGame)
e.pack()

#set focus on entry box
e.focus_set()
root.mainloop()
