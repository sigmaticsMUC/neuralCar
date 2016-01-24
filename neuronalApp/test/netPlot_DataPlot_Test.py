from neuronalApp.netPlot import DataPlot as dp
from neuronalApp.netModel import Activation as active
from neuronalApp.netIO import DataPackage as dP

input = [2,3,4,5,6,6,7,8,8,5,2,3,4,5,3,6,4,2,5,7]
output1 = active.gaussian(input)
output2 = active.logistic(input)
output3 = active.identity(input)


pack1 = dP.DataPackage("red", "nn-output", [output1, output2, output3, 7])
pack2 = dP.DataPackage("green", "test-data", [1,2,100, 110])
pack3 = dP.DataPackage( dataName = "Default-Name")
dp.data_plot(pack1, pack2, pack3)