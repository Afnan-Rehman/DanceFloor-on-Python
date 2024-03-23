import matplotlib.pyplot as plt
from stageLights import *

def main():
    SIZE = 10
    LIMITS = (1000,1000)

    lights = np.empty((10,10), dtype=object)
    colours = ["red", "orange", "yellow", "green", "blue", "violet"]
    
    fileobject = open('col_lights.csv')
    data = fileobject.readlines()
    fileobject.close()
  

    for line in data:
        splitline = line.strip().split(',')
        r = int(splitline[0])
        c = int(splitline[1])
        r1 = int(splitline[2])
        c1 = int(splitline[3])
        color = splitline [4]
        lights[r,c] = Light((r1,c1), color)
           # lights[r,c].plotLight(ax)

   # fig, axes=plt.subplots(1,10)
    for i in range (10):
        ax= plt.axes()
        ax.set_xlim(0,1000)
        ax.set_ylim(0,1000)
        ax.set_aspect("equal")
        ax.set_facecolor('black')
        





        for a in range(SIZE):
            for c in range(SIZE):
                lights [a,c].setColour(colours[(i+a+c)%6])
                lights [a,c].plotLight(ax)


        plt.title("Moving Coloured Lights -"+ str(i+1),fontsize="18")
        plt.savefig("Moving Coloured Lights -"+ str(i+1) + '.png')
        plt.pause(0.5)
        plt.clf()

    
   





        
    #bubbles.stepChange()
    #bubbles.plotBubbles(ax)

    plt.title("Moving Coloured Lights -", fontsize="18")
    plt.show()
    #plt.pause(1)
    #plt.clf()

if __name__ == "__main__":
    main()
