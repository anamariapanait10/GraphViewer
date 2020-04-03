from graph import graph

class GraphManager:

    def __init__(self, isDirected):
        self.graph = graph.Graph(isDirected)

    def parse_graph_data(self, data):
        """Data is a string in the format ... which holds all the necessary data for creating the graph."""
        print(data)
        pass