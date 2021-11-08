# Group 4 Unessay Project
# Authors: Sahil Brar, Roshan Shankar, Abel Tekeste, Maria Martine Baclig
# Password Hacking/Guessing Game with useful hints and techniques taught in class

import tkinter as tk
import random
from tkinter import ttk
from PIL import ImageTk, Image

# Setup variables for GUI
LARGE_FONT = ("Consolas", 15)
HEADER_FONT = ("Consolas", 20)
PROFILE_FONT = ("Consolas", 13)
BACKGROUND_COLOR = "#80c1ff"
HEIGHT = 600
WIDTH = 800

# Initialize list for profiles used during game session to prevent replay
usedProfilesHard = []
usedProfilesEasy = []

# Function to setup the game GUI
class Game(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Password Game")

        container = tk.Frame(self)

        container.pack(side="top", fill ="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, EasyMode, HardMode, successScreen, failScreen):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]

# Class the start page of the game, mostly GUI and button placements
class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        tk.Frame.tk_setPalette(self, "black")

        load = Image.open("background.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(relwidth=1, relheight=1)

        lower_frame = tk.Frame(self, bg=BACKGROUND_COLOR, bd=5)
        lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.4, anchor='n')

        higher_frame = tk.Frame(self, bg=BACKGROUND_COLOR, bd=5)
        higher_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

        # title
        label = tk.Label(higher_frame, text="Welcome to the password guessing game. \n Choose a level below:",
                         font=LARGE_FONT, bg=BACKGROUND_COLOR)
        label.place(relwidth=1, relheight=1)

        # Easy mode button
        button1 = tk.Button(lower_frame, text="EASY MODE", font=LARGE_FONT, bg="green",
                            command=lambda: controller.show_frame(EasyMode))
        button1.place(relwidth=1, relheight=0.5)

        # Hard mode button
        button2 = tk.Button(lower_frame, text="HARD MODE", font=LARGE_FONT, bg="red",
                            command=lambda: controller.show_frame(HardMode))
        button2.place(rely=0.5, relwidth=1, relheight=0.5)

#---Class for easy mode of the game--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class EasyMode(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH) #to fix screen dimensions
        canvas.pack()

        load = Image.open("background.jpg") #set background image
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0, relwidth=1, relheight=1)

        higher_frame = tk.Frame(self, bg=BACKGROUND_COLOR, bd=5) #set top header frame
        higher_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        lower_frame = tk.Frame(self, bg=BACKGROUND_COLOR, bd=5) #set body frame
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')

        easyLabel = tk.Label(higher_frame, text="EASY MODE", font=HEADER_FONT, bg="green")
        easyLabel.place(relheight=1, relwidth=1)
        self.i = 1
        # Randomly select which user to hack
        self.choice = random.randint(1, 8)
        usedProfilesEasy.append(self.choice)
        if self.choice == 1:
            self.PROFILE = "Ryan Henry"
            self.PASSWORD = "shredder"
            self.HINT = "Ryan's dog is named after a popular Teenage Mutant Ninja Turtles villain."

        if self.choice == 2:
            self.PROFILE = "Mr. Chow"
            self.PASSWORD = "123456"
            self.HINT = "Most used PASSWORD in the world."

        if self.choice == 3:
            self.PROFILE = "Alan Turing"
            self.PASSWORD = "honey"
            self.HINT = "Winnie the pooh's favorite food."

        if self.choice == 4:
            self.PROFILE = "Scarlett"
            self.PASSWORD = "paris"
            self.HINT = "Love capital of the world."
        
        if self.choice == 5:
            self.PROFILE = "Miss Martha Thompson"
            self.PASSWORD = "qwerty"
            self.HINT = "One of the most used passwords in 2019."
        
        if self.choice == 6:
            self.PROFILE = "Babe Ruth"
            self.PASSWORD = "baseball"
            self.HINT = "Favorite sport."
        
        if self.choice == 7:
            self.PROFILE = "Betty"
            self.PASSWORD = "abc123"
            self.HINT = "Love the alphabet and counting."

        if self.choice == 8:
            self.PROFILE = "Isaiah Odom"
            self.PASSWORD = "batman"
            self.HINT = "Bruce Wayne's alter ego."

        self.display_pass = self.PASSWORD
        # length of PASSWORD to be displayed
        for j in range(0, len(self.display_pass)):
            # Change the PASSWORD to a list (can't change strings in python)
            self.display_pass = list(self.display_pass)
            # Replace the letter to be hidden
            self.display_pass[j] = "*"
            # Change list back into string
            self.display_pass = "".join(self.display_pass)

        load = Image.open("profile_180.png") #set profile image
        render = ImageTk.PhotoImage(load)
        img = tk.Label(lower_frame, bg=BACKGROUND_COLOR, image=render, height=180, width=180)
        img.image = render
        img.place(relwidth=1, rely=0)

        self.profileText = tk.StringVar()
        self.profileText.set("Profile: " + self.PROFILE)
        self.profileLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=PROFILE_FONT, textvariable=self.profileText)\
            .place(rely=0.45, relx=0.01) #profile placement

        self.hintLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=PROFILE_FONT, text="Hint: ").place(
            rely=0.5, relx=0.01) #hint placement

        hint_frame = tk.Frame(lower_frame, bg=BACKGROUND_COLOR)  # set hint body frame
        hint_frame.place(rely=0.51, relx=0.1, relheight=0.15, relwidth=0.87)

        self.hintScroll = tk.Scrollbar(hint_frame) #set scrollbar in hint body
        self.hintScroll.pack(side='right', fill='y')
        self.hintText = tk.Text(hint_frame, bg=BACKGROUND_COLOR, wrap="word", font=PROFILE_FONT) #set hint body text
        self.hintText.pack(side="left", fill="y")
        self.hintScroll.config(command=self.hintText.yview)
        self.hintText.insert(tk.END, self.HINT)
        self.hintText.config(yscrollcommand=self.hintScroll.set, state="disabled")

        self.labelText = tk.StringVar()
        self.labelText.set("Your guess:")
        self.guessLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=LARGE_FONT, textvariable=self.labelText)
        self.guessLabel.place(rely=0.72, relx=0.01, relheight=0.18) #guess prompt placement

        self.directory = tk.StringVar(None)
        self.guessEntry = tk.Entry(lower_frame, bg=BACKGROUND_COLOR, font=LARGE_FONT, textvariable=self.directory, width=30)
        self.guessEntry.place(rely=0.77, relx=0.22, relheight=0.08, relwidth=0.4) #user guess placement

        self.displayText = tk.StringVar()
        self.displayText.set(self.display_pass)
        self.displayLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=LARGE_FONT, textvariable=self.displayText) \
            .place(rely=0.7, relx=0.22)  #password length placement
        self.displayLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=LARGE_FONT, text="Password:") \
            .place(rely=0.7, relx=0.01)  #password prompt placement

        self.enterButton = tk.Button(lower_frame, bg=BACKGROUND_COLOR, font=LARGE_FONT, text="ENTER", command=lambda: self.checkGuess(controller))\
            .place(rely=0.75, relx=0.85, relheight=0.12) #enter button placement

        self.attemptsText = tk.StringVar()
        self.attemptsText.set("Attempt: " + str(self.i) +"/10")
        self.attemptsLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=PROFILE_FONT, textvariable=self.attemptsText)\
            .place(rely=0.75, relx=0.63, relheight=0.12) #attempt counter placement

        self.tryText = tk.StringVar()
        self.tryText.set("")
        self.tryLabel = tk.Label(lower_frame, font=LARGE_FONT, bg=BACKGROUND_COLOR, textvariable=self.tryText)\
            .place(rely=0.88, relx=0.22, relheight=0.1, relwidth=0.4) #feedback string placement

        self.backButton = tk.Button(lower_frame, font=LARGE_FONT, bg=BACKGROUND_COLOR, text="< Back", command=lambda: self.backToMain(controller))\
            .place(rely=0.88, relx=0.01, relheight=0.1, relwidth=0.15) #back button placement

        self.reloadButton = tk.Button(lower_frame, font=LARGE_FONT, bg=BACKGROUND_COLOR, text="RESET",
                                    command=lambda: self.reloadEasy(controller)) \
            .place(rely=0.88, relx=0.85, relheight=0.12)  #reload button placement


    def checkGuess(self, contr):
        if self.i <= 10:
            guess = self.guessEntry.get() 
            if self.i == 10 and guess != self.PASSWORD:
                self.i = self.i + 1
                self.attemptsText.set("Attempt: " + str(self.i) + "/10")
                contr.show_frame(failScreen)
            else:
                if self.PASSWORD == guess:
                    self.i = self.i + 1
                    self.attemptsText.set(
                        "Attempt: " + str(self.i) + "/10")
                    contr.show_frame(successScreen)
                else:
                    if len(guess) == len(self.PASSWORD):
                        for j in range(0, len(self.PASSWORD)):
                            # Check each char, if the same then replace
                            if guess[j] == self.PASSWORD[j]:
                                # Change the PASSWORD to a list (can't change strings in python)
                                self.display_pass = list(self.display_pass)
                                # Replace the corresponding char
                                self.display_pass[j] = guess[j]
                                # Change list back into string
                                self.display_pass = "".join(self.display_pass)
                        self.displayText.set(self.display_pass)
                        self.i = self.i + 1
                        self.tryText.set("Try Again!")
                        self.attemptsText.set("Attempt: " + str(self.i)  + "/10")
                    else:
                        # length is not the same as the password
                        if len(guess) > len(self.PASSWORD):
                            self.tryText.set("Too many characters!")
                        else:
                            self.tryText.set("Too few characters!")
        else:
            contr.show_frame(failScreen)

    def reset(self):
        self.hintText.config(state="normal")
        self.hintText.delete("1.0", tk.END)
        while True:
            self.choice = random.randint(1, 8)
            if self.choice in usedProfilesEasy:
                self.choice = random.randint(1, 8)
            else:
                self.i = 1
                usedProfilesEasy.append(self.choice)
                if self.choice == 1:
                    self.PROFILE = "Ryan Henry"
                    self.PASSWORD = "shredder"
                    self.HINT = "Ryan's dog is named after a popular Teenage Mutant Ninja Turtles villain."

                if self.choice == 2:
                    self.PROFILE = "Mr. Chow"
                    self.PASSWORD = "123456"
                    self.HINT = "Most used PASSWORD in the world."

                if self.choice == 3:
                    self.PROFILE = "Alan Turing"
                    self.PASSWORD = "honey"
                    self.HINT = "Winnie the pooh's favorite food."

                if self.choice == 4:
                    self.PROFILE = "Scarlett"
                    self.PASSWORD = "paris"
                    self.HINT = "Love capital of the world."

                if self.choice == 5:
                    self.PROFILE = "Miss Martha Thompson"
                    self.PASSWORD = "qwerty"
                    self.HINT = "One of the most used passwords in 2019."
        
                if self.choice == 6:
                    self.PROFILE = "Babe Ruth"
                    self.PASSWORD = "baseball"
                    self.HINT = "Favorite sport"
        
                if self.choice == 7:
                    self.PROFILE = "Betty"
                    self.PASSWORD = "abc123"
                    self.HINT = "Love the alphabet and counting"

                if self.choice == 8:
                    self.PROFILE = "Isaiah Odom"
                    self.PASSWORD = "batman"
                    self.HINT = "Bruce Wayne's alter ego."
                break
        self.display_pass = self.PASSWORD
        # length of PASSWORD to be displayed
        for j in range(0, len(self.display_pass)):
            # Change the PASSWORD to a list (can't change strings in python)
            self.display_pass = list(self.display_pass)
            # Replace the letter to be hidden
            self.display_pass[j] = "*"
            # Change list back into string
            self.display_pass = "".join(self.display_pass)
        self.profileText.set("Profile: " + self.PROFILE)
        self.attemptsText.set("Attempt: " + str(self.i) + "/10")
        self.tryText.set("")
        self.hintText.insert(tk.END, self.HINT)
        self.hintText.config(state="disabled")
        self.displayText.set(self.display_pass)
        self.guessEntry.delete(0, 'end')

    def getAttempts(self):
        return self.i

    def backToMain(self, contr):
        self.reset()
        contr.show_frame(StartPage)

    def reloadEasy(self, contr):
        if len(usedProfilesEasy) < 8:
            self.reset()
        else:
            usedProfilesEasy.clear()
            contr.show_frame(StartPage)


    
#---Class for hard mode of the game-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class HardMode(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        load = Image.open("background.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0, relwidth=1, relheight=1)

        higher_frame = tk.Frame(self, bg=BACKGROUND_COLOR, bd=5)
        higher_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        lower_frame = tk.Frame(self, bg=BACKGROUND_COLOR, bd=5)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')

        hardLabel = tk.Label(higher_frame, text="HARD MODE", font=HEADER_FONT, bg="red")
        hardLabel.place(relheight=1, relwidth=1)
        
        self.i = 1
        # Randomly select which user to hack
        self.choice = random.randint(1, 8)
        usedProfilesHard.append(self.choice)
        if self.choice == 1:
            self.PROFILE = "Kate Upton"
            self.PASSWORD = "C00kieMonst3r"
            self.HINT = "Sesame Street character who loves cookies. Some letters may be numbers."

        if self.choice == 2:
            self.PROFILE = "Wolfgang Amadeus Mozart"
            self.PASSWORD = "!Lov3MyPian0"
            self.HINT = "I ____ my _____. A musical instrument in which strings are struck by a wooden hammer and played using keys."

        if self.choice == 3:
            self.PROFILE = "Steve Jobs"
            self.PASSWORD = "Loo00ool"
            self.HINT = "Text reaction to a funny message. Some letters may be numbers."

        if self.choice == 4:
            self.PROFILE = "Seth Rogen"
            self.PASSWORD = "Sno0pD0gg420"
            self.HINT = "Favorite rapping dog in Hip Hop. Last three digits are numbers"

        if self.choice == 5:
            self.PROFILE = "Zachary Byrd"
            self.PASSWORD = "@8cD3fGh!"
            self.HINT = "Alphabet with a twist"

        if self.choice == 6:
            self.PROFILE = "Corey Oakley"
            self.PASSWORD = "vanillaIphoneEarth"
            self.HINT = "Ice cream flavor, type of phone, planet. (No spaces)"

        if self.choice == 7:
            self.PROFILE = "Conrad"
            self.PASSWORD = "Un!corn123"
            self.HINT = "Legendary creature with a horn projecting from its forehead. Last 3 characters may be numbers."

        if self.choice == 8:
            self.PROFILE = "Olivia Grace"
            self.PASSWORD = "$t@rbuck$101"
            self.HINT = "Favorite place to get coffee. Last 3 characters may be numbers."

        self.display_pass = self.PASSWORD
        # length of PASSWORD to be displayed
        for j in range(0, len(self.display_pass)):
            # Change the PASSWORD to a list (can't change strings in python)
            self.display_pass = list(self.display_pass)
            # Replace the letter to be hidden
            self.display_pass[j] = "*"
            # Change list back into string
            self.display_pass = "".join(self.display_pass)

        load = Image.open("profile_180.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(lower_frame, bg=BACKGROUND_COLOR, image=render, height=180, width=180)
        img.image = render
        img.place(relwidth=1, rely=0)

        self.profileText = tk.StringVar()
        self.profileText.set("Profile: " + self.PROFILE)
        self.profileLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=PROFILE_FONT,
                                     textvariable=self.profileText) \
            .place(rely=0.45, relx=0.01)  # profile placement

        self.hintLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=PROFILE_FONT, text="Hint: ").place(
            rely=0.5, relx=0.01)  # hint placement

        hint_frame = tk.Frame(lower_frame, bg=BACKGROUND_COLOR)  # set hint body frame
        hint_frame.place(rely=0.51, relx=0.1, relheight=0.15, relwidth=0.87)

        self.hintScroll = tk.Scrollbar(hint_frame)  # set scrollbar in hint body
        self.hintScroll.pack(side='right', fill='y')
        self.hintText = tk.Text(hint_frame, bg=BACKGROUND_COLOR, wrap="word", font=PROFILE_FONT)  # set hint body text
        self.hintText.pack(side="left", fill="y")
        self.hintScroll.config(command=self.hintText.yview)
        self.hintText.config(yscrollcommand=self.hintScroll.set)
        self.hintText.insert(tk.END, self.HINT)

        self.labelText = tk.StringVar()
        self.labelText.set("Your guess:")
        self.guessLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=LARGE_FONT, textvariable=self.labelText)
        self.guessLabel.place(rely=0.72, relx=0.01, relheight=0.18)

        self.directory = tk.StringVar(None)
        self.guessEntry = tk.Entry(lower_frame, bg=BACKGROUND_COLOR, font=LARGE_FONT, textvariable=self.directory,
                                   width=30)
        self.guessEntry.place(rely=0.77, relx=0.22, relheight=0.08, relwidth=0.4)

        self.displayText = tk.StringVar()
        self.displayText.set(self.display_pass)
        self.displayLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=LARGE_FONT, textvariable=self.displayText) \
            .place(rely=0.7, relx=0.22)  # password length placement
        self.displayLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=LARGE_FONT, text="Password:") \
            .place(rely=0.7, relx=0.01)  # password prompt placement

        self.enterButton = tk.Button(lower_frame, bg=BACKGROUND_COLOR, font=LARGE_FONT, text="ENTER",
                                     command=lambda: self.checkGuess(controller)) \
            .place(rely=0.75, relx=0.85, relheight=0.12)

        self.attemptsText = tk.StringVar()
        self.attemptsText.set("Attempt: " + str(self.i) + "/10")
        self.attemptsLabel = tk.Label(lower_frame, bg=BACKGROUND_COLOR, font=PROFILE_FONT,
                                      textvariable=self.attemptsText) \
            .place(rely=0.75, relx=0.63, relheight=0.12)

        self.tryText = tk.StringVar()
        self.tryText.set("")
        self.tryLabel = tk.Label(lower_frame, font=LARGE_FONT, bg=BACKGROUND_COLOR, textvariable=self.tryText) \
            .place(rely=0.88, relx=0.22, relheight=0.1, relwidth=0.4)

        self.backButton = tk.Button(lower_frame, font=LARGE_FONT, bg=BACKGROUND_COLOR, text="< Back",
                                    command=lambda: self.backToMain(controller)) \
            .place(rely=0.88, relx=0.01, relheight=0.1, relwidth=0.15)

        self.reloadButton = tk.Button(lower_frame, font=LARGE_FONT, bg=BACKGROUND_COLOR, text="RESET",
                                      command=lambda: self.reloadHard(controller)) \
            .place(rely=0.88, relx=0.85, relheight=0.12)  # reload button placement

    def checkGuess(self, contr):
        if self.i <= 10:
            guess = self.guessEntry.get()
            if self.i == 10 and guess != self.PASSWORD:
                contr.show_frame(failScreen)
            else:
                if self.PASSWORD == guess:
                    self.i = self.i +1 
                    self.attemptsText.set(
                        "Attempt: " + str(self.i) + "/10")
                    contr.show_frame(successScreen)
                else:
                    if len(guess) == len(self.PASSWORD):
                        for j in range(0, len(self.PASSWORD)):
                            # Check each char, if the same then replace
                            if guess[j] == self.PASSWORD[j]:
                                # Change the PASSWORD to a list (can't change strings in python)
                                self.display_pass = list(self.display_pass)
                                # Replace the corresponding char
                                self.display_pass[j] = guess[j]
                                # Change list back into string
                                self.display_pass = "".join(self.display_pass)
                        self.displayText.set(self.display_pass)
                        self.i = self.i + 1
                        self.tryText.set("Try Again!")
                        self.attemptsText.set(
                            "Attempt: " + str(self.i) + "/10")
                    else:
                        # length is not the same as the password
                        if len(guess) > len(self.PASSWORD):
                            self.tryText.set("Too many characters!")
                        else:
                            self.tryText.set("Too few characters!")
        else:
            contr.show_frame(failScreen)
    
    def reset(self):
        self.hintText.config(state="normal")
        self.hintText.delete("1.0", tk.END)
        while True:
            self.choice = random.randint(1, 8)
            if self.choice in usedProfilesHard:
                self.choice = random.randint(1, 8)
            else:
                self.i = 1
                usedProfilesHard.append(self.choice)
                if self.choice == 1:
                    self.PROFILE = "Kate Upton"
                    self.PASSWORD = "C00kieMonst3r"
                    self.HINT = "Sesame Street character who loves cookies. Some letters may be numbers."

                if self.choice == 2:
                    self.PROFILE = "Wolfgang Amadeus Mozart"
                    self.PASSWORD = "!Lov3MyPian0"
                    self.HINT = "I ____ my _____. A musical instrument in which strings are struck by a wooden hammer and played using keys."

                if self.choice == 3:
                    self.PROFILE = "Steve Jobs"
                    self.PASSWORD = "Loo00ool"
                    self.HINT = "Text reaction to a funny message. Some letters may be numbers."

                if self.choice == 4:
                    self.PROFILE = "Seth Rogen"
                    self.PASSWORD = "Sn00pD0gg420"
                    self.HINT = "Favorite rapping dog in Hip Hop. Last three digits are numbers"

                if self.choice == 5:
                    self.PROFILE = "Zachary Byrd"
                    self.PASSWORD = "@8cD3fGh!"
                    self.HINT = "Alphabet with a twist"

                if self.choice == 6:
                    self.PROFILE = "Corey Oakley"
                    self.PASSWORD = "vanillaIphoneEarth"
                    self.HINT = "Ice cream flavor, type of phone, planet. (No spaces)"

                if self.choice == 7:
                    self.PROFILE = "Conrad"
                    self.PASSWORD = "Un!corn123"
                    self.HINT = "Legendary creature with a horn projecting from its forehead. Last 3 characters may be numebers."

                if self.choice == 8:
                    self.PROFILE = "Olivia Grace"
                    self.PASSWORD = "$t@rbuck$101"
                    self.HINT = "Favorite place to get coffee. Last 3 characters may be numbers."
                break
        self.display_pass = self.PASSWORD
        # length of PASSWORD to be displayed
        for j in range(0, len(self.display_pass)):
            # Change the PASSWORD to a list (can't change strings in python)
            self.display_pass = list(self.display_pass)
            # Replace the letter to be hidden
            self.display_pass[j] = "*"
            # Change list back into string
            self.display_pass = "".join(self.display_pass)
        self.profileText.set("Profile: " + self.PROFILE)
        self.attemptsText.set("Attempt: " + str(self.i) + "/10")
        self.tryText.set("")
        self.hintText.insert(tk.END, self.HINT)
        self.hintText.config(state="disabled")
        self.displayText.set(self.display_pass)
        self.guessEntry.delete(0, 'end')

    def getAttempts(self):
        return self.i

    def backToMain(self, contr):
        self.reset()
        contr.show_frame(StartPage)

    def reloadHard(self,contr):
        if len(usedProfilesHard) < 8:
            self.reset()
        else:
            usedProfilesHard.clear()
            contr.show_frame(StartPage)

#---Class for successfully completeing game----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class successScreen(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        load = Image.open("background.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0, relwidth=1, relheight=1)

        higher_frame = tk.Frame(self, bg=BACKGROUND_COLOR, bd=5)
        higher_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        lower_frame = tk.Frame(self, bg=BACKGROUND_COLOR, bd=5)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')

        label = tk.Label(higher_frame, bg=BACKGROUND_COLOR, text="You got the right password!", font=LARGE_FONT)
        label.place(relwidth=1, relheight=1)
        backButton = tk.Button(lower_frame, text="Back to main page", font=LARGE_FONT, bg="black",
                               command=lambda: self.resetToMain(controller))
        backButton.place(relheight=0.5, relwidth=1, rely=0.5)

        playAgainButton = tk.Button(lower_frame, text="Play Again", font=LARGE_FONT, bg="purple",
                                    command=lambda: self.playAgain(controller))
        playAgainButton.place(relwidth=1, relheight=0.5)

        self.playAgain(controller)

     def playAgain(self, contr):
         easy = contr.get_page(EasyMode)
         hard = contr.get_page(HardMode)
         if easy.getAttempts() != 1:
             easy.reloadEasy(contr)
             contr.show_frame(EasyMode)
         if hard.getAttempts() != 1:
             hard.reloadHard(contr)
             contr.show_frame(HardMode)


     def resetToMain(self, contr):
        easy = contr.get_page(EasyMode)
        hard = contr.get_page(HardMode)
        if easy.getAttempts() != 1:
            print(easy.getAttempts())
            easy.reloadEasy(contr)
        if hard.getAttempts() != 1:
            hard.reloadHard(contr)
        

#---Class for unsucessfully completing the game----------------------------------------------------------------------------------------------------------------------------------------------------------------
class failScreen(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, height=HEIGHT, width=WIDTH)
        canvas.pack()

        load = Image.open("background.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0, relwidth=1, relheight=1)

        higher_frame = tk.Frame(self, bg=BACKGROUND_COLOR, bd=5)
        higher_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        lower_frame = tk.Frame(self, bg=BACKGROUND_COLOR, bd=5)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')

        label = tk.Label(higher_frame, bg=BACKGROUND_COLOR, text="You ran out of attempts.", font=LARGE_FONT)
        label.place(relwidth=1, relheight=1)
        backButton = tk.Button(lower_frame, text="Back to main page", font=LARGE_FONT, bg="black",
                               command=lambda: self.resetToMain(controller))
        backButton.place(relheight=0.5, relwidth=1, rely=0.5)

        playAgainButton = tk.Button(lower_frame, text="Play Again", font=LARGE_FONT, bg="purple",
                                    command=lambda: self.playAgain(controller))
        playAgainButton.place(relwidth=1, relheight=0.5)

        self.playAgain(controller)

     def playAgain(self, contr):
         easy = contr.get_page(EasyMode)
         hard = contr.get_page(HardMode)
         if easy.getAttempts() != 1:
             easy.reset()
             contr.show_frame(EasyMode)
         else:
             hard.reset()
             contr.show_frame(HardMode)

     def resetToMain(self, contr):
        easy = contr.get_page(EasyMode)
        hard = contr.get_page(HardMode)
        if easy.getAttempts() != 1:
            easy.reset()
        if hard.getAttempts() != 1:
            hard.reset()
        contr.show_frame(StartPage)

# Start the game and the pop up window application
app = Game()
app.mainloop()
