from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty
from globals import globals
from math import sqrt, sin, cos, pi

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
    trianglePoints = ListProperty()
    labelPosition = ListProperty([0, 0])
    cost = NumericProperty(0)

    def __init__(self, node1, node2, cost=0): # the nodes are NodeWidget objects
        super().__init__()

        self.points = [node1.pos[0] + globals.radiusOfNodeWidget / 2, node1.pos[1] + globals.radiusOfNodeWidget / 2,
                       node2.pos[0] + globals.radiusOfNodeWidget / 2, node2.pos[1] + globals.radiusOfNodeWidget / 2]

        self.node1 = node1
        self.node2 = node2
        self.cost = cost
        self.color = globals.EdgeWidgetColor
        self.trianglePoints = [0, 0, 0, 0, 0, 0]
        self.labelPosition = [ (node1.pos[0] + node2.pos[0]) / 2 - 10,
                               (node1.pos[1] + node2.pos[1]) / 2 - 10]

    def getIsDirected(self):
        return globals.graphManager.isDirected


    def getTrianglePoints(self):
        points=[]

        source_x = self.node1.pos[0]
        source_y = self.node1.pos[1]

        dest_x = self.node2.pos[0]
        dest_y = self.node2.pos[1]

        dist = sqrt((dest_x - source_x) ** 2 + (dest_y - source_y) ** 2)

        sinus = (dest_y - source_y) / dist
        cosinus = (dest_x - source_x) / dist
        points.append(dest_x - (globals.radiusOfNodeWidget / 2) * cosinus + globals.radiusOfNodeWidget / 2)
        points.append(dest_y - (globals.radiusOfNodeWidget / 2) * sinus + globals.radiusOfNodeWidget / 2)

        cos_p2 = cosinus * cos(pi / 12) + sinus * sin(pi / 12)
        sin_p2 = sinus * cos(pi / 12) - sin(pi / 12) * cosinus

        r2 = 50
        points.append(dest_x - r2 * cos_p2 + globals.radiusOfNodeWidget / 2)
        points.append(dest_y - r2 * sin_p2 + globals.radiusOfNodeWidget / 2)

        cos_p3 = cosinus * cos(pi / 12) - sinus * sin(pi / 12)
        sin_p3 = sinus * cos(pi / 12) + sin(pi / 12) * cosinus

        points.append(dest_x - r2 * cos_p3 + globals.radiusOfNodeWidget / 2)
        points.append(dest_y - r2 * sin_p3 + globals.radiusOfNodeWidget / 2)

        return points

    def updateCoords(self):
        nodeWidget1 = globals.graphManager.getNodeWidgetById(self.node1.Id)
        nodeWidget2 = globals.graphManager.getNodeWidgetById(self.node2.Id)

        self.points = [nodeWidget1.pos[0] + globals.radiusOfNodeWidget / 2, nodeWidget1.pos[1] + globals.radiusOfNodeWidget / 2,
                       nodeWidget2.pos[0] + globals.radiusOfNodeWidget / 2, nodeWidget2.pos[1] + globals.radiusOfNodeWidget / 2]

        if globals.graphManager.isDirected == True:
            self.trianglePoints = self.getTrianglePoints()

        self.labelPosition = [(self.points[0] + self.points[2]) / 2 - 10,
                              (self.points[1] + self.points[3]) / 2 - 10]


    def getEdgeWidgetColor(self):
        return globals.EdgeWidgetColor

    def updateEdgeWidgetColor(self):
        self.color = globals.EdgeWidgetColor
