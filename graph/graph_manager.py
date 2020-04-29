from graph.graph_exception import GraphException
from graph import node_widget
from graph import edge_widget
import random
from math import sqrt
from globals import globals

class GraphManager:

    def __init__(self, is_directed):
        self.is_directed = is_directed
        self.node_widgets = []   # the list of nodes
        self.edge_widgets = []   # the list of edges

    def getNodeWidgetList(self):
        return self.node_widgets

    def getEdgeWidgetList(self):
        return self.edge_widgets

    def getNodeWidgetById(self, node_id): # returns None if it does not exists
        try:
            node_id = int(node_id)
        except:
            raise GraphException('Node id must be a positive integer.')

        node = None
        for node_widget in self.node_widgets:
            if node_widget.Id == node_id:
                node = node_widget
                break
        return node

    def deleteNodeWidgetById(self, node_id):
        for node_widget in self.node_widgets[:]:
            if node_widget.Id == node_id:
                self.node_widgets.remove(node_widget)
                break

    def deleteEdgeWidgetById(self, node1_id, node2_id):
        # I put the following conditions because when a graph is undirected it might have two edges overlap if
        # in the input it was given both the edge from the node1 to node2 and from node2 to node1. So in that case
        # both edges must be deleted. It's not the same when the graph is directed.

        if globals.graph_manager.getIsDirected() == True:
            for edge_widget in self.edge_widgets[:]:
                if edge_widget.node1.Id == node1_id and edge_widget.node2.Id == node2_id:
                    self.edge_widgets.remove(edge_widget)
                    break
        else:
            for edge_widget in self.edge_widgets[:]:
                if edge_widget.node1.Id == node1_id and edge_widget.node2.Id == node2_id \
                or edge_widget.node2.Id == node1_id and edge_widget.node1.Id == node2_id:
                    self.edge_widgets.remove(edge_widget)

    def deleteNodeWidgetByCoords(self, x1, y1):  # the x and y are the coordinates of the touch and if they collide with
        for node_widget in self.node_widgets[:]:  # a node, it will be deleted
            x2 = node_widget.pos[0] + globals.node_radius + globals.main_view_widget.ids.graph_canvas.pos[0]
            y2 = node_widget.pos[1] + globals.node_radius + globals.main_view_widget.ids.graph_canvas.pos[1]
            dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if dist <= globals.node_radius:
                globals.main_view_widget.ids.graph_canvas.remove_widget(node_widget)
                self.node_widgets.remove(node_widget)
                return node_widget.Id

    def deleteEdgeWidgetByCoords(self, x, y):    # the x and y are the coordinates of the touch and if they collide with
        for edge_widget in self.edge_widgets[:]:  # an edge, it will be deleted
            if edge_widget.collide_point(x, y):
                globals.main_view_widget.ids.graph_canvas.remove_widget(edge_widget)
                self.edge_widgets.remove(edge_widget)

    def NodeWidgetExists(self, node_id): # verify if a NodeWidget exists
        exists = False
        for node_widget in self.node_widgets:
            if node_widget.Id == node_id:
                exists = True

        return exists

    def setisDirected(self, true_or_false):
        self.is_directed = true_or_false

    def getIsDirected(self):
        return self.is_directed

    def interpretLine(self, line):  # returns -1 for invalid syntax
                                    # and a list otherwise, in the following format:
                                    # [ node_id ] for isolated nodes
                                    # [ node1_id, node2_id ] for unweighted edge
                                    # [ node1_id, node2_id, cost ] for weighted edge

        found_source = False
        found_dest = False
        found_cost = False
        index = 0

        while index < len(line):

            if line[index].isdigit():

                if not found_source:
                    source = int(line[index])
                    index += 1
                    while index < len(line) and line[index].isdigit():
                        source = source * 10 + int(line[index])
                        index += 1
                    found_source = True

                elif not found_dest:
                    dest = int(line[index])
                    index += 1
                    while index < len(line) and line[index].isdigit():
                        dest = dest * 10 + int(line[index])
                        index += 1
                    found_dest = True

                elif found_cost == False:
                    cost = int(line[index])
                    index += 1
                    while index < len(line) and line[index].isdigit():
                        cost = cost * 10 + int(line[index])
                        index += 1
                    found_cost = True

                else:
                    return -1

            elif line[index] != ' ' and line[index] != '\n':
                return -1

            else:
                index += 1

        if found_source == False: # if the condition is True, then it is an empty line
            return []
        elif found_source == True and found_dest == False: # if the condition is True, then it is an isolated node
            return [source]
        elif found_cost == False:  # if the condition is True, then it is an unweighted edge
            return [source, dest]
        else:    # if the condition is True, then it is an weighted edge
            return [source, dest, cost]

    def update_canvas(self, arg=0):

        globals.main_view_widget.ids.graph_canvas.clear_widgets()

        for edge in self.edge_widgets:
            if self.is_directed == True:
                edge.triangle_points = edge.getTrianglePoints()
            globals.main_view_widget.ids.graph_canvas.add_widget(edge)

        for node in self.node_widgets:
            globals.main_view_widget.ids.graph_canvas.add_widget(node)


    def update_text_on_edgeAdd(self):

        new_text = ""

        for edge in self.edge_widgets:
            new_text += str(edge.node1.Id) + " " + str(edge.node2.Id) + "\n"

        for node in self.node_widgets:
            if len(node.neighbors) == 0:
                new_text += str(node.Id) + "\n"

        globals.main_view_widget.ids.input_text.text = new_text

    def update_text_on_delete(self, text, nodeId): # this function updates the text when the user eliminates a node by double click
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

                globals.main_view_widget.ids.input_text.text = new_text


    def nodeWidgetsDontOverlap(self):   # This function generates random coordinates for the NodeWidget
                                        # which do not overlap the other nodes

         # boundary coordonates for spawning the nodes
        coords = [10, 10,
                  int(globals.main_view_widget.ids.graph_canvas.size[0] - 50),
                  int(globals.main_view_widget.ids.graph_canvas.size[1] - 50)]

        while(True):    # TODO= Put a boundary...
            x1 = random.randrange(coords[0], coords[2])
            y1 = random.randrange(coords[1], coords[3])

            GoodCoords = True
            for nodeWidget in self.node_widgets:
                x2 = nodeWidget.pos[0]
                y2 = nodeWidget.pos[1]
                dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if dist < 2 * globals.node_radius + globals.minimum_distance_between_nodes:
                    GoodCoords = False
                    break

            if GoodCoords == True:
                return [x1, y1]

    def addNodeWidget(self, nodeId, pos=0):

        if self.NodeWidgetExists(nodeId) == False:
            if pos == 0:
                pos = self.nodeWidgetsDontOverlap() # This function generates random positions which do not overlap the other nodes
            new_nodeWidget = node_widget.NodeWidget(nodeId, pos)
            self.node_widgets.append(new_nodeWidget)
            globals.main_view_widget.ids.graph_canvas.add_widget(new_nodeWidget)
            return new_nodeWidget

    def edgeAlreadyExists(self, node1Id, node2Id):
        for edge in self.edge_widgets:
            if int(edge.node1.Id) == node1Id and int(edge.node2.Id) == node2Id:
                return True
        return False

    def addEdgeWidget(self, node1Id, node2Id, cost=0):

        if node1Id != node2Id and self.edgeAlreadyExists(node1Id, node2Id) == False:

            new_edgeWidget = edge_widget.EdgeWidget(self.getNodeWidgetById(node1Id), self.getNodeWidgetById(node2Id), cost)
            self.edge_widgets.append(new_edgeWidget)
            globals.main_view_widget.ids.graph_canvas.add_widget(new_edgeWidget, 200)

    def interpretAdjacencyList(self, line):# returns -1 for invalid syntax
                                    # and a list otherwise, in the following format:
                                    # [ nodeId, [neighbor1Id, neighbor2Id, ...]]

        found_node = False
        found_neighbors = False
        neighbors = []
        index = 0

        while index < len(line):

            if line[index].isdigit():

                if found_node == False:
                    node = int(line[index])
                    index += 1
                    while index < len(line) and line[index].isdigit():
                        node = node * 10 + int(line[index])
                        index += 1
                    found_node = True

                elif found_neighbors == False:

                    while index < len(line):
                        if line[index].isdigit() == True:
                            neighbor = int(line[index])
                            index += 1
                            while index < len(line) and line[index].isdigit():
                                neighbor = neighbor * 10 + int(line[index])
                                index += 1
                            neighbors.append(neighbor)
                            index += 1
                        elif line[index] != ' ' and line[index] != '\n' and line[index] != ':' and line[index] != ',':
                            return -1
                    found_neighbors == True

            elif line[index] != ' ' and line[index] != '\n' and line[index] != ':' and line[index] != ',':
                return -1
            else:
                index += 1

        if found_node == False: # if the condition is True, then it is an empty line, I don't think it really needs this condition
            return []
        else:
            return [node, neighbors]

    def interpretAdjacencyMatrix(self, nodeId, line): # returns -1 for invalid syntax #TODO: verifica daca are nr de coloanele si linii egale
                                              # and a list otherwise, in the following format:
                                              # [ nodeId, [neighbor1Id, neighbor2Id, ...]]
        found_node = False
        index = 0
        neighbors = []
        while index < len(line):
            if line[index].isdigit():

                if found_node == False:
                    node = int(line[index])
                    index += 1
                    while index < len(line) and line[index].isdigit():
                        node = node * 10 + int(line[index])
                        index += 1
                    found_node = True


        return [nodeId, neighbors]

    def returnOldPosition(self, node_id, last_node_widgets_list):
        pos = 0
        for node in last_node_widgets_list:
            if node.Id == node_id:
                pos = node.pos
                break
        return pos

    def interpretCostMatrix(self, node_id, line): # returns -1 for invalid syntax
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

        return [node_id, neighbors]

    def deleteOldNodes(self, last_node_widgets_list):
        globals.graph_manager.node_widgets.sort(key=lambda node: node.Id)
        for node in last_node_widgets_list:
            result = globals.binarySearch(globals.graph_manager.node_widgets, 0, len(globals.graph_manager.node_widgets) - 1, node.Id)
            if result == -1:
                globals.main_view_widget.ids.graph_canvas.remove_widget(node)

    def deleteOldEdges(self, last_edge_widgets_list):
        for edge in last_edge_widgets_list:
            if self.edgeAlreadyExists(edge.node1.Id, edge.node2.Id) == False:
                globals.main_view_widget.ids.graph_canvas.remove_widget(edge)

    def parse_graph_data(self, dummy=0, data=""):
        """Data is a string in the format "node_1_Id" + " " + "node_2_Id" which holds all the necessary data for creating the graph."""

        if data == "":
            data = globals.main_view_widget.ids.input_text.text
        globals.main_view_widget.ids.graph_canvas.clear_widgets()

        if data != "":
            lines = data.split('\n')
            last_node_widgets_list = self.node_widgets
            last_edge_widgets_list = self.edge_widgets
            self.node_widgets = []
            self.edge_widgets = []
            node_id = 1

            if lines:
                for line in lines:
                    if line != "":
                        if globals.edge_list_input_btn == True:
                            value = self.interpretLine(line) # on a line can be an isolated node, an unweighted edge, an weighted edge
                                                             # an empty string or invalid syntax
                                                             # see function description for more information

                            if value == -1:
                                raise GraphException("Invalid format for the edges list!")
                            elif len(value) == 0:
                                pass
                            elif len(value) == 1:
                                self.addNodeWidget(value[0], pos=self.returnOldPosition(value[0], last_node_widgets_list))
                            else:
                                if len(value) == 2:
                                    if value[0] != value[1]:

                                        self.addNodeWidget(value[0], pos=self.returnOldPosition(value[0], last_node_widgets_list))  # this does nothing if it already exists
                                        self.addNodeWidget(value[1], pos=self.returnOldPosition(value[1], last_node_widgets_list))
                                        self.addEdgeWidget(value[0], value[1])

                                if len(value) == 3:
                                    if value[0] != value[1]:

                                        self.addNodeWidget(value[0], pos=self.returnOldPosition(value[0], last_node_widgets_list))
                                        self.addNodeWidget(value[1], pos=self.returnOldPosition(value[1], last_node_widgets_list))
                                        self.addEdgeWidget(value[0], value[1], value[2])

                                if self.is_directed == True:
                                    if value[0] != value[1]:
                                        for node in self.node_widgets:
                                            if node.Id == value[0]:
                                                node.neighbors.append(self.getNodeWidgetById(value[1]))
                                                break
                                else:
                                    if value[0] != value[1]:
                                        for node in self.node_widgets:
                                            if node.Id == value[0]:
                                                node.neighbors.append(self.getNodeWidgetById(value[1]))
                                            if node.Id == value[1]:
                                                node.neighbors.append(self.getNodeWidgetById(value[0]))
                                self.deleteOldNodes(last_node_widgets_list)
                                self.deleteOldEdges(last_edge_widgets_list)

                        elif globals.adjacency_list_input_btn == True or globals.adjacency_matrix_input_btn == True:

                            if globals.adjacency_list_input_btn == True:
                                value = self.interpretAdjacencyList(line)
                                if value == -1:
                                    raise GraphException("Invalid format for the adjacency list!")
                            if globals.adjacency_matrix_input_btn == True:
                                value = self.interpretAdjacencyMatrix(node_id, line)
                                node_id += 1
                                if value == -1:
                                    raise GraphException("Invalid format for the adjacency matrix!")


                            self.addNodeWidget(value[0], pos=self.returnOldPosition(value[0], last_node_widgets_list))
                            nodeWidget = self.getNodeWidgetById(value[0])
                            for node in value[1]:
                                if node != nodeWidget.Id:
                                    self.addNodeWidget(node, pos=self.returnOldPosition(node, last_node_widgets_list))
                                    node = self.getNodeWidgetById(node)
                                    self.addEdgeWidget(nodeWidget.Id, node.Id)

                                    if self.is_directed == True:
                                        nodeWidget.neighbors.append(node)
                                    else:
                                        nodeWidget.neighbors.append(node)
                                        node.neighbors.append(nodeWidget)

                        else: # when globals.costMatrixBtn == True
                            self.interpretCostMatrix()

        #self.update_canvas()

        self.printGraph()

    #def addNodeFromDrawing(self, node):
    #    self.node_widgets.append(node)

    def printGraph(self):
        for node in self.node_widgets:
            print(node.Id, end=": ")
            for neighbor in node.neighbors:
                print(neighbor.Id, end=" ")
            print()
        print()

    def getIndexFromListOfNodes(self, node):
        index = -1
        for n in self.node_widgets:
            index += 1
            if node.Id == n.Id:
                return index