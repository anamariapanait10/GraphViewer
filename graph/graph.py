from .graph_exception import GraphException


class Node:

    def __init__(self, id): #the neighbors will be represented as a list of edges where the source node is "self" node
        self.id = id        #and the destination node will be all his neighbors at a time
        self.neighbors = [] #example: the graph has edges between node 1 and node 2, node 2 and node 3, node 1 and node 3;
                            #         node 1 will have the id 1 and list neighnors will be [Edge(1,2), Edge(1,3)]
#Note that the id DOES NOT represent the index in the list of nodes, because when I add nodes to the list I do not
#correlate the id with the index (example: If a want to add the node with the id 2 (and the list is empty),
# it will be put first in the list, so his index in the list will be 1)

class Edge:

    def __init__(self, source, dest, cost=-1):  #cost is optional, if it does not receive any value,
        self.source = source                    # it will receive the default value (-1) and will be considered at no cost
        self.dest = dest


class Graph:
    """"This is a class that represents a directed or undirected graph with the help of neighbors list"""

    def __init__(self, isDirected):     #isDirected will receive a bool value, True means the graph is directed,
        self.isDirected = isDirected    #False means the contrary
        self.nodes = []                 #the list of nodes in the order of their addition


    def getNodeById(self, id):  #this function is nedeed because the id of a node is not equal to its index in the list
                                #of nodes and I have to search through the list to find a node by id

        """Function that returns an object of class Node with the Id id"""

        nd = None
        for n in self.nodes:
            if n.id == id:
                nd = n
                break
        return nd


    def addNode(self, nodeId):
        """This method adds a node to the graph.
            :param nodeId id of the new node
        """
        try:
            nodeId = int(nodeId)
        except ValueError:
            raise GraphException('Node id must be an integer!')

        ok = True
        for n in self.nodes:
            if n.id == nodeId:
                ok = False

        if ok:
            newNode = Node(nodeId)
            self.nodes.append(newNode)
        else:
            raise GraphException('Node alreeady exists!')


    def addEdge(self, src, dest, cost=-1):
        for n in self.nodes:
            if n.id == src:
                ok = True
                for e in n.neighbors:
                    if dest == e.dest:
                        ok = False
                        break
                if ok:
                    n.neighbors.append(Edge(src, dest, cost))
                else:
                    raise GraphException('Edge already exists!')

            if n.id == dest and not self.isDirected:
                ok = True
                for e in n.neighbors:
                    if src == e.dest:
                        ok = False
                        break
                if ok:
                    n.neighbors.append(Edge(dest, src, cost))


    def removeNode(self, nodeId):
        nd = self.getNodeById(nodeId)

        if nd == None:
            raise GraphException("Node does not exist!")

        if not self.isDirected:
            for neighbor in nd.neighbors:
                destNode = self.getNodeById(neighbor.dest)
                for edge in destNode.neighbors[:]:
                    if edge.dest == nd.id:
                        destNode.neighbors.remove(edge)
        else:
            for neighbor in self.nodes:
                destNode = self.getNodeById(neighbor.dest)
                for edge in destNode.neighbors[:]:
                    if edge.dest == nd.id:
                        destNode.neighbors.remove(edge)

        self.nodes.remove(nd)


    def removeEdge(self, src, dest):
        if not self.isDirected:
            for n in self.nodes:
                if n.id == src:
                    for e in n.neighbors[:]:
                        if e.dest == dest:
                            n.neighbors.remove(e)

                if n.id == dest:
                    for e in n.neighbors[:]:
                        if e.dest == src:
                            n.neighbors.remove(e)
        else:
            for n in self.nodes:
                if n.id == src:
                    for e in n.neighbors[:]:
                        if e.dest == dest:
                            n.neighbors.remove(e)


    def printGraph(self):
        for n in self.nodes:
            print(n.id, end=": ")
            for e in n.neighbors:
                print(e.dest, end=" ")

            print()
