from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from gui import globals


colors = { 'white': [0.9, 0.9, 0.9, 1], 'black': [0, 0, 0, 1], 'red': [1, 0, 0, 1], 'yellow': [0.937, 0.87, 0.32, 1],
           'orange': [1, 0.62, 0.088, 1], 'blue': [0.199, 0.7, 1, 1], 'purple': [0.75, 0.5, 1, 1],
           'green': [0.099, 1, 0.66, 1], 'pink': [1, 0.5, 0.875, 1] }


def changeEdgeWidgetColor(color):
    for c in colors:
        if c == color:
            globals.EdgeWidgetColor = colors[c]
            break
    globals.graphManager.update_canvas()


class EdgeWidget(Widget):

    points = ListProperty()

    def __init__(self, node1, node2, cost=0): # the nodes are NodeWidget objects
        super().__init__()
        self.points = [node1.pos[0] + node1.size[0] / 2, node1.pos[1] + node1.size[1] / 2, node2.pos[0] + node2.size[0] / 2, node2.pos[1] + node2.size[1] / 2]
        self.cost = cost
        self.node1 = node1
        self.node2 = node2

    def updateCoords(self):
        n1 = globals.graphManager.getNodeWidgetById(self.node1.nr)
        n2 = globals.graphManager.getNodeWidgetById(self.node2.nr)

        self.points = [self.node1.pos[0] + self.node1.size[0] / 2, self.node1.pos[1] + self.node1.size[1] / 2,
                       self.node2.pos[0] + self.node2.size[0] / 2, self.node2.pos[1] + self.node2.size[1] / 2]


    def getEdgeWidgetColor(self):
        return globals.EdgeWidgetColor