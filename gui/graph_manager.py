from graph import graph
from graph.graph_exception import GraphException
import random

from gui import node_widget


class GraphManager:

    def __init__(self, isDirected, mainViewWidget):
        self.mainViewWidget = mainViewWidget
        self.graph = graph.Graph(isDirected)
        self.nodeWidgets = []   # the list of ids of the WidgetNodes
        self.isDirected = isDirected

    def getNodeWidgetList(self):
        return self.nodeWidgets

    def NodeWidgetExists(self, nodeId): # verify if a NodeWidget exists
        exists = False
        for node in self.nodeWidgets:
            if node == nodeId:
                exists = True

        return exists

    def isIsolatedNode(self,  text):    # returns -1 for invalid format, 0 it it is not isolated and the id if it is
        finished = False
        for index in range(len(text)):
            if text[index].isdigit():
                if finished == False:
                    number = int(text[index])
                    index += 1
                    while index < len(text) and text[index].isdigit():
                        number = number * 10 + text[index]
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
                        source = source * 10 + text[index]
                        index += 1
                    foundSource = True
                elif foundDest == False:
                    dest = int(text[index])
                    index += 1
                    while index < len(text) and text[index].isdigit():
                        dest = dest * 10 + text[index]
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
                        source = source * 10 + text[index]
                        index += 1
                    foundSource = True
                elif foundDest == False:
                    dest = int(text[index])
                    index += 1
                    while index < len(text) and text[index].isdigit():
                        dest = dest * 10 + text[index]
                        index += 1
                    foundDest = True
                elif foundCost == False:
                    cost = int(text[index])
                    index += 1
                    while index < len(text) and text[index].isdigit():
                        cost = cost * 10 + text[index]
                        index += 1
                    foundDest = True
                else:
                    return -1
            elif text[index] != ' ' and text[index] != '\n':
                return -1

        return [source, dest, cost]

    def parse_graph_data(self, data):
        """Data is a string in the format "node_1_Id node_2_Id" which holds all the necessary data for creating the graph."""

        if data != "":
            lines = data.split('\n') # edges or isolated nodes
            self.graph = graph.Graph(self.isDirected)
            self.nodeWidgets = []
            if lines != None:
                for line in lines:
                    if line != "":

                        node = self.isIsolatedNode(line)

                        if  node != 0 and node != -1:
                            self.graph.addNode(node)

                            if self.NodeWidgetExists(node) == False:
                                node_widget.setmaxid(node)
                                self.mainViewWidget.ids.graph_canvas.add_widget(node_widget.NodeWidget(node,
                                                                                                       [random.randrange(30, 200),
                                                                                                        random.randrange(30, 200)]))
                                self.nodeWidgets.append(node)

                        elif node != -1:
                            edge = self.isEdgeWithoutWeight(line)
                            if edge != 1 and edge != 0:
                                alreadyExists = False
                                self.graph.addNode(edge[0], alreadyExists)
                                if alreadyExists == False:
                                    if self.NodeWidgetExists(edge[0]) == False:
                                        node_widget.setmaxid(edge[0])
                                        self.mainViewWidget.ids.graph_canvas.add_widget(node_widget.NodeWidget(edge[0],
                                                                                                           [random.randrange(30,
                                                                                                                             200),
                                                                                                            random.randrange(30,
                                                                                                                             200)]))
                                        self.nodeWidgets.append(edge[0])

                                alreadyExists = False
                                self.graph.addNode(edge[1], alreadyExists)
                                if alreadyExists == False:
                                    if self.NodeWidgetExists(edge[1]) == False:
                                        node_widget.setmaxid(edge[1])
                                        self.mainViewWidget.ids.graph_canvas.add_widget(node_widget.NodeWidget(edge[1],
                                                                                                           [random.randrange(30,
                                                                                                                             200),
                                                                                                            random.randrange(30,
                                                                                                                             200)]))
                                        self.nodeWidgets.append(edge[1])

                                self.graph.addEdge(edge[0], edge[1])

                            elif edge == 0:
                                edge = self.isWeightedEdge(line)
                                if edge != -1:
                                    alreadyExists = False
                                    self.graph.addNode(edge[0], alreadyExists)
                                    if alreadyExists == False:
                                        if self.NodeWidgetExists(edge[0]) == False:
                                            node_widget.setmaxid(edge[0])
                                            self.mainViewWidget.ids.graph_canvas.add_widget(node_widget.NodeWidget(edge[0],
                                                                                                               [random.randrange(30,
                                                                                                                                 200),
                                                                                                                random.randrange(30,
                                                                                                                                 200)]))
                                            self.nodeWidgets.append(edge[0])

                                    alreadyExists = False
                                    self.graph.addNode(edge[1], alreadyExists)
                                    if alreadyExists == False:
                                        if self.NodeWidgetExists(edge[1]) == False:
                                            node_widget.setmaxid(edge[1])
                                            self.mainViewWidget.ids.graph_canvas.add_widget(node_widget.NodeWidget(edge[1],
                                                                                                               [random.randrange(30,
                                                                                                                                 200),
                                                                                                                random.randrange(30,
                                                                                                                                 200)]))
                                            self.nodeWidgets.append(edge[1])

                                    self.graph.addEdge(edge[0], edge[1], edge[2])

                                else:
                                    raise GraphException("Invalid format for the adjacency list!")

                            else:
                                raise GraphException("Invalid format for the adjacency list!")

                        else:
                            raise GraphException("Invalid format for the adjacency list!")

        """
        edges = data.split()
        self.graph = graph.Graph(self.isDirected)
        self.nodeWidgets = []

        for source, dest in zip(edges[0::2], edges[1::2]):  # data[0::2] creates subset collection of elements with (index % 2 == 0)
                                                            # zip(x,y) creates a tuple collection
            try:
                source = int(source)
            except:
                raise GraphException('The source node id must be a positive integer.')
            try:
                dest = int(dest)
            except:
                raise GraphException('The dest node id must be a positive integer.')

            self.graph.addNode(source)
            # (random.randrange(30, 200), random.randrange(30, 200))
            node_widget.maxid += 1
            self.mainViewWidget.ids.graph_canvas.add_widget(node_widget.NodeWidget(node_widget.getmaxid(), [random.randrange(30, 200), random.randrange(30, 200)]))
            self.graph.addNeighbourNode(source, dest)
        """

        self.graph.printGraph()

    def addNodeFromDrawing(self, node):
        self.nodeWidgets.append(node)