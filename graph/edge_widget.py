from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty
from globals import globals
from math import sqrt, sin, cos, pi


#TODO: use the edge_length constant
def changeEdgeLength(new_length):
    globals.edge_length = new_length

class EdgeWidget(Widget):

    points = ListProperty()
    triangle_points = ListProperty()
    label_position = ListProperty([0, 0])
    cost = NumericProperty(0)
    color = ListProperty(globals.colors['black'])

    def __init__(self, node1, node2, cost=0): # the nodes are NodeWidget objects
        super().__init__()

        if node1 != None and node2 != None:
            self.points = [node1.pos[0] + globals.node_radius, node1.pos[1] + globals.node_radius,
                           node2.pos[0] + globals.node_radius, node2.pos[1] + globals.node_radius]

            self.node1 = node1
            self.node2 = node2
            self.cost = cost
            self.triangle_points = [0, 0, 0, 0, 0, 0]
            self.label_position = [(node1.pos[0] + node2.pos[0]) / 2 - 10,
                                   (node1.pos[1] + node2.pos[1]) / 2 - 10]


    def getTrianglePoints(self):
        points=[]

        source_x = self.node1.pos[0]
        source_y = self.node1.pos[1]

        dest_x = self.node2.pos[0]
        dest_y = self.node2.pos[1]

        dist = sqrt((dest_x - source_x) ** 2 + (dest_y - source_y) ** 2)

        sine = (dest_y - source_y) / dist
        cosine = (dest_x - source_x) / dist
        points.append(dest_x - globals.node_radius * cosine + globals.node_radius)
        points.append(dest_y - globals.node_radius * sine + globals.node_radius)

        cos_p2 = cosine * cos(pi / 12) + sine * sin(pi / 12)
        sin_p2 = sine * cos(pi / 12) - sin(pi / 12) * cosine

        r2 = 50
        points.append(dest_x - r2 * cos_p2 + globals.node_radius)
        points.append(dest_y - r2 * sin_p2 + globals.node_radius)

        cos_p3 = cosine * cos(pi / 12) - sine * sin(pi / 12)
        sin_p3 = sine * cos(pi / 12) + sin(pi / 12) * cosine

        points.append(dest_x - r2 * cos_p3 + globals.node_radius)
        points.append(dest_y - r2 * sin_p3 + globals.node_radius)

        return points

    def updateCoords(self):
        node_widget1 = globals.graph_manager.getNodeWidgetById(self.node1.Id)
        node_widget2 = globals.graph_manager.getNodeWidgetById(self.node2.Id)

        self.points = [node_widget1.pos[0] + globals.node_radius, node_widget1.pos[1] + globals.node_radius,
                       node_widget2.pos[0] + globals.node_radius, node_widget2.pos[1] + globals.node_radius]

        if globals.graph_manager.is_directed:
            self.triangle_points = self.getTrianglePoints()

        self.label_position = [(self.points[0] + self.points[2]) / 2 - 10,
                              (self.points[1] + self.points[3]) / 2 - 10]
