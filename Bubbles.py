import matplotlib.pyplot as plt
from stageLights1 import *
import numpy as np


def main():
    SIZE = 1
    LIMITS = (1000,1000)
    
    lights = np.empty((10,10), dtype=object)
    #colours = ["red", "orange", "yellow", "green", "blue", "violet"]
    bubbles = BubbleMachine((0,200))

    for a in range (10):
        ax= plt.axes()
        ax.set_xlim(0,1000)
        ax.set_ylim(0,1000)
        ax.set_aspect("equal")
        ax.set_facecolor('black')
        
        bubbles.stepChange()
        bubbles.plotBubbles(ax)
        

        plt.title("Floating Bubble -"+ str(a+1),fontsize="18")
        #plt.savefig("Floating Bubble -" + str (a+1) + '.png')
        plt.pause(0.5)
        plt.clf()

if __name__ == "__main__":
    main()
