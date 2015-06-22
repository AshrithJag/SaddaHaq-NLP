from Tkinter import *
import os
root = Tk()


def printName(event):
    os.system('./tweets_sentiments_trends.sh 10')

button_1 = Button(root, text="Click me")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()
