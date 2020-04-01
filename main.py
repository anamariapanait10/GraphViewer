from graph.graph import Graph
from gui.GraphGeneratorApp import GraphGeneratorApp


if __name__ == '__main__':

    GraphGeneratorApp().run()

    '''myGraph = Graph(False)
    myGraph.addNode(1)
    myGraph.addNode(2)
    myGraph.addNode(3)
    myGraph.addNode(4)

    myGraph.addEdge(1, 2)
    myGraph.addEdge(3, 4)
    myGraph.addEdge(1, 3)
    myGraph.addEdge(1, 4)

    myGraph.printGraph()

    print()

    myGraph.removeNode(3)

    myGraph.printGraph()'''