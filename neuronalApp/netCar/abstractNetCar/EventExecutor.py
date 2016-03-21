class EventExecutor:

    def __init__(self, angle, step, reaction_time):
        self.ANGLE = angle
        self.STEP = step
        self.REACTIONTIME = reaction_time
        self.RUNNING = True

    def turnleft(self):
        self.ANGLE += self.STEP

    def turnright(self):
        self.ANGLE -= self.STEP
