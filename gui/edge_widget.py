from kivy.uix.widget import Widget
from kivy.properties import ListProperty


class EdgeWidget(Widget):

    points = ListProperty()

    def __init__(self, node1, node2, cost=0): # the nodes are NodeWidget objects
        super().__init__()
        self.points = [node1.pos[0] + node1.size[0] / 2, node1.pos[1] + node1.size[1] / 2, node2.pos[0] + node2.size[0] / 2, node2.pos[1] + node2.size[1] / 2]
        self.cost = cost