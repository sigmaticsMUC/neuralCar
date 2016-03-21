import neuronalApp.netCar.CarSim as CarSim
import sqlite3
connection = sqlite3.connect("lokaledb.db")


CarSim.start_simulation()