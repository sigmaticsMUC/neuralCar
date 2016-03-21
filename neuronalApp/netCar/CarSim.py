from CarPlotter import CarPlotter
from Field import Field
from Car import Car
from EventExecutor import EventExecutor
from thread import start_new_thread
import numpy as np
import threading
import time
from StateReader import StateReader


simfile = "../../external/data.json"
state_reader = StateReader(simfile)
state_reader.read()
car, field, event = state_reader.getState()
last = 0

# this function will be started in a thread
# and it will be responsible for reading NN output and passing it to the EventExecutor object
def actions():

    time.sleep(2.5)
    pass
    #'''
    while True:
        time.sleep(0.05)
        while not event.RUNNING:
            pass
        front = field.getBoundaryDistanceFront()
        distance = field.getBoundaryDistanceSides()
        #print front
        if distance[0] < distance[1] and front < 0.75*(distance[0]+distance[1]):
            event.turnleft()
        elif distance[0] > distance[1] and front < 0.75*(distance[0]+distance[1]):
            event.turnright()
        else:
            pass
    #'''


def simulate():

    time.sleep(2)
    while True:
        time.sleep(0.05)
        if event.RUNNING:
            dx = np.cos(event.ANGLE)
            dy = np.sin(event.ANGLE)

            car.update_direction(dx, dy)

            nextcarpos = car.get_next_pos()

            validpos = field.checkpos(nextcarpos[0], nextcarpos[1])

            if validpos:
                print "HI"
                car.move()
            else:
                print "Stop"
                event.RUNNING = False





def start_simulation():

    try:
        t=threading.Thread(target=actions)
        t.daemon = True  # set thread to daemon ('ok' won't be printed in this case)

        g=threading.Thread(target=simulate)
        g.daemon = True

        t.start()
        g.start()

        pltobj = CarPlotter(field, event)

    except:
        print "Error: unable to start thread"

