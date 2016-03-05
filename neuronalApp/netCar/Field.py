from PIL import Image
import scipy.misc
import Car

class Field:

    def __init__(self, field_path, car):

        self.field_image = read_image(path=field_path)
        self.car = car

    def checkpos(self, x, y):

        pixels = self.field_image.load()
        #print pixels[x,y]
        if pixels[x,y] == (0,0,0):
           # print x,y
            return False
        else:
            return True









def read_image(path):

    img = Image.open(path)
    return img

