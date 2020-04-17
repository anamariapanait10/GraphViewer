from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from gui import globals



def changeEdgeWidgetColor(color):
    for c in globals.colors:
        if c == color:
            globals.EdgeWidgetColor = globals.colors[c]
            break
    globals.graphManager.update_canvas()

def changeEdgeLength(new_length):
    globals.lengthOfEdgeWidget = new_length

class EdgeWidget(Widget):

    points = ListProperty()

    def __init__(self, node1, node2, cost=0): # the nodes are NodeWidget objects
        super().__init__()
        self.points = [node1.pos[0] + node1.size[0] / 2, node1.pos[1] + node1.size[1] / 2, node2.pos[0] + node2.size[0] / 2, node2.pos[1] + node2.size[1] / 2]
        self.cost = cost
        self.node1 = node1
        self.node2 = node2

    def getIsDirected(self):
        return globals.graphManager.getIsDirected()

    def getTrianglePoints(self):
        # self.node2 is the dest
        # I have to make a vector to the node1 and node2
        # then fix the first vertex of the triangle to
        pass

    def updateCoords(self):
        n1 = globals.graphManager.getNodeWidgetById(self.node1.nr)
        n2 = globals.graphManager.getNodeWidgetById(self.node2.nr)

        self.points = [self.node1.pos[0] + self.node1.size[0] / 2, self.node1.pos[1] + self.node1.size[1] / 2,
                       self.node2.pos[0] + self.node2.size[0] / 2, self.node2.pos[1] + self.node2.size[1] / 2]



    def getEdgeWidgetColor(self):
        return globals.EdgeWidgetColor

    def getEdgeLength(self):
        return globals.lengthOfEdgeWidget