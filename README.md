# Neural Network controlled autonomous driving RC-Car
## About
A project agreed upon by students from Munich University of Applied Sciences  
to create a neural network controlled autonomous driving RC-Car in effort to  
acquire practical experience in machine learning. This introduction will
continously be updated as the ideas of the project become more concrete.
##Requirements
Raspberry pi - Provides the serial interface for controlling RC-Car.
Arduino - Allows the driver to send commands to the car via a serial interface.  
Train   - Neural network code written in Python to train with backpropagation.  
Camera  - To take images of the road ahead and pass them on to the neural  
          network for processing.
## Idea for the vehicle simulation.
Neural network learns how to drive a simulated 2D car. 
Input: Location and state related input of car simulation
Output: Action which moves the car to desired state

