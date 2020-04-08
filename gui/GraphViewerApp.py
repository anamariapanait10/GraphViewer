import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from gui.graph_manager import GraphManager
from math import sqrt, log

from gui import node_widget

kivy.require('2.0.0')


lastInputText = ""

mainViewWidget = None
graphManager = None

c1 = 2
c2 = 1
c3 = 1
c4 = 0.1
M = 100

def dist(v, u):
    return sqrt(((v.pos[0] - u.pos[0]) ** 2) + ((v.pos[1] - u.pos[1]) ** 2))


def __calculateForces():
    # for v in graphManager.nodeWidgets:
    nodeWidgets = graphManager.getNodeWidgetList()
    for v in nodeWidgets:
        fx = 0
        fy = 0
        # for u in graphManager.nodeWidgets:
        for u in nodeWidgets:
            if v != u:
                fx += c3 / ((v.pos[0] - u.pos[0]) ** 2)
                fx += c1 * log((v.pos[0] - u.pos[0]) / c2)
                fy += c3 / ((v.pos[1] - u.pos[1]) ** 2)
                fy += c1 * log((v.pos[1] - u.pos[1]) / c2)

        v.force = (fx, fy)


def __moveNodes():
    # for v in graphManager.nodeWidgets:
    nodeWidgets = GraphManager.getNodeWidgetList()
    for v in nodeWidgets:
        v.pos[0] = v.pos[0] + c4 * v.force[0]
        v.pos[1] = v.pos[1] + c4 * v.force[1]


def __update():
    __calculateForces()
    __moveNodes()


def recalculatePositions():
    for t in range(M):
        __update()



class MainViewWidget(Widget):
    def on_touch_down(self, touch):
        if self.ids.graph_canvas.collide_point(*touch.pos):
            #node_widget.maxid += 1
            nx = touch.pos[0] - self.ids.graph_canvas.pos[0] - 25
            ny = touch.pos[1] - self.ids.graph_canvas.pos[1] - 25

            if nx < 30:
                nx = 30

            if ny < 30:
                ny = 30

            if nx > self.ids.graph_canvas.size[0] - 30:
                nx = self.ids.graph_canvas.size[0] - 30

            if ny > self.ids.graph_canvas.size[1] - 30:
                ny = self.ids.graph_canvas.size[1] - 30

            n = node_widget.NodeWidget(node_widget.getmaxid(), [nx, ny])
            self.ids.graph_canvas.add_widget(n)
            graphManager.addNodeFromDrawing(n)
            return True
        else:
            return super().on_touch_down(touch)

    def keyIsEnter(self, text):
        if text[len(text)-1] == '\n':   # Trebuie adaugat si spatiile/enterurile de la mijolc
            return True
        return False

    def text_event(self, event, text):
        if text != "":
            global lastInputText
            if self.keyIsEnter(text) == True or len(lastInputText) > len(text):
                self.ids.graph_canvas.clear_widgets()
                graphManager.parse_graph_data(text)
                recalculatePositions()
                lastInputText = text


class GraphViewerApp(App):
    def build(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand') # disable multi-touch emulation
        global mainViewWidget
        mainViewWidget = MainViewWidget()
        global graphManager
        graphManager = GraphManager(False, mainViewWidget)

        mainViewWidget.ids.input_nodes.bind(text=mainViewWidget.text_event)

        return mainViewWidget

