import matplotlib.pyplot as plt
from stageLights import *

def main():
    SIZE = 10
    LIMITS = (1000,1000)
    
    fileobject= open('lights.csv')
    data=fileobject.readlines()
    fileobject.close()
    ax = plt.axes()
    ax.set_xlim(0,1000)
    ax.set_ylim(0,1000)
    ax.set_aspect("equal")
    ax.set_facecolor('black')



    for line in data:
        splitline = line.strip().split(',')
        light = Light((int(splitline[2]), int(splitline[3])),splitline[4])
        light.plotLight(ax)
    fileobject.close()


        
    #bubbles.stepChange()
    #bubbles.plotBubbles(ax)

    plt.title("Coloured Lights - From File", fontsize="18")
    
    plt.show()
    #plt.pause(2)
    #plt.clf()

if __name__ == "__main__":
    main()
