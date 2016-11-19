class EventExecutor:

    def __init__(self, angle, step, reaction_time, tracking):
        self.ANGLE = angle
        self.STEP = step
        self.REACTIONTIME = reaction_time
        self.RUNNING = True
        self.TRACKING = tracking

    def turnleft(self):
        self.ANGLE += self.STEP

    def turnright(self):
        self.ANGLE -= self.STEP
