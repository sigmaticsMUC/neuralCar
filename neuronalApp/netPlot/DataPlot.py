import matplotlib.pyplot as plt
import numpy as np
from neuronalApp.netIO import  DataPackage as dP

def data_plot(*args):

    for data in args:
        num_of_data = len(data.signals)
        X = np.linspace(1, num_of_data, num_of_data, endpoint=True)
        plt.plot(X, data.signals, label = data.plotInfs.dataName, color= data.plotInfs.color )
        plt.legend(loc='upper left', frameon=False)

    plt.show()
