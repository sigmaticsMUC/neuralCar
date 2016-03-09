


class Events:

    def __init__(self):
        self.ANGLE = 0
        self.STEP = 0.1


    def turnleft(self):
        self.ANGLE -= self.STEP


    def turnright(self):
        self.ANGLE += self.STEP