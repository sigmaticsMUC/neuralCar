from Tkinter import *
from random import randint
from Tkinter import *
from PIL import ImageTk
import numpy as np
import Field
import Car

winkel = 0
step = 0.1

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")
        self.carone = Car.Car(180, 200, 1)

    def move_ball(self):
        dx = np.cos(winkel)
        dy = np.sin(winkel)


        self.carone.update_direction(dx, dy)
        x,y = self.carone.get_next_pos()


        field = Field.Field("Track1.png", self.carone)

        bool = field.checkpos(x,y)


        if bool:
            canvas.create_line(self.carone.position, self.carone.get_next_pos(), fill = "blue", width = 2)
            self.carone.move()
            self.canvas.move(self.ball, dx, dy)

           # self.canvas.after(50, self.move_ball)
        #else:
        #    print "FAIL"


def turnright():

    global winkel
    winkel = winkel +  step


def turnleft():

    global winkel
    winkel = winkel -  step

# initialize root Window and canvas
root = Tk()
root.title("Balls")
root.resizable(False,False)
canvas = Canvas(root, width = 750, height = 500)

canvas.pack(expand=YES, fill=BOTH)

image = ImageTk.PhotoImage(file = "Track1.png")
canvas.create_image(10, 10, image = image, anchor = NW)


button1 = Button(text = "right", command = turnright, anchor = W)
button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
button1_window = canvas.create_window(10, 15, anchor=NW, window=button1)

button2 = Button(text = "left", command = turnleft, anchor = W)
button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
button2_window = canvas.create_window(10, 40, anchor=NW, window=button2)

# create two ball objects and animate them
ball2 = Ball(canvas, 170, 190, 190, 210)

def ballmover():
    ball2.move_ball()
    root.after(50  , ballmover)


root.after(2000, ballmover)
root.mainloop()



