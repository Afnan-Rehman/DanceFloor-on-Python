import matplotlib.pyplot as plt
from stageLights import *

def main():
    SIZE = 10
    LIMITS = (1000,1000)

    ax = plt.axes()
    ax.set_xlim(0,1000)
    ax.set_ylim(0,1000)
    ax.set_aspect("equal")
    ax.set_facecolor('black')

    lights = np.empty((10,10), dtype=object)
    for i in range(10):
        for j in range(10):
            pos = (50 + i*100, 50 + j*100)
            lights[i,j] = Light(pos, 'red')
            lights[i,j].plotLight(ax)

    

    



        
    #bubbles.stepChange()
    #bubbles.plotBubbles(ax)

    plt.title("Red Lights - 10x10", fontsize="18")
    
    plt.show()
    #plt.pause(2)
    #plt.clf()

if __name__ == "__main__":
    main()
