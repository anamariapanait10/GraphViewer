from globals import globals
from kivy.clock import Clock
from functools import partial
from kivy.uix.popup import Popup
from gui import popup_widget
from graph.graph_exception import GraphException

class BFS():

    visited = None
    queue = None
    isFirstTime = True

    def BFSUtil(self, queue, visited, dummy):
        if len(queue) != 0 and globals.main_view_widget.ids.play_btn.state == 'down':

            node = queue.pop(0)  # Dequeue a vertex from queue and color it
            print(node.Id, end=" ")
            node.background_color = globals.colors['green']
           # globals.graph_manager.update_canvas()

            for n in node.neighbors:  # Get all adjacent vertices of the dequeued vertex node. If a adjacent has not
                if visited[globals.graph_manager.getIndexFromListOfNodes(n)] == False:  # been visited, then mark it visited and enqueue it
                    queue.append(n)
                    visited[globals.graph_manager.getIndexFromListOfNodes(n)] = True
        else:
            self.visited = visited
            self.queue = queue
            Clock.unschedule(self.BFSUtil)


    def start(self):
        source = globals.main_view_widget.ids.bfs_txt_input.text
        isOk = True

        if globals.main_view_widget.ids.play_btn.visible == True:

            try:
                if source == "":
                    globals.error_popup_widget = popup_widget.ErrorPopupWidget()
                    globals.error_popup_widget.setText("You must enter the starting node first!")
                    globals.popup_window = Popup(title="Error", content=globals.error_popup_widget, size_hint=(None, None),
                                                 size=(400, 200), auto_dismiss=False)
                    globals.popup_window.open()
                    globals.error_popup_widget.ids.error_popup_btn.bind(on_press=popup_widget.ErrorPopupWidget.closePopUp)
                    isOk = False

                else:
                    source = int(source)
                    source = globals.graph_manager.getNodeWidgetById(source)
                    if source == None:
                        raise GraphException("The starting node does not exist")
            except:
                raise GraphException("Invalid number for the starting node")

            if isOk == True and self.isFirstTime:
                self.visited = [False] * (len(globals.graph_manager.node_widgets))  # Mark all the vertices as not visited
                self.queue = []  # Create a queue for BFS
                self.queue.append(source)  # Mark the source node as visited and enqueue it

                self.visited[globals.graph_manager.getIndexFromListOfNodes(source)] = True
                Clock.schedule_interval(partial(self.BFSUtil, self.queue, self.visited), 1)
                self.isFirstTime = False
            elif isOk == True:
                Clock.schedule_interval(partial(self.BFSUtil, self.queue, self.visited), 1)



    def DFSUtil(self, v, visited):

        visited[self.getIndexFromListOfNodes(v)] = True  # Mark the current node as visited and color it
        print(v.Id, end=' ')
        v.backgroundColor = [1, 0, 0, 1]

        for i in v.neibors:  # Recur for all the vertices adjacent to this vertex
            if visited[self.getIndexFromListOfNodes(i)] == False:
                self.DFSUtil(i, visited)

                # The function to do DFS traversal. It uses

    # recursive DFSUtil()

    def DFS(self, startNode):

        try:
            startNode = int(startNode)
            startNode = self.getNodeWidgetById(startNode)
            if startNode == None:
                raise GraphException("The starting node does not exist")
        except:
            raise GraphException("Invalid number for the starting node")

        visited = [False] * (len(self.node_widgets))  # Mark all the vertices as not visited

        self.DFSUtil(startNode, visited)  # Call the recursive helper function to print DFS traversal

    def dijkstra(self, src):

        dist = [sys.maxint] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices of the picked vertex only if the current
            # distance is greater than new distance and the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                        sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist) 
        
        
        
