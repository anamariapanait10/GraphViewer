from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from globals import globals


def changeEdgeWidgetColor(color):
    for c in globals.colors:
        if c == color:
            globals.EdgeWidgetColor = globals.colors[c]
            break
    globals.graphManager.update_canvas()

#TODO: use the lengthEdgeWidget constant
def changeEdgeLength(new_length):
    globals.lengthOfEdgeWidget = new_length

class EdgeWidget(Widget):

    points = ListProperty()

    def __init__(self, node1, node2, cost=0): # the nodes are NodeWidget objects
        super().__init__()
        self.points = [node1.pos[0] + node1.size[0] / 2, node1.pos[1] + node1.size[1] / 2,
                       node2.pos[0] + node2.size[0] / 2, node2.pos[1] + node2.size[1] / 2]
        self.node1 = node1
        self.node2 = node2
        self.cost = cost
        self.color = globals.EdgeWidgetColor

    def getIsDirected(self):
        return globals.graphManager.isDirected

    #TODO: find a solution for the triangle...
    def getTrianglePoints(self):
        # I am thinking to make a vector perpendicular to the edge at a distance of 20 from the sourceNode
        # then fix the first vertex of the triangle to the sourceNode
        # and make the other vertexes to be at the same distance (10 I think) and on the vector
        # in order to form a triangle that maintains its shapes regardless of the edge orientation
        pass

    def updateCoords(self):
        nodeWidget1 = globals.graphManager.getNodeWidgetById(self.node1.Id)
        nodeWidget2 = globals.graphManager.getNodeWidgetById(self.node2.Id)

        self.points = [nodeWidget1.pos[0] + nodeWidget1.size[0] / 2, nodeWidget1.pos[1] + nodeWidget1.size[1] / 2,
                       nodeWidget2.pos[0] + nodeWidget2.size[0] / 2, nodeWidget2.pos[1] + nodeWidget2.size[1] / 2]


    def getEdgeWidgetColor(self):
        return globals.EdgeWidgetColor

    def updateEdgeWidgetColor(self):
        self.color = globals.EdgeWidgetColor
