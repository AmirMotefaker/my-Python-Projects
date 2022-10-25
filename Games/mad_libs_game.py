# Code by @AmirMotefaker

# Mad Libs Game

# Mad Libs is a phrasal template word game.

# Example:
# We start with a story, containing several blanked out words. Here’s a basic example:
# Rumble in the  _______.
# We then prompt the user to fill in the gaps, in this case, with a noun or place. We might end up with something like this:
# Rumble in the Toilet.


# Solution 1 - simple

food = input("Enter a type of food: ")
girl = input("Enter a girl's name: ")
adj1 = input("Enter an adjective: ")
bird = input("Enter a noun: ")
verb1 = input("Enter a verb in the past tense: ")
verb2 = input("Enter another verb in the past tense: ")
verb3 = input("Enter a third verb in the past tense: ")
noun1 = input("Enter a noun: ")
story = "It was " + food + " day at school, and " + girl + " was super " + adj1 + " for lunch. But when she went outside to eat, a " + bird + " stole her " + food + "! " + girl + " chased the " + bird + " all over school. She " + verb1 + ", " + verb2 + ", and " + verb3 + " through the playground. Then she tripped on her " + noun1 + " and the " + bird + " escaped! Luckily, " + girl + "'s friends were willing to share their " + food + " with her."
 
print(story)


# Solution 2 - advanced(Tkinter)
# The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit.

# step-by-step:
# 1. Install Tkinter
# 2. Initializing window
# 3. Creatine functions
# 4. Creating buttons

# Tk(): It helps in displaying the window on the screen.
# title(): It displays the title in the parentheses on the top of the window.
# geometry(): It defines the geometry of the screen.
# config(): It sets the background colour of the window.
# Button(): It displays buttons on the window.
# mainloop(): It is useful in running the event loop.

# Story1() function will take the desired input from the user and display it on the screen.text contains the story.
# Label(): It prints the text in the parentheses on the window.
# Entry(): It provides a textarea.
# get(): It helps to get the value of the variable.
# place(): It sets the position of a text , textarea on the screen.

# Story2() does the same function as Story1(). The only difference is in the story.


from tkinter import *

def Story1(win):
  def final(tl: Toplevel, name, sports, City, playername, drinkname, snacks):

    text = f'''
       One day me and my friend {name} decided to play a {sports} game in {City}.
       But we were not able to play.So, we went to watch the game and our favourite player {playername}.
       We drank {drinkname} and also ate some {snacks} 
       We really enjoyed it! We are looking forward to go again and enjoy '''

    tl.geometry(newGeometry='500x550')

    Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
    Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)

  NewScreen = Toplevel(win, bg='Green')
  NewScreen.title("A Memorable Day")
  NewScreen.geometry('500x500')
  Label(NewScreen, text=' A Memorable Day').place(x=100, y=1)
  Label(NewScreen, text='Name:').place(x=1, y=35)
  Label(NewScreen, text='Enter a game:').place(x=1, y=70)
  Label(NewScreen, text='Enter a city:').place(x=1, y=110)
  Label(NewScreen, text='Enter the name of a player:').place(x=1, y=150)
  Label(NewScreen, text='Enter the name of a drink:').place(x=1, y=190)
  Label(NewScreen, text='Enter the name of a snack:').place(x=1, y=230)
  Name = Entry(NewScreen, width=17)
  Name.place(x=250, y=35)
  game = Entry(NewScreen, width=17)
  game.place(x=250, y=70)
  city = Entry(NewScreen, width=17)
  city.place(x=250, y=105)
  player = Entry(NewScreen, width=17)
  player.place(x=250, y=150)
  drink = Entry(NewScreen, width=17)
  drink.place(x=250, y=190)
  snack = Entry(NewScreen, width=17)
  snack.place(x=250, y=220)
  SubmitButton = Button(NewScreen, text="Submit", background="Yellow", font=('Times', 12), command=lambda:final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
  SubmitButton.place(x=150, y=270)

  NewScreen.mainloop()

def Story2(win):
    def final(tl: Toplevel, profession, noun, feeling, emotion,verb):
            text = f'''
            When I was a child, I wanted to become a {profession}
          but as I grew up I got into the {noun} and decided to become an
          engineer. Then I went into a job that I was not {feeling} at.
          After getting {emotion} I decided to do what I love.
          Despite getting lower{verb} than I used to get in my previous job.I am very
          feeling '''

            tl.geometry(newGeometry='500x550')

            Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
            Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
    NewScreen = Toplevel(win, bg='red')
    NewScreen.title("Ambitions")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='Ambitions').place(x=150, y=1)
    Label(NewScreen, text='Enter a profession:').place(x=1, y=35)
    Label(NewScreen, text='Enter a noun:').place(x=1, y=70)
    Label(NewScreen, text='Enter a feeling:').place(x=1, y=110)
    Label(NewScreen, text='Enter a emotion:').place(x=1, y=150)
    Label(NewScreen, text='Enter a verb:').place(x=1, y=190)
    Profession = Entry(NewScreen, width=17)
    Profession.place(x=250, y=35)
    Noun = Entry(NewScreen, width=17)
    Noun.place(x=250, y=70)
    Feeling = Entry(NewScreen, width=17)
    Feeling.place(x=250, y=105)
    Emotion= Entry(NewScreen, width=17)
    Emotion.place(x=250, y=150)
    Verb = Entry(NewScreen, width=17)
    Verb.place(x=250, y=190)
    SubmitButton = Button(NewScreen, text="Submit", background="Yellow", font=('Times', 12), command=lambda:final(NewScreen, Profession.get(), Noun.get(), Feeling.get(), Emotion.get(), Verb.get()))
    SubmitButton.place(x=150, y=270)
  

Screen = Tk()
Screen.title("AmirMotefaker Mad Libs Generator")
Screen.geometry('400x400')
Screen.config(bg="White")
Label(Screen, text='AmirMotefaker Mad Libs Generator').place(x=100, y=20)
Story1Button = Button(Screen, text='A memorable day', font=("Times New Roman", 13),command=lambda: Story1(Screen),bg='Green')
Story1Button.place(x=140, y=90)
Story2Button = Button(Screen, text='Ambitions', font=("Times New Roman", 13),command=lambda: Story2(Screen), bg='Red')
Story2Button.place(x=160, y=150)

Screen.update()
Screen.mainloop()
