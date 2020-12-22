#Graph Program

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting (axis_x,axis_y)

def plotlineXY(axis_x,axis_y):
    fig, ax = plt.subplots()
    ax.plot(axis_x, axis_y)
    ax.set(xlabel='Pressure', ylabel='Actuator Position', title='Output Test')
    ax.grid()
    fig.savefig("test.png")
    plt.show()

    