import matplotlib.pyplot as plt
import numpy as np

class Light():
    canR = 30

    def __init__(self, pos, colour):
        self.pos = pos
        self.colour = colour

    def setColour(self, colour):
        self.colour = colour

    def plotLight(self, ax):
        circle1 = plt.Circle([self.pos[0],self.pos[1]],self.canR, color=self.colour)
        ax.add_patch(circle1)

class BubbleMachine():

    def __init__(self, pos):
        self.pos = pos
        self.bubbles = []
        self.flow = 1

    def startBubbles(self):
        self.flow = 1

    def stopBubbles(self):
        self.flow = 0

    def stepChange(self):
        if self.flow == 1:
            self.bubbles.append([self.pos[0], self.pos[1]])
        for s in self.bubbles:
            s[0] = s[0] + 100
            s[1] = s[1] + 100

    def plotBubbles(self, ax):
        xvalues = [s[0] for s in self.bubbles]
        yvalues = [s[1] for s in self.bubbles]
        print(xvalues)
        print(yvalues)
        
        ax.scatter(xvalues, yvalues, s=[500], c="white")
