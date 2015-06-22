from Tkinter import *
import os


def printName(event):
    os.system('./tweets_sentiments_trends.sh 10')

def printTrends(event):
    os.system('python get_trends.py')

def printText(event):
    os.system('python get_trends.py')
    f= open("trends.txt")
    t = Text(bottom, fg="red")
    #t is a Text widget
    t.insert(1.0, f.read())
    t.pack()
    f.close()
    

root = Tk()
#theLabel = Label(root, text="This is the start")
#theLabel.pack()
top = Frame(root)
top.pack()
bottom = Frame(root)
bottom.pack(side=BOTTOM)

button1 = Button(top, text="Sentiment Scores and Tweets", fg="red")
button1.bind("<Button-1>", printName)

button2 = Button(top, text="Get the trends", fg="blue")
button2.bind("<Button-1>", printTrends)

button3 = Button(top, text="Button 3", fg="green")
button3.bind("<Button-1>", printText)

button4 = Button(top, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
