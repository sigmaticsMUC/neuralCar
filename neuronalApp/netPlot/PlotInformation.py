# stores plotinformation


class PlotInformation:

    def __init__(self, color, dataName):
        self.color = color
        self.dataName = dataName

    def toString(self):

        return self.color + " : " + self.dataName

