import json
import numpy as np

from neuronalApp.netCar.simCar.Car import Car
from neuronalApp.netCar.simCar.Field import Field

from neuronalApp.netCar.abstractNetCar.EventExecutor import EventExecutor


class StateReader:

    CARPOSX = "car_x"
    CARPOSY = "car_y"
    CARdx = "car_dx"
    CARdy = "car_dy"
    CARVELOCITY = "car_velocity"
    FIELDPATH = "field_path"
    STEPSIZE = "step_size"
    RESOLUTION = "resolution"
    REACTIONTIME = "reaction_time"
    TRACKING = "track_data"

    def __init__(self, simfile):

        self.sim_path = simfile
        self.position = 0,0
        self.direction = 0,0
        self.velocity = 0
        self.field_path = ""
        self.step_size = 0
        self.reaction_time = 0
        self.tracking = False

    def read(self):

        with open(self.sim_path) as data_file:
            data = json.load(data_file)

        self.position = (data[self.CARPOSX], data[self.CARPOSY])
        self. direction = (data[self.CARdx], data[self.CARdy])
        self.velocity = data[self.CARVELOCITY]
        self.field_path = str(data[self.FIELDPATH])
        self.step_size = data[self.STEPSIZE]
        self.reaction_time = data[self.REACTIONTIME]
        self.tracking = data[self.TRACKING]

    def getState(self):

        car = Car(self.position[0], self.position[1], self.velocity)
        normaldirection = self.normalizeDirection(self.direction[0], self.direction[1])
        car.update_direction(normaldirection[0], normaldirection[1])
        field = Field(self.field_path, car)
        eventhandler = EventExecutor(self.calcAngle(self.direction[0], self.direction[1]),
                                     self.step_size, self.reaction_time, self.tracking)
        return car, field, eventhandler

    def calcAngle(self, dx, dy):
        return np.arctan(dy/dx)

    def normalizeDirection(self, dx, dy):

        length = np.sqrt(dx**2 + dy**2)
        return dx/length, dy/length
