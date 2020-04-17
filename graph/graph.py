from .graph_exception import GraphException


class Node:

    def __init__(self, id):  #  the neighbors will be represented as a list of edges where the source node is "self" node
        self.id = id         #  and the destination node will be all his neighbors at a time
        self.neighbors = []  #  example: the graph has edges between node 1 and node 2, node 2 and node 3, node 1 and node 3;
                             #          node 1 will have the id 1 and list neighnors will be [Edge(1,2), Edge(1,3)]
#  Note that the id DOES NOT represent the index in the list of nodes, because when I add nodes to the list I do not
#  correlate the id with the index (example: If a want to add the node with the id 2 (and the list is empty),
#  it will be put first in the list, so his index in the list will be 1)

class Edge:

    def __init__(self, source, dest, cost=0):  # cost is optional, if it does not receive any value,
        self.source = source                    #  it will receive the default value (0) and will be considered at no cost
        self.dest = dest
        self.cost = cost


class Graph:
    """This is a class that represents a directed or undirected graph with the help of neighbors list"""

    def __init__(self, isDirected):     #  isDirected will receive a bool value, True means the graph is directed,
        self.isDirected = isDirected    #  False means the contrary
        self.nodes = []                 #  the list of nodes in the order of their addition


    def setIsDirected(self, TrueOrFalse):
        self.isDirected = TrueOrFalse

    def getNodeById(self, id):  #  this function is nedeed because the id of a node is not equal to its index in the list
                                #  of nodes and I have to search through the list to find a node by id

        """Function that returns an object of class Node with the Id id"""

        try:
            id = int(id)
        except:
            raise GraphException('Node id must be a positive integer.')

        nd = None
        for n in self.nodes:
            if n.id == id:
                nd = n
                break
        return nd

    def getEdgeByIds(self, sourceId, destId):
        """This method returns an edge by id of the source and destination nodes if exists and creates it if not"""

        source = self.getNodeById(sourceId)

        e = None
        for edg in source.neighbors:
            if(edg.dest == destId):
                e = edg

        if(e == None):  # if edge does not exists, I create it
            self.addEdge(sourceId, destId)
            for edg in source.neighbors:
                if (edg.dest == destId):
                    e = edg

        return e;

    def addNode(self, nodeId): # exists variable tells me if the node existed before calling this method
        """This method adds a node to the graph.
            :param nodeId id of the new node
        """
        try:
            nodeId = int(nodeId)
        except ValueError:
            raise GraphException('Node id must be an integer!')

        nd = self.getNodeById(nodeId)
        if nd == None:  # if it is not found, then we have to add it
            newNode = Node(nodeId)
            self.nodes.append(newNode)
            return False
        else:
            return True
            #  raise GraphException('Node already exists!')

    def addEdge(self, src, dest, cost=0):  #note that src and dest are ids of the nodes
        try:
            cost = int(cost)
        except:
            raise GraphException('The cost must be a positive integer.')

        try:
            src = int(src)
        except:
            raise GraphException('The source node id must be a positive integer.')

        try:
            dest = int(dest)
        except:
            raise GraphException('The destination node id must be a positive integer.')

        for n in self.nodes:
            if n.id == src:
                ok = True
                for e in n.neighbors:
                    if dest == e.dest:
                        ok = False
                        break
                if ok:
                    n.neighbors.append(Edge(src, dest, cost))
                #else:
                #    raise GraphException('Edge already exists!')

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
        try:
            src = int(src)
        except:
            raise GraphException('The source node id must be a positive integer.')

        try:
            dest = int(dest)
        except:
            raise GraphException('The destination node id must be a positive integer.')

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
        print()

