from graph import graph
from graph.graph_exception import GraphException
import random
from math import sqrt
from gui import node_widget
from gui import edge_widget
from gui import globals

class GraphManager:

    def __init__(self, isDirected, mainViewWidget):
        self.mainViewWidget = mainViewWidget
        self.graph = graph.Graph(isDirected)
        self.nodeWidgets = []   # the list of WidgetNodes
        self.edgeWidgets = []
        self.isDirected = isDirected

    def getNodeWidgetList(self):
        return self.nodeWidgets

    def getEdgeWidgetList(self):
        return self.edgeWidgets

    def getNodeWidgetById(self, id):
        try:
            id = int(id)
        except:
            raise GraphException('Node id must be a positive integer.')

        nd = None
        for n in self.nodeWidgets:
            if n.nr == id:
                nd = n
                break
        return nd

    def deleteNodeWidgetById(self, nodeId): # functia doar scoate din lista nodeWidgets nodul cu idul nodeId
        for nodeWidget in self.nodeWidgets[:]:
            if nodeWidget.nr == nodeId:
                self.nodeWidgets.remove(nodeWidget)
                break

    def deleteEdgeWidgetById(self, node1Id, node2Id):
        for edgeWidget in self.edgeWidgets[:]:
            if edgeWidget.node1.nr == node1Id and edgeWidget.node2.nr == node2Id:
                self.edgeWidgets.remove(edgeWidget)
                break

    def deleteNodeWidget(self, x1, y1): # the x and y are the coordinates of the touch and if they collide with a node, it will be deleted
        for nodeWidget in self.nodeWidgets[:]:
            x2 = nodeWidget.pos[0]
            y2 = nodeWidget.pos[1]
            dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if dist <= globals.radiusOfNodeWidget:
                self.mainViewWidget.ids.graph_canvas.remove(nodeWidget)
                self.graph.removeNode(nodeWidget.nr)
                self.nodeWidgets.remove(nodeWidget)

    def deleteEdgeWidget(self, x, y): # the x and y are the coordinates of the touch and if they collide with an edge, it will be deleted
        for edgeWidget in self.edgeWidgets[:]:
            if edgeWidget.collide_point(x, y):
                self.mainViewWidget.ids.graph_canvas.remove(edgeWidget)
                self.graph.removeEdge(edgeWidget.node1.nr, edgeWidget.node2.nr)
                self.edgeWidgets.remove(edgeWidget)

    def NodeWidgetExists(self, nodeId): # verify if a NodeWidget exists
        exists = False
        for nodeWidget in self.nodeWidgets:
            if nodeWidget.nr == nodeId:
                exists = True

        return exists

    def setisDirected(self, TrueOrFalse):
        self.isDirected = TrueOrFalse
        self.graph.setIsDirected(TrueOrFalse)

    def getIsDirected(self):
        return self.isDirected


    def interpretLine(self, text):  # returns -1 for invalid syntax
                                    # and a list otherwise:
                                    # [nodeId] for isolated nodes
                                    # [node1Id, node2Id] for unweighted edge
                                    # [nodeId, node2Id, cost] for weighted edge

        foundSource = False
        foundDest = False
        foundCost = False
        index = 0

        while index < len(text):

            if text[index].isdigit():

                if foundSource == False:
                    source = int(text[index])
                    index += 1
                    while index < len(text) and text[index].isdigit():
                        source = source * 10 + int(text[index])
                        index += 1
                    foundSource = True

                elif foundDest == False:
                    dest = int(text[index])
                    index += 1
                    while index < len(text) and text[index].isdigit():
                        dest = dest * 10 + int(text[index])
                        index += 1
                    foundDest = True

                elif foundCost == False:
                    cost = int(text[index])
                    index += 1
                    while index < len(text) and text[index].isdigit():
                        cost = cost * 10 + int(text[index])
                        index += 1
                    foundDest = True

                else:
                    return -1

            elif text[index] != ' ' and text[index] != '\n':
                return -1

            else:
                index += 1

        if foundSource == False: # if the condition is True, then it is an empty line
            return []   #TODO: deal with this case
        elif foundSource == True and foundDest == False: # if the condition is True, then it is an isolated node
            return [source]
        elif foundCost == False:  # if the condition is True, then it is an unweighted edge
            return [source, dest]
        else:    # if the condition is True, then it is an weighted edge
            return [source, dest, cost]


    def update_canvas(self):
        self.mainViewWidget.ids.graph_canvas.clear_widgets()

        for edge in self.edgeWidgets[:]:
            #self.deleteEdgeWidgetById(edge.node1.nr, edge.node2.nr) # this method only removes the edge from de edgeWidgets list
            #new_edge = edge_widget.EdgeWidget(edge.node1, edge.node2)
            edge.setEdgeWidgetColor()
            # del edge
            #self.edgeWidgets.append(new_edge)
            #self.mainViewWidget.ids.graph_canvas.add_widget(new_edge)
            self.mainViewWidget.ids.graph_canvas.add_widget(edge)


        for node in self.nodeWidgets[:]:
            self.deleteNodeWidgetById(node.nr) # this method only removes the node from de nodeWidgets list
            new_node = node_widget.NodeWidget(node.nr, [node.pos[0], node.pos[1]])
            new_node.setBackgroundColor()
            new_node.setColor()
            new_node.setLabelId(node.nr)
            # del node
            self.nodeWidgets.append(new_node)
            self.mainViewWidget.ids.graph_canvas.add_widget(new_node)

    def nodeWidgetsDontOverlap(self):   # This function generates random coordinates for the NodeWidget until
                                        #  the nodeWidget does not overlap the other nodeWidgets
        # boundary coordonates for spawning the nodes
        coords = [10, 10,
                  int(self.mainViewWidget.ids.graph_canvas.size[0] - 50),
                  int(self.mainViewWidget.ids.graph_canvas.size[1] - 50)]

        while(True):    # TODO= Put a boundary...
            x1 = random.randrange(coords[0], coords[2])
            y1 = random.randrange(coords[1], coords[3])

            GoodCoords = True
            for nodeWidget in self.nodeWidgets:
                x2 = nodeWidget.pos[0]
                y2 = nodeWidget.pos[1]
                dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if dist < 2 * globals.radiusOfNodeWidget + globals.minimumDistanceBetweenNodeWidgets:
                    GoodCoords = False
                    break

            if GoodCoords == True:
                return [x1, y1]

    def addNodeWidget(self, nodeId):

        if self.NodeWidgetExists(nodeId) == False:
            self.graph.addNode(nodeId)
            pos = self.nodeWidgetsDontOverlap()
            nodeWidget = node_widget.NodeWidget(nodeId, pos)
            self.nodeWidgets.append(nodeWidget)

    def edgeAlreadyExists(self, sourceNodeId, destNodeId):
        for edge in self.edgeWidgets:
            if edge.node1.nr == sourceNodeId and edge.node2.nr == destNodeId:
                return True
        return False

    def addWidgetEdge(self, sourceNodeId, destNodeId, cost=0):

        if self.edgeAlreadyExists(sourceNodeId, destNodeId) == False:

            self.addNodeWidget(sourceNodeId) # this does nothing if it already exists (and also adds the node to the internal graph)
            self.addNodeWidget(destNodeId)

            self.graph.addEdge(sourceNodeId, destNodeId, cost)
            edgeWidget = edge_widget.EdgeWidget(self.getNodeWidgetById(sourceNodeId), self.getNodeWidgetById(destNodeId), cost)
            self.edgeWidgets.append(edgeWidget)

    def parse_graph_data(self, data):
        """Data is a string in the format "node_1_Id" + " " + "node_2_Id" which holds all the necessary data for creating the graph."""

        if data != "":
            lines = data.split('\n')
            self.graph = graph.Graph(self.isDirected)
            self.nodeWidgets = []
            self.edgeWidgets = []

            if lines != None:
                for line in lines:
                    if line != "":

                        value = self.interpretLine(line) # on a line can be an isolated node, an unweighted edge, an weighted edge
                                             # an empty string or invalid sintax
                                             # see function description for more information

                        if value == -1:
                            raise GraphException("Invalid format for the adjacency list!")
                        elif len(value) == 0:
                            pass
                        elif len(value) == 1:
                            self.addNodeWidget(value[0])
                        elif len(value) == 2:
                            self.addWidgetEdge(value[0], value[1])
                        elif len(value) == 3:
                            self.addWidgetEdge(value[0], value[1], value[2])

        self.update_canvas()
        self.graph.printGraph()

    def addNodeFromDrawing(self, node):
        self.nodeWidgets.append(node)

    def randomizePositions(self):
        coords = [10, 10,
                  int(self.mainViewWidget.ids.graph_canvas.size[0] - 50),
                  int(self.mainViewWidget.ids.graph_canvas.size[1] - 50)]
        for v in self.nodeWidgets:
            x1 = random.randrange(coords[0], coords[2])
            y1 = random.randrange(coords[1], coords[3])

            v.pos = [x1, y1]

        self.update_canvas()