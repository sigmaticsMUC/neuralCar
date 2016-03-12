from Tkinter import *
from PIL import ImageTk
import numpy as np
import Field
import Car
from EventExecutor import  EventExecutor
import Image
import sys


class CarPlotter:

    titleplot = "CarSim 0.1"

    def __init__(self, field, event):
        self.field = field
        self.car = field.car
        self.path = field.field_path
        self.root = Tk()
        self.event = event
        self.control_button_text = "STOP"

        im_width, im_height = self.field.field_image.size
        self.canvas = Canvas(self.root, width = im_width, height = im_height)

        image = ImageTk.PhotoImage(file = self.path)
        self.trackimage = self.canvas.create_image(10, 10, image = image, anchor = NW)

        #image2 = Image.open("car.png")
        #self.trackimage2 = self.canvas.create_image(100, 100, image = image3, anchor = NW)

        carx, cary = self.car.position
        self.carimg = self.canvas.create_oval(carx-10, cary-10, carx+10, cary+10, fill="red")

        self.right_button = Button(text = "right", command = self.event.turnright, anchor = W)
        self.left_button = Button(text = "left", command = self.event.turnleft, anchor = W)
        self.stop_button = Button(text = self.control_button_text, command = self.switch_active_state, anchor = W)

        self.canvas.pack(expand=YES, fill=BOTH)

        self.initCanvas()

        self.root.after(2000, self.simulate)
        self.root.mainloop()

    def initCanvas(self):
        self.root.title(self.titleplot)
        self.root.resizable(False,False)

        self.right_button.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        self.canvas.create_window(10, 15, anchor=NW, window=self.right_button)

        self.left_button.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        self.canvas.create_window(10, 40, anchor=NW, window=self.left_button)

        self.stop_button.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        self.canvas.create_window(10, 65, anchor=NW, window=self.stop_button)

    def simulate(self):
        if self.event.RUNNING:
            dx = np.cos(self.event.ANGLE)
            dy = np.sin(self.event.ANGLE)

            self.car.update_direction(dx, dy)

            nextcarpos = self.car.get_next_pos()

            validpos = self.field.checkpos(nextcarpos[0], nextcarpos[1])

            if validpos:
                self.canvas.create_line(self.car.position, nextcarpos, fill = "blue", width = 2)
                self.car.move()
                self.canvas.move(self.carimg, dx, dy)
                self.root.after(50, self.simulate)
            else:
                self.event.RUNNING = False


    def switch_active_state(self):
        if self.control_button_text == "STOP":
            self.control_button_text = "START"
        else:
            self.control_button_text = "STOP"

        self.stop_button.config(text = self.control_button_text)
        self.event.RUNNING = not self.event.RUNNING
        if self.event.RUNNING:
            self.root.after(50, self.simulate)




