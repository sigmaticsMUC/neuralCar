import math
import numpy as np
from PIL import Image


class Field:

    def __init__(self, field_path, car):

        self.field_path = field_path
        self.field_image = self.read_image(path=field_path)
        self.car = car
        self.pixels = self.field_image.load()

    def checkpos(self, x, y):

        xCeil = math.ceil(x)
        yCeil = math.ceil(y)

        xCur = math.ceil(self.car.position[0])
        yCur = math.ceil(self.car.position[1])

        xtrunc = math.trunc(x)
        ytrunc = math.trunc(y)

        if self.pixels[xCeil,yCeil] == (0,0,0) or self.pixels[xtrunc, ytrunc] == (0,0,0)\
                or self.pixels[xCeil, ytrunc] == (0,0,0) or self.pixels[xtrunc, yCeil] == (0,0,0):
            return False
        else:
            return True

    def read_image(self, path):

        img = Image.open(path)
        return img

    def getBoundaryDistanceSides(self):

        x = self.car.direction[0]
        y = self.car.direction[1]

        xP = self.car.position[0]
        yP = self.car.position[1]

        leftVector = (x * np.cos(np.pi/2) - y * np.sin(np.pi/2), x * np.sin(np.pi/2) - y * np.cos(np.pi/2))
        rightVector = (x * np.cos(3*np.pi/2) - y * np.sin(3*np.pi/2), x * np.sin(3*np.pi/2) - y * np.cos(3*np.pi/2))

        rCounter = 0
        lCounter = 0

        rx = rightVector[0]
        ry = rightVector[1]

        while self.checkpos(xP+rx*rCounter, yP+ry*rCounter):
            rCounter +=1

        lx = leftVector[0]
        ly = leftVector[1]

        while self.checkpos(xP+lx*lCounter, yP+ly*lCounter):
            lCounter += 1

        rightVector = (rx*rCounter, ry*rCounter)
        leftVector = (lx*lCounter, ly*lCounter)

        rDistance = np.sqrt(rightVector[0]**2 + rightVector[1]**2)
        lDistance = np.sqrt(leftVector[0]**2 + leftVector[1]**2)

        return rDistance, lDistance

    def getBoundaryDistanceFront(self):

        x = self.car.direction[0]
        y = self.car.direction[1]

        xP = self.car.position[0]
        yP = self.car.position[1]

        fCounter = 0
        while self.checkpos(xP+x*fCounter, yP+y*fCounter):
            fCounter += 1

        frontVector = (x*fCounter, y*fCounter)

        # front distance
        return np.sqrt(frontVector[0]**2 + frontVector[1]**2)


    def pixel_size_toCons(self):
        print self.field_image.size
