import json
from Car import Car
from Field import Field
import numpy as np
from EventExecutor import EventExecutor


class StateReader:

    CARPOSX = "car_x"
    CARPOSY = "car_y"
    CARdx = "car_dx"
    CARdy = "car_dy"
    CARVELOCITY = "car_velocity"
    FIELDPATH = "field_path"
    STEPSIZE = "step_size"
    RESOLUTION = "resolution"

    def __init__(self, simfile):

        self.sim_path = simfile
        self.position = 0,0
        self.direction = 0,0
        self.velocity = 0
        self.field_path = ""
        self.step_size = 0
        self.resolution = 0

    def read(self):

        with open(self.sim_path) as data_file:
            data = json.load(data_file)

        self.position = (data[self.CARPOSX], data[self.CARPOSY])
        self. direction = (data[self.CARdx], data[self.CARdy])
        self.velocity = data[self.CARVELOCITY]
        self.field_path = str(data[self.FIELDPATH])
        self.step_size = data[self.STEPSIZE]
        self.resolution = data[self.RESOLUTION]

    def getState(self):

        car = Car(self.position[0], self.position[1], self.velocity)
        normaldirection = self.normalizeDirection(self.direction[0], self.direction[1])
        car.update_direction(normaldirection[0], normaldirection[1])
        field = Field(self.field_path, car, self.resolution)
        eventhandler = EventExecutor(self.calcAngle(self.direction[0], self.direction[1]), self.step_size)
        return car, field, eventhandler

    def calcAngle(self, dx, dy):
        return np.arctan(dy/dx)

    def normalizeDirection(self, dx, dy):

        length = np.sqrt(dx**2 + dy**2)
        return dx/length, dy/length
