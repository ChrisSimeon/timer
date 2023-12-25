
import tkinter as tk
from tkinter import ttk
import time
import sys
import os


HEIGHT = 2
WIDTH = 10




def buttonpress():
    buttonpressed = True
    print ("Yes")

def countdown():
    query = sys.argv[1]
    #query = 1
    zeit = int(query)*60
    global buttonpressed
    buttonpressed= False

    def timetime(zeit):
        if zeit >= 0:
            m, s = divmod(zeit, 60)
            h, m = divmod(m, 60)
            zeit = zeit - 1
            label.config(text=str(h).zfill(2) + ":" +
                        str(m).zfill(2) + ":" + str(s).zfill(2))
            if not buttonpressed:
                label.after(1000, timetime(zeit))
            else: 
                buttonpressed = False
                label.after(1000, timetime(int(query)*60))
        else:
            file = "./Alarm.mp3"
            os.system("mpg123 " + file)
            zeit = 0
            overtime(zeit)

    def overtime(zeit):
        m, s = divmod(zeit, 60)
        h, m = divmod(m, 60)
        zeit = zeit + 1
        label.config(text=str(h).zfill(2) + ":" +
                     str(m).zfill(2) + ":" + str(s).zfill(2))
        label.after(1000, lambda: overtime(zeit))

    timetime(zeit)

# Grundfenster
root = tk.Tk()
root.title("Timer")

# Inhalt
label = tk.Label(root, height=HEIGHT, width=WIDTH, font=(
    "Impact", 35), bd=5, fg="white", bg="black", text="hey")
label.pack(expand=True)

restartButton = tk.Button(root, text="Restart", font=40, command=buttonpress)
restartButton.pack(expand= True, fill="x")


countdown()


root.mainloop()
