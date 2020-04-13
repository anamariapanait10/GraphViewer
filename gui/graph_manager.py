from graph import graph
from graph.graph_exception import GraphException
import random

from gui import node_widget
from gui import edge_widget


class GraphManager:

    def __init__(self, isDirected, mainViewWidget):
        self.mainViewWidget = mainViewWidget
        self.graph = graph.Graph(isDirected)
        self.nodeWidgets = []   # the list of WidgetNodes
        self.edgeWidgets = []
        self.isDirected = isDirected

    def getNodeWidgetList(self):
        return self.nodeWidgets

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

    def NodeWidgetExists(self, nodeId): # verify if a NodeWidget exists
        exists = False
        for node in self.nodeWidgets:
            if node.nr == nodeId:
                exists = True

        return exists

    def setisDirected(self, TrueOrFalse):
        self.isDirected = TrueOrFalse


    def isIsolatedNode(self,  text):    # returns -1 for invalid format, 0 it it is not isolated and the id if it is
        finished = False
        for index in range(len(text)):
            if text[index].isdigit():
                if finished == False:
                    number = int(text[index])
                    index += 1
                    while index < len(text) and text[index].isdigit():
                        number = number * 10 + int(text[index])
                        index += 1
                    finished  = True
                else:   #it it finds another number then it is not isolated
                    return 0
            elif text[index] != ' ' and text[index] != '\n':
                return -1

        if finished == True:
            return number


    def isEdgeWithoutWeight(self, text):    # returns -1 for invalid sintax, 0 if it is not an edge without weight
        foundSource = False
        foundDest = False
        for index in range(len(text)):
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
                else:
                    return 0
            elif text[index] != ' ' and text[index] != '\n':
                return -1

        return [source, dest]

    def isWeightedEdge(self, text):
        foundSource = False
        foundDest = False
        foundCost = False
        for index in range(len(text)):
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

        return [source, dest, cost]

    def update_canvas(self):
        self.mainViewWidget.ids.graph_canvas.clear_widgets()
        for edge in self.edgeWidgets:
            self.mainViewWidget.ids.graph_canvas.add_widget(edge)
        for node in self.nodeWidgets:
            self.mainViewWidget.ids.graph_canvas.add_widget(node)

    def parse_graph_data(self, data):
        """Data is a string in the format "node_1_Id node_2_Id" which holds all the necessary data for creating the graph."""

        if data != "":
            lines = data.split('\n') # edges or isolated nodes
            self.graph = graph.Graph(self.isDirected)
            self.nodeWidgets = []
            self.edgeWidgets = []

            coords = [10, 10,
                      self.mainViewWidget.ids.graph_canvas.size[0] - 50,
                      self.mainViewWidget.ids.graph_canvas.size[1] - 50]
            # boundary coordonates for spawning the nodes

            if lines != None:
                for line in lines:
                    if line != "":

                        node = self.isIsolatedNode(line)

                        if  node != 0 and node != -1:
                            self.graph.addNode(node)

                            if self.NodeWidgetExists(node) == False:
                                nodeWidget = node_widget.NodeWidget(node,[random.randrange(coords[0], coords[2]),
                                                                               random.randrange(coords[1], coords[3])])
                                self.mainViewWidget.ids.graph_canvas.add_widget(nodeWidget)
                                self.nodeWidgets.append(nodeWidget)

                        elif node == 0:
                            edge = self.isEdgeWithoutWeight(line)
                            if edge != -1 and edge != 0:
                                alreadyExistsSource = self.graph.addNode(edge[0])
                                if alreadyExistsSource == False:
                                    nodeWidgetSource = node_widget.NodeWidget(edge[0], [random.randrange(coords[0], coords[2]),
                                                                               random.randrange(coords[1], coords[3])])

                                    self.nodeWidgets.append(nodeWidgetSource)

                                alreadyExistsDest = self.graph.addNode(edge[1])
                                if alreadyExistsDest == False:
                                    nodeWidgetDest = node_widget.NodeWidget(edge[1], [random.randrange(coords[0], coords[2]),
                                                                               random.randrange(coords[1], coords[3])])
                                    self.nodeWidgets.append(nodeWidgetDest)

                                self.graph.addEdge(edge[0], edge[1])
                                edgeWidget = edge_widget.EdgeWidget(self.getNodeWidgetById(edge[0]),
                                                                    self.getNodeWidgetById(edge[1]))

                                #self.mainViewWidget.ids.graph_canvas.add_widget(edgeWidget)
                                self.edgeWidgets.append(edgeWidget)

                                # I added the nodes on the canvas after the edge because I want to draw them on top of it
                                #if alreadyExistsSource == False:
                                #    self.mainViewWidget.ids.graph_canvas.add_widget(nodeWidgetSource)
                                #if alreadyExistsDest == False:
                                #    self.mainViewWidget.ids.graph_canvas.add_widget(nodeWidgetDest)

                                # self.update_canvas()

                            elif edge == 0:
                                edge = self.isWeightedEdge(line)
                                if edge != -1:
                                    alreadyExistsSource = self.graph.addNode(edge[0])
                                    if alreadyExistsSource == False:
                                        nodeWidgetSource = node_widget.NodeWidget(edge[0], [random.randrange(coords[0], coords[2]),
                                                                               random.randrange(coords[1], coords[3])])
                                        self.nodeWidgets.append(nodeWidgetSource)

                                    alreadyExistsDest = self.graph.addNode(edge[1])
                                    if alreadyExistsDest == False:
                                        nodeWidgetDest = node_widget.NodeWidget(edge[1], [random.randrange(coords[0], coords[2]),
                                                                               random.randrange(coords[1], coords[3])])
                                        self.nodeWidgets.append(nodeWidgetDest)

                                    self.graph.addEdge(edge[0], edge[1], edge[2])
                                    edgeWidget = edge_widget.EdgeWidget(self.getNodeWidgetById(edge[0]),
                                                                        self.getNodeWidgetById(edge[1]), edge[2])
                                    #self.mainViewWidget.ids.graph_canvas.add_widget(edgeWidget)
                                    self.edgeWidgets.append(edgeWidget)

                                    # I added the nodes on the canvas after the edge because I want to draw them on top of it
                                    #if alreadyExistsSource == False:
                                    #    self.mainViewWidget.ids.graph_canvas.add_widget(nodeWidgetSource)
                                    #if alreadyExistsDest == False:
                                    #    self.mainViewWidget.ids.graph_canvas.add_widget(nodeWidgetDest)
                                    # self.update_canvas()

                                else:
                                    raise GraphException("Invalid format for the adjacency list!")

                            else:
                                raise GraphException("Invalid format for the adjacency list!")

                        else:
                            raise GraphException("Invalid format for the adjacency list!")

        self.update_canvas()
        self.graph.printGraph()

    def addNodeFromDrawing(self, node):
        self.nodeWidgets.append(node)