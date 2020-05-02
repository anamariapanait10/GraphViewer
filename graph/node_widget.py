from kivy.uix.widget import Widget
from globals import globals
from kivy.properties import StringProperty, ListProperty, NumericProperty

def getnextid():
    next_id = 1

    globals.graph_manager.node_widgets.sort(key=lambda node: node.Id)

    while True:
        result = globals.binarySearch(globals.graph_manager.node_widgets, 0, len(globals.graph_manager.node_widgets) - 1, next_id)

        if result == -1: # means that it does not exists a node with that id
            return next_id

        next_id += 1


def changeNodeRadius(new_radius):
    globals.node_radius = new_radius
    NodeWidget.radius = int(new_radius)


class NodeWidget(Widget):

    node_id = StringProperty()
    background_color = ListProperty(globals.colors['white'])
    border_color = ListProperty(globals.colors['black']) # this refers to the id color as well
    border_width = NumericProperty(5)
    radius = NumericProperty(globals.node_radius)

    def __init__(self, Id, pos):
        super().__init__()  # calls the constructor of the Widget class
        self.Id = Id
        self.pos = pos
        self.neighbors = [] # the list of neighbors
        self.size = [ 2 * self.radius, 2 * self.radius ]
        self.force = [0, 0]
        self.node_id = str(Id)
        self.background_color = globals.node_background_color
        self.border_color = globals.node_border_color

    def set_radius(self, r):
        self.radius = r