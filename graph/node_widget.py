from kivy.uix.widget import Widget
from globals import globals
from kivy.properties import StringProperty, ListProperty, NumericProperty

def getnextid():
    nextid = 1

    globals.graphManager.nodeWidgets.sort(key=lambda node: node.Id)

    while True:
        result = globals.binarySearch(globals.graphManager.nodeWidgets, 0, len(globals.graphManager.nodeWidgets) - 1, nextid)

        if result == -1: # means that it does not exists a node with that id
            return nextid

        nextid += 1


def changeNodeWidgetBackgroundColor(color):
    for c in globals.colors:
        if c == color:
            globals.NodeWidgetBackgroundColor = globals.colors[c]
            break
    globals.graphManager.update_canvas()

def changeNodeWidgetColor(color):
    for c in globals.colors:
        if c == color:
            globals.NodeWidgetColor = globals.colors[c]
            break
    globals.graphManager.update_canvas()

def changeNodeRadius(new_radius):
    globals.radiusOfNodeWidget = new_radius


class NodeWidget(Widget):

    nodeId = StringProperty()
    backgroundColor = ListProperty(globals.colors['white'])
    marginWidth = NumericProperty(5)

    def __init__(self, Id, pos):
        super().__init__()  # calls the constructor of the Widget class
        self.Id = Id
        self.pos = pos
        self.neighbors = [] # the list of neighbors
        self.size = [ 2 * globals.radiusOfNodeWidget, 2 * globals.radiusOfNodeWidget ]
        self.force = [0, 0]
        #self.backgroundColor = globals.NodeWidgetBackgroundColor
        self.color = globals.NodeWidgetColor # the color refers to the margins and the id of the node
        self.nodeId = str(Id)

    def setMarginWidth(self, value):
        self.marginWidth = int(value)
        globals.graphManager.update_canvas()

    def getMarginWidth(self):
        globals.graphManager.update_canvas()
        return self.marginWidth

    def setNodeId(self, nodeId):
        self.Id = nodeId
        self.ids.nodeId_lbl.text = str(nodeId)

    def setLabelId(self, nodeId):
        self.nodeId = str(nodeId)
        self.ids.nodeId_lbl.text = str(nodeId)

    def getId(self):
        return self.nodeId

    def getNextId(self):
        return getnextid()

    def getNodeWidgetBackgroundColor(self):
        #return globals.NodeWidgetBackgroundColor
        return self.backgroundColor

    def getNodeWidgetColor(self):
        return globals.NodeWidgetColor

    def getNodeRadius(self):
        return globals.radiusOfNodeWidget