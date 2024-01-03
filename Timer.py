
import tkinter as tk
from tkinter import ttk
import sys
import os


HEIGHT = 2
WIDTH = 10


import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # Build up the UI
        self.label = tk.Label(root, height=HEIGHT, width=WIDTH, font=(
            "Impact", 35), bd=5, fg="white", bg="black", text="hey")
        self.label.pack(expand=True)

       # Establish the Variable and tell Tkinter to watch it 
        startButton = tk.Button(root, text="Restart", font=40, command=self.buttonpress)
        startButton.pack(expand= True, fill="x")

        # Initialize Button to False

        # Pass on arguments from Shell
        self.query = sys.argv[1]
        self.zeit = int(self.query)*60

        self.countdown()

    def buttonpress(self): # resets Time to original time
        self.zeit =  int(self.query)*60

    def countdown(self):
        if self.zeit >= 0:
            m, s = divmod(self.zeit, 60)
            h, m = divmod(m, 60)
            self.zeit -= 1
            self.label.config(text=str(h).zfill(2) + ":" +
                        str(m).zfill(2) + ":" + str(s).zfill(2))
            print(self.buttonpressed.get())
            self.label.after(1000, lambda: self.countdown())
        else:
            file = "./Alarm.mp3"
            os.system("mpg123 " + file)
            self.overtime()
    

    def overtime(self):
            m, s = divmod(self.zeit, 60)
            h, m = divmod(m, 60)
            self.zeit = self.zeit + 1
            self.label.config(text=str(h).zfill(2) + ":" +
                        str(m).zfill(2) + ":" + str(s).zfill(2))
            self.label.after(1000, lambda: self.overtime())

root = tk.Tk()
myapp = App(root)
root.title("Timer")
myapp.mainloop()

