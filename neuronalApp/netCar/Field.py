from PIL import Image
import numpy as np
import Car
import math

class Field:

    def __init__(self, field_path, car, resolution):

        self.field_path = field_path
        self.field_image = self.read_image(path=field_path)
        self.car = car
        self.pixels = self.field_image.load()
        self.resolution = resolution

    def checkpos(self, x, y):

       # print "Current" + str(self.car.position)
       # print "Checking pos at: " + str(x) + ", " + str(y)
       # print "++++++++++++++"

        xCeil = math.ceil(x)
        yCeil = math.ceil(y)

        xCur = math.ceil(self.car.position[0])
        yCur = math.ceil(self.car.position[1])

        xtrunc = math.trunc(x)
        ytrunc = math.trunc(y)
        if self.pixels[xCeil,yCeil] == (0,0,0) or self.pixels[xtrunc, ytrunc] == (0,0,0) or self.pixels[xCur, yCur] == (0,0,0):
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

        # x = x * cos(90) - y * sin(90)
        # y = x * sin(90) - y * cos(90)

        leftVector = (x * np.cos(np.pi/4) - y * np.sin(np.pi/4), x * np.sin(-np.pi/4) - y * np.cos(-np.pi/4))
        rightVector = (-leftVector[0], -leftVector[1])

        rCounter = 0
        lCounter = 0

        rx = self.resolution * rightVector[0]
        ry = self.resolution * rightVector[1]

        while self.checkpos(xP+rx*rCounter, yP+ry*rCounter):
            rCounter +=1

        lx = self.resolution * leftVector[0]
        ly = self.resolution * leftVector[1]

        while self.checkpos(xP+lx*lCounter, yP+ly*lCounter):
            lCounter += 1

        rightVector = (rx*rCounter, ry*rCounter)
        leftVector = (lx*lCounter, ly*lCounter)

        rDistance = np.sqrt(rightVector[0]**2 + rightVector[1]**2)
        lDistance = np.sqrt(leftVector[0]**2 + leftVector[1]**2)

        return rDistance, lDistance

    def getBoundaryDistanceFront(self):

        x = self.resolution * self.car.direction[0]
        y = self.resolution * self.car.direction[1]

        xP = self.car.position[0]
        yP = self.car.position[1]

        fCounter = 0
        while self.checkpos(xP+x*fCounter, yP+y*fCounter):
            fCounter += 1

        frontVector = (x*fCounter, y*fCounter)

        # front distance
        return np.sqrt(frontVector[0]**2 + frontVector[1]**2)


    def pixel_toCons(self):
        print self.field_image.size
