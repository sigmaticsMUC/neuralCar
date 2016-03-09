from CarPlotter import CarPlotter
from Field import Field
from Car import Car
from Events import Events
from thread import start_new_thread
import numpy as np
import threading
import time




car = Car(100, 200, 1)
field = Field("../../external/Track2.png", car)
event = Events()



def actions():

    print "Started"
    global event
    time.sleep(2)
    for i in range(10):
        time.sleep(0.1)
        event.turnright()

    time.sleep(1)

    for i in range(50):
        time.sleep(0.1)
        event.turnleft()

    print event.ANGLE


try:

    t=threading.Thread(target=actions)
    t.daemon = True  # set thread to daemon ('ok' won't be printed in this case)
    t.start()
except:
    print "Error: unable to start thread"

pltobj = CarPlotter(field, event)
