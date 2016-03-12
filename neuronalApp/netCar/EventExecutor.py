class EventExecutor:

    def __init__(self, angle, step):
        self.ANGLE = angle
        self.STEP = step
        self.RUNNING = True

    def turnleft(self):
        self.ANGLE -= self.STEP

    def turnright(self):
        self.ANGLE += self.STEP
