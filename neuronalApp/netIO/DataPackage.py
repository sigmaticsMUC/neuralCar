# class which stores NN data (e.g to write in database or to plot it)
from neuronalApp.netPlot import PlotInformation as pI


class DataPackage:

    def __init__(self, color = "black", dataName = "default", signals = [4,5,6,7], identifier="xxxxx"):
        self.plotInfs = pI.PlotInformation(color, dataName)
        self.signals = signals
        self.identifier = identifier