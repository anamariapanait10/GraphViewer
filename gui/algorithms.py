from heapq import *
import sys
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
                n.neighbors.sort(key=lambda node: node.Id)
                if visited[globals.graph_manager.getIndexFromListOfNodes(n)] == False:  # been visited, then mark it visited and enqueue it
                    queue.append(n)
                    visited[globals.graph_manager.getIndexFromListOfNodes(n)] = True
        else:
            self.visited = visited
            self.queue = queue
            Clock.unschedule(self.BFSUtil)


    def start(self):
        source = globals.main_view_widget.ids.algorithm_txt_input.text
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

class DFS:

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

        source = globals.main_view_widget.ids.algorithm_txt_input.text
        isOk = True

        if globals.main_view_widget.ids.play_btn.visible == True:

            try:
                if source == "":
                    globals.error_popup_widget = popup_widget.ErrorPopupWidget()
                    globals.error_popup_widget.setText("You must enter the starting node first!")
                    globals.popup_window = Popup(title="Error", content=globals.error_popup_widget,
                                                 size_hint=(None, None),
                                                 size=(400, 200), auto_dismiss=False)
                    globals.popup_window.open()
                    globals.error_popup_widget.ids.error_popup_btn.bind(
                        on_press=popup_widget.ErrorPopupWidget.closePopUp)
                    isOk = False

                else:
                    source = int(source)
                    source = globals.graph_manager.getNodeWidgetById(source)
                    if source == None:
                        raise GraphException("The starting node does not exist")
            except:
                raise GraphException("Invalid number for the starting node")

            if isOk == True and self.isFirstTime:
                self.visited = [False] * (
                    len(globals.graph_manager.node_widgets))  # Mark all the vertices as not visited
                self.queue = []  # Create a queue for BFS
                self.queue.append(source)  # Mark the source node as visited and enqueue it

                self.visited[globals.graph_manager.getIndexFromListOfNodes(source)] = True
                Clock.schedule_interval(partial(self.BFSUtil, self.queue, self.visited), 1)
                self.isFirstTime = False
            elif isOk == True:
                Clock.schedule_interval(partial(self.BFSUtil, self.queue, self.visited), 1)

        try:
            startNode = int(startNode)
            startNode = self.getNodeWidgetById(startNode)
            if startNode == None:
                raise GraphException("The starting node does not exist")
        except:
            raise GraphException("Invalid number for the starting node")

        visited = [False] * (len(self.node_widgets))  # Mark all the vertices as not visited

        self.DFSUtil(startNode, visited)  # Call the recursive helper function to print DFS traversal


class Dijkstra:

    def dijkstra_util(self, dummy):
        if len(self.heap) > 0:
            tmp = heappop(self.heap)
            u = tmp[1]
            u_widget = globals.graph_manager.getNodeWidgetById(u)

            for current_edge in globals.graph_manager.edge_widgets:
                if current_edge.node1.Id == u:
                    vc = current_edge.node2.Id
                    vc_widget = globals.graph_manager.getNodeWidgetById(vc)
                    vc_index = globals.graph_manager.getIndexFromListOfNodes(vc_widget)
                    dist = current_edge.cost
                    if self.d[globals.graph_manager.getIndexFromListOfNodes(u_widget)] + dist < self.d[vc_index]:
                        if self.d[vc] != self.inf:
                            for p in self.heap[:]:
                                if p == (self.d[vc], vc):
                                    self.heap.remove(p)

                        self.d[vc] = self.d[u] + dist
                        heappush(self.heap, (self.d[vc], vc))
        else:
            Clock.unschedule(self.dijkstra_util)
            print(self.d)


    def dijkstra(self, src):
        self.inf = sys.maxsize
        self.d = [self.inf] * len(globals.graph_manager.node_widgets)
        self.d[src] = 0
        self.number_of_neighbors = len(globals.graph_manager.getNodeWidgetById(src).neighbors)
        self.heap = [(0, src)]
        heapify(self.heap)
        Clock.schedule_interval(self.dijkstra_util, 0.1)

    def start(self):
        self.sn = 1
        try:
            self.sn = int(globals.main_view_widget.ids.algorithm_txt_input.text)
        except:
            raise GraphException('The starting node must be a valid node')

        self.dijkstra(self.sn)