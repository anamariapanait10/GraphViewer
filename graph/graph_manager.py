from graph.graph_exception import GraphException
from graph import node_widget
from graph import edge_widget
import random
from math import sqrt
from globals import globals

class GraphManager:

    def __init__(self, isDirected):
        self.isDirected = isDirected
        self.nodeWidgets = []   # the list of nodes
        self.edgeWidgets = []   # the list of edges

    def getNodeWidgetList(self):
        return self.nodeWidgets

    def getEdgeWidgetList(self):
        return self.edgeWidgets

    def getNodeWidgetById(self, nodeId): # returns None if it does not exists
        try:
            nodeId = int(nodeId)
        except:
            raise GraphException('Node id must be a positive integer.')

        node = None
        for nodeWidget in self.nodeWidgets:
            if nodeWidget.Id == nodeId:
                node = nodeWidget
                break
        return node

    def deleteNodeWidgetById(self, nodeId): 
        for nodeWidget in self.nodeWidgets[:]:
            if nodeWidget.Id == nodeId:
                self.nodeWidgets.remove(nodeWidget)
                break

    def deleteEdgeWidgetById(self, node1Id, node2Id):
        # I put the following conditions because when a graph is undirected it might have two edges overlap if
        # in the input it was given both the edge from the node1 to node2 and from node2 to node1. So in that case
        # both edges must be deleted. It's not the same when the graph is directed.

        if globals.graphManager.getIsDirected() == True:
            for edgeWidget in self.edgeWidgets[:]:
                if edgeWidget.node1.Id == node1Id and edgeWidget.node2.Id == node2Id:
                    self.edgeWidgets.remove(edgeWidget)
                    break
        else:
            for edgeWidget in self.edgeWidgets[:]:
                if edgeWidget.node1.Id == node1Id and edgeWidget.node2.Id == node2Id \
                or edgeWidget.node2.Id == node1Id and edgeWidget.node1.Id == node2Id:
                    self.edgeWidgets.remove(edgeWidget)

    def deleteNodeWidgetByCoords(self, x1, y1): # the x and y are the coordinates of the touch and if they collide with a node, it will be deleted
        for nodeWidget in self.nodeWidgets[:]:
            x2 = nodeWidget.pos[0] + globals.radiusOfNodeWidget + globals.mainViewWidget.ids.graph_canvas.pos[0]
            y2 = nodeWidget.pos[1] + globals.radiusOfNodeWidget + globals.mainViewWidget.ids.graph_canvas.pos[1]
            dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if dist <= globals.radiusOfNodeWidget:
                globals.mainViewWidget.ids.graph_canvas.remove_widget(nodeWidget)
                self.nodeWidgets.remove(nodeWidget)
                return nodeWidget.Id

    def deleteEdgeWidgetByCoords(self, x, y): # the x and y are the coordinates of the touch and if they collide with an edge, it will be deleted
        for edgeWidget in self.edgeWidgets[:]:
            if edgeWidget.collide_point(x, y):
                globals.mainViewWidget.ids.graph_canvas.remove_widget(edgeWidget)
                self.edgeWidgets.remove(edgeWidget)

    def NodeWidgetExists(self, nodeId): # verify if a NodeWidget exists
        exists = False
        for nodeWidget in self.nodeWidgets:
            if nodeWidget.Id == nodeId:
                exists = True

        return exists

    def setisDirected(self, TrueOrFalse):
        self.isDirected = TrueOrFalse

    def getIsDirected(self):
        return self.isDirected

    def interpretLine(self, line):  # returns -1 for invalid syntax
                                    # and a list otherwise, in the following format:
                                    # [ nodeId ] for isolated nodes
                                    # [ node1Id, node2Id ] for unweighted edge
                                    # [ nodeId, node2Id, cost ] for weighted edge

        foundSource = False
        foundDest = False
        foundCost = False
        index = 0

        while index < len(line):

            if line[index].isdigit():

                if foundSource == False:
                    source = int(line[index])
                    index += 1
                    while index < len(line) and line[index].isdigit():
                        source = source * 10 + int(line[index])
                        index += 1
                    foundSource = True

                elif foundDest == False:
                    dest = int(line[index])
                    index += 1
                    while index < len(line) and line[index].isdigit():
                        dest = dest * 10 + int(line[index])
                        index += 1
                    foundDest = True

                elif foundCost == False:
                    cost = int(line[index])
                    index += 1
                    while index < len(line) and line[index].isdigit():
                        cost = cost * 10 + int(line[index])
                        index += 1
                    foundDest = True

                else:
                    return -1

            elif line[index] != ' ' and line[index] != '\n':
                return -1

            else:
                index += 1

        if foundSource == False: # if the condition is True, then it is an empty line
            return []
        elif foundSource == True and foundDest == False: # if the condition is True, then it is an isolated node
            return [source]
        elif foundCost == False:  # if the condition is True, then it is an unweighted edge
            return [source, dest]
        else:    # if the condition is True, then it is an weighted edge
            return [source, dest, cost]


    def update_canvas(self, arg=0):
        """This function clears all widgets from the canvas and creates new widgets with almost the same properties
         except the color and dimensions might change. I was forced to create new widgets because Kivy refreshes
         the visual properties only after next call"""

        globals.mainViewWidget.ids.graph_canvas.clear_widgets()

        for edge in self.edgeWidgets:
            #self.deleteEdgeWidgetById(edge.node1.Id, edge.node2.Id) # this method only removes the edge from de edgeWidgets list
            #new_edge = edge_widget.EdgeWidget(edge.node1, edge.node2)
            #new_edge.updateEdgeWidgetColor()
            #new_edge.id = edge.id
            #self.edgeWidgets.append(new_edge)
           # globals.mainViewWidget.ids.graph_canvas.add_widget(new_edge)
            if self.isDirected == True:
                edge.trianglePoints = edge.getTrianglePoints()
            globals.mainViewWidget.ids.graph_canvas.add_widget(edge)


        for node in self.nodeWidgets[:]:
            # self.deleteNodeWidgetById(node.Id) # this method only removes the node from de nodeWidgets list
            # new_node = node_widget.NodeWidget(node.Id, [node.pos[0], node.pos[1]])
            node.setLabelId(node.Id)
            node.color = globals.NodeWidgetColor
            node.backgroundColor = globals.NodeWidgetBackgroundColor

            # del node
            # self.nodeWidgets.append(new_node)
            globals.mainViewWidget.ids.graph_canvas.add_widget(node)


    def update_text(self, text, nodeId): # this function updates the text when the user eliminates a node by double click
        if text != "":
            lines = text.split('\n')
            if lines != None:
                new_text = ""
                for line in lines:
                    if line != "":
                        value = self.interpretLine(line)
                        if value == -1:
                            raise GraphException("Invalid format for the adjacency list!")
                        elif len(value) == 0:
                            pass
                        elif len(value) == 1:
                            if value[0] != nodeId:
                                new_text += line + "\n"
                        elif len(value) == 2 or len(value) == 3:
                            if value[0] != nodeId and value[1] != nodeId:
                                new_text += line + "\n"
                            elif value[0] == nodeId:
                                node = self.getNodeWidgetById(value[1])
                                if len(node.neighbors) == 1: # if it has only one neighbor, with the id nodeId, it won't have anymore after deleting
                                    new_text += str(value[1]) + "\n"
                            elif value[1] == nodeId:
                                node = self.getNodeWidgetById(value[0])
                                if len(node.neighbors) == 1:  # if it has only one neighbor, with the id nodeId, it won't have anymore after deleting
                                    new_text += str(value[0]) + "\n"

                globals.mainViewWidget.ids.input_nodes.text = new_text


    def nodeWidgetsDontOverlap(self):   # This function generates random coordinates for the NodeWidget
                                        # which do not overlap the other nodes

         # boundary coordonates for spawning the nodes
        coords = [10, 10,
                  int(globals.mainViewWidget.ids.graph_canvas.size[0] - 50),
                  int(globals.mainViewWidget.ids.graph_canvas.size[1] - 50)]

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

    def addNodeWidget(self, nodeId, pos=0):

        if self.NodeWidgetExists(nodeId) == False:
            if pos == 0:
                pos = self.nodeWidgetsDontOverlap() # This function generates random positions which do not overlap the other nodes
            new_nodeWidget = node_widget.NodeWidget(nodeId, pos)
            self.nodeWidgets.append(new_nodeWidget)

    def edgeAlreadyExists(self, node1Id, node2Id):
        for edge in self.edgeWidgets:
            if int(edge.node1.Id) == node1Id and int(edge.node2.Id) == node2Id:
                return True
        return False

    def addEdgeWidget(self, node1Id, node2Id, cost=0):

        if self.edgeAlreadyExists(node1Id, node2Id) == False:

            new_edgeWidget = edge_widget.EdgeWidget(self.getNodeWidgetById(node1Id), self.getNodeWidgetById(node2Id), cost)
            self.edgeWidgets.append(new_edgeWidget)

    def interpretAdjacencyList(self, line):# returns -1 for invalid syntax
                                    # and a list otherwise, in the following format:
                                    # [ nodeId, [neighbor1Id, neighbor2Id, ...]]

        foundNode = False
        foundNeighbors = False
        index = 0

        while index < len(line):

            if line[index].isdigit():

                if foundNode == False:
                    node = int(line[index])
                    index += 1
                    while index < len(line) and line[index].isdigit():
                        node = node * 10 + int(line[index])
                        index += 1
                    foundNode = True

                elif foundNeighbors == False:
                    neighbors =[]
                    while index < len(line):
                        if line[index].isDigit() == True:
                            neighbor = int(line[index])
                            index += 1
                            while index < len(line) and line[index].isdigit():
                                neighbor = neighbor * 10 + int(line[index])
                                index += 1
                        elif line[index] != ' ' and line[index] != '\n' and line[index] != ',':
                            return -1
                        else:
                            neighbors.append(neighbor)
                            index += 1

            elif line[index] != ' ' and line[index] != '\n' and line[index] != ',':
                return -1
            else:
                index += 1

        if foundNode == False: # if the condition is True, then it is an empty line
            return []
        elif foundNode == True and foundNeighbors == False: # if the condition is True, then it has no neighbors
            return [node,[]]
        else:
            return [node, neighbors]

    def interpretAdjacencyMatrix(self, nodeId, line): # returns -1 for invalid syntax #TODO: verifica daca are nr de coloanele si linii egale
                                              # and a list otherwise, in the following format:
                                              # [ nodeId, [neighbor1Id, neighbor2Id, ...]]
        index = 0
        neighbors = []
        while index < len(line):
            if line[index].isdigit():

                if foundNode == False:
                    node = int(line[index])
                    index += 1
                    while index < len(line) and line[index].isdigit():
                        node = node * 10 + int(line[index])
                        index += 1
                    foundNode = True



        return [nodeId, neighbors]

    def interpretCostMatrix(self, nodeId, line): # returns -1 for invalid syntax
                                                 # and a list otherwise, in the following format:
                                                 # [ nodeId, [[ neighbor1Id, cost ], [ neighbor2Id, cost ] ...]]
        index = 0
        neighbors = []
        while index < len(line):

            if line[index].isdigit():
                neighbors.append(index + 1)
            elif line[index] != ' ' and line[index] != '\n' and line[index] != '0':
                return -1

            index += 1

        return [nodeId, neighbors]

    def parse_graph_data(self, dummy=0, data=""):
        """Data is a string in the format "node_1_Id" + " " + "node_2_Id" which holds all the necessary data for creating the graph."""

        if data == "":
            data = globals.mainViewWidget.ids.input_nodes.text

        if data != "":
            lines = data.split('\n')
            lastNodeWidgetsList = self.nodeWidgets
            self.nodeWidgets = []
            self.edgeWidgets = []
            nodeId = 1

            if lines != None:
                for line in lines:
                    if line != "":
                        if globals.listOfEdgesBtn == True:
                            value = self.interpretLine(line) # on a line can be an isolated node, an unweighted edge, an weighted edge
                                                 # an empty string or invalid sintax
                                                 # see function description for more information

                            if value == -1:
                                raise GraphException("Invalid format for the edges list!")
                            elif len(value) == 0:
                                pass
                            elif len(value) == 1:
                                pos = 0
                                for node in lastNodeWidgetsList:
                                    if node.Id == value[0]:
                                        pos = node.pos
                                        break
                                self.addNodeWidget(value[0], pos)

                            else:
                                if len(value) == 2:
                                    if value[0] != value[1]:
                                        pos = 0
                                        for node in lastNodeWidgetsList:
                                            if node.Id == value[0]:
                                                pos = node.pos
                                                break
                                        self.addNodeWidget(value[0], pos)  # this does nothing if it already exists
                                        pos = 0
                                        for node in lastNodeWidgetsList:
                                            if node.Id == value[1]:
                                                pos = node.pos
                                                break
                                        self.addNodeWidget(value[1], pos)
                                        self.addEdgeWidget(value[0], value[1])
                                if len(value) == 3:
                                    if value[0] != value[1]:
                                        pos = 0
                                        for node in lastNodeWidgetsList:
                                            if node.Id == value[0]:
                                                pos = node.pos
                                                break
                                        self.addNodeWidget(value[0], pos)  # this does nothing if it already exists
                                        pos = 0
                                        for node in lastNodeWidgetsList:
                                            if node.Id == value[1]:
                                                pos = node.pos
                                                break
                                        self.addNodeWidget(value[1], pos)
                                        self.addEdgeWidget(value[0], value[1], value[2])

                                if self.isDirected == True:
                                    if value[0] != value[1]:
                                        for node in self.nodeWidgets:
                                            if node.Id == value[0]:
                                                node.neighbors.append(self.getNodeWidgetById(value[1]))
                                                break
                                else:
                                    if value[0] != value[1]:
                                        for node in self.nodeWidgets:
                                            if node.Id == value[0]:
                                                node.neighbors.append(self.getNodeWidgetById(value[1]))
                                            if node.Id == value[1]:
                                                node.neighbors.append(self.getNodeWidgetById(value[0]))

                        elif globals.adjacencyListBtn == True or globals.adjacencyMatrixBtn == True:

                            if globals.adjacencyListBtn == True:
                                value = self.interpretAdjacencyList(line)
                                if value == -1:
                                    raise GraphException("Invalid format for the adjacency list!")
                            if globals.adjacencyMatrixBtn == True:
                                value = self.interpretAdjacencyMatrix(nodeId, line)
                                nodeId += 1
                                if value == -1:
                                    raise GraphException("Invalid format for the adjacency matrix!")

                            nodeWidget = self.addNodeWidget(value[0])
                            for node in nodeWidget[1]:
                                if node.Id != nodeWidget.Id:
                                    node = self.addNodeWidget(node)
                                    self.addEdgeWidget(nodeWidget, node)

                                    if self.isDirected == True:
                                        nodeWidget.neighbors.append(node)
                                    else:
                                        nodeWidget.neighbors.append(node)
                                        node.neighbors.append(nodeWidget)

                        else: # when globals.costMatrixBtn == True
                            self.interpretCostMatrix()

        self.update_canvas()
        self.printGraph()

    def addNodeFromDrawing(self, node):
        node.setLabelId(node.Id)
        self.nodeWidgets.append(node)

    def printGraph(self):
        for node in self.nodeWidgets:
            print(node.Id, end=": ")
            for neighbor in node.neighbors:
                print(neighbor.Id, end=" ")
            print()
        print()
