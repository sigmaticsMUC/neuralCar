from PIL import Image
import Car

class Field:

    def __init__(self, field_path, car):

        self.field_path = field_path
        self.field_image = self.read_image(path=field_path)
        self.car = car
        self.pixels = self.field_image.load()


    def checkpos(self, x, y):

        if self.pixels[x,y] == (0,0,0):
            return False
        else:
            return True

    def read_image(self, path):

        img = Image.open(path)
        return img
