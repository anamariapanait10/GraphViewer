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
        if len(queue) != 0 and globals.mainViewWidget.ids.play_btn.state == 'down':

            node = queue.pop(0)  # Dequeue a vertex from queue and color it
            print(node.Id, end=" ")
            node.backgroundColor = globals.colors['green']
            globals.graphManager.update_canvas()

            for n in node.neighbors:  # Get all adjacent vertices of the dequeued vertex node. If a adjacent has not
                if visited[globals.graphManager.getIndexFromListOfNodes(n)] == False:  # been visited, then mark it visited and enqueue it
                    queue.append(n)
                    visited[globals.graphManager.getIndexFromListOfNodes(n)] = True
        else:
            self.visited = visited
            self.queue = queue
            Clock.unschedule(self.BFSUtil)


    def start(self):
        source = globals.mainViewWidget.ids.bfs_txt_input.text
        isOk = True

        try:
            if source == "":
                globals.errorPopupWidget = popup_widget.ErrorPopupWidget()
                globals.errorPopupWidget.setText("You must enter the starting node first!")
                globals.popupWindow = Popup(title="Error", content=globals.errorPopupWidget, size_hint=(None, None),
                                            size=(400, 200), auto_dismiss=False)
                globals.popupWindow.open()
                globals.errorPopupWidget.ids.error_popup_btn.bind(on_press=popup_widget.ErrorPopupWidget.closePopUp)
                isOk = False

            else:
                source = int(source)
                source = globals.graphManager.getNodeWidgetById(source)
                if source == None:
                    raise GraphException("The starting node does not exist")
        except:
            raise GraphException("Invalid number for the starting node")

        if isOk == True and self.isFirstTime:
            self.visited = [False] * (len(globals.graphManager.nodeWidgets))  # Mark all the vertices as not visited
            self.queue = []  # Create a queue for BFS
            self.queue.append(source)  # Mark the source node as visited and enqueue it

            self.visited[globals.graphManager.getIndexFromListOfNodes(source)] = True
            Clock.schedule_interval(partial(self.BFSUtil, self.queue, self.visited), 1)
            self.isFirstTime = False
        elif isOk == True:
            Clock.schedule_interval(partial(self.BFSUtil, self.queue, self.visited), 1)