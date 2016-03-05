

class Car:

    color = (255, 0, 0)

    def __init__(self, xpos, ypos, velocity):
        self.velocity = velocity
        self.position = (xpos, ypos)    # instance variable unique to each instance
        #self.direction = (1.0, 0)       # vector indicating directon of car


    def move(self):

        self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
        #print self.position
        #print "moved"

    def get_next_pos(self):

        return self.position[0] + self.direction[0], self.position[1] + self.direction[1]

    def update_direction(self, dx, dy):

        self.direction = (dx, dy)

    def to_string(self):

        return "Car position at: " + str(self.position[0]) + ", " + str(self.position[1]) + "\n" + \
            "Car direction: " + str(self.direction[0]) + ", " + str(self.direction[1]) + "\n" + \
            "Car velocity: " + str(self.velocity)


