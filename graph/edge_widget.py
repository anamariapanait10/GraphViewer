from kivy.uix.widget import Widget
from kivy.properties import ListProperty
from globals import globals
from math import sqrt

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
        '''self.points = [node1.pos[0] + node1.size[0] / 2, node1.pos[1] + node1.size[1] / 2,
                       node2.pos[0] + node2.size[0] / 2, node2.pos[1] + node2.size[1] / 2]'''

        self.points = [node1.pos[0] + globals.radiusOfNodeWidget / 2, node1.pos[1] + globals.radiusOfNodeWidget / 2,
                       node2.pos[0] + globals.radiusOfNodeWidget / 2, node2.pos[1] + globals.radiusOfNodeWidget / 2]

        self.node1 = node1
        self.node2 = node2
        self.cost = cost
        self.color = globals.EdgeWidgetColor

    def getIsDirected(self):
        return globals.graphManager.isDirected

    #TODO: find a solution for the triangle...
    def getTrianglePoints(self):
        points=[]

        source_x = self.node1.pos[0]
        source_y = self.node1.pos[1]

        dest_x = self.node2.pos[0]
        dest_y = self.node2.pos[1]

        dist = sqrt((dest_x - source_x) ** 2 + (dest_y - source_y) ** 2)

        if dest_x > source_x and dest_y > source_y: # if dest is in the first dial
            sinus = (dest_y - source_y) / dist
            cosinus = (dest_x - source_x) / dist
            points.append(dest_x + globals.radiusOfNodeWidget * cosinus)
            points.append(dest_y + globals.radiusOfNodeWidget * sinus)

            ct = 20
            points.append(dest_x + ct * cosinus + 10)
            points.append(dest_y + ct * sinus + 10)

            points.append(dest_x + ct * cosinus - 10)
            points.append(dest_y + ct * sinus - 10)

        elif dest_x < source_x and dest_y > source_y: # if dest is in the second dial
            sinus = (dest_y - source_y) / dist
            cosinus = - (dest_x - source_x) / dist
            points.append(dest_x + globals.radiusOfNodeWidget * cosinus)
            points.append(dest_y + globals.radiusOfNodeWidget * sinus)

            ct = 20
            points.append(dest_x + ct * cosinus + 10)
            points.append(dest_y + ct * sinus + 10)

            points.append(dest_x + ct * cosinus - 10)
            points.append(dest_y + ct * sinus - 10)

        elif dest_x < source_x and dest_y < source_y: # if dest is in the third dial
            sinus = - (dest_y - source_y) / dist
            cosinus = - (dest_x - source_x) / dist
            points.append(dest_x + globals.radiusOfNodeWidget * cosinus)
            points.append(dest_y + globals.radiusOfNodeWidget * sinus)

            ct = 20
            points.append(dest_x + ct * cosinus + 10)
            points.append(dest_y + ct * sinus + 10)

            points.append(dest_x + ct * cosinus - 10)
            points.append(dest_y + ct * sinus - 10)

        else: # if dest is in the forth dial
            sinus = - (dest_y - source_y) / dist
            cosinus = (dest_x - source_x) / dist
            points.append(dest_x + globals.radiusOfNodeWidget * cosinus)
            points.append(dest_y + globals.radiusOfNodeWidget * sinus)

            ct = 20
            points.append(dest_x + ct * cosinus + 10)
            points.append(dest_y + ct * sinus + 10)

            points.append(dest_x + ct * cosinus - 10)
            points.append(dest_y + ct * sinus - 10)

        return points

    def updateCoords(self):
        nodeWidget1 = globals.graphManager.getNodeWidgetById(self.node1.Id)
        nodeWidget2 = globals.graphManager.getNodeWidgetById(self.node2.Id)

        self.points = [nodeWidget1.pos[0] + globals.radiusOfNodeWidget / 2, nodeWidget1.pos[1] + globals.radiusOfNodeWidget / 2,
                       nodeWidget2.pos[0] + globals.radiusOfNodeWidget / 2, nodeWidget2.pos[1] + globals.radiusOfNodeWidget / 2]


    def getEdgeWidgetColor(self):
        return globals.EdgeWidgetColor

    def updateEdgeWidgetColor(self):
        self.color = globals.EdgeWidgetColor
