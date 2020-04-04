from graph import graph
from graph.graph_exception import GraphException

class GraphManager:

    def __init__(self, isDirected):
        self.graph = graph.Graph(isDirected)

    def parse_graph_data(self, data):
        """Data is a string in the format "node_1_Id node_2_Id" which holds all the necessary data for creating the graph."""

        edges = data.split()
        myGraph = graph.Graph(False)

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

            myGraph.addNode(source)
            myGraph.addNeighbourNode(source, dest)


        myGraph.printGraph();
