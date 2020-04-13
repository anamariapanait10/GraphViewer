#import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from gui import globals
from gui.graph_manager import GraphManager
from math import sqrt, log
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior

from gui import node_widget

#kivy.require('2.0.0')


lastInputText = ""

mainViewWidget = None


c1 = 2
c2 = 1
c3 = 1
c4 = 0.1
M = 100

def dist(v, u):
    return sqrt(((v.pos[0] - u.pos[0]) ** 2) + ((v.pos[1] - u.pos[1]) ** 2))


def __calculateForces():
    # for v in graphManager.nodeWidgets:
    nodeWidgets = globals.graphManager.getNodeWidgetList()
    for v in nodeWidgets:
        fx = 0
        fy = 0
        # for u in graphManager.nodeWidgets:
        for u in nodeWidgets:
            if v != u:
                fx += c3 / ((v.pos[0] - u.pos[0]) ** 2)
                fx += c1 * log(abs((v.pos[0] - u.pos[0]) / c2))
                fy += c3 / ((v.pos[1] - u.pos[1]) ** 2)
                fy += c1 * log(abs((v.pos[1] - u.pos[1]) / c2))

        v.force = (fx, fy)


def __moveNodes():
    # for v in graphManager.nodeWidgets:
    nodeWidgets = globals.graphManager.getNodeWidgetList()
    for v in nodeWidgets:
        v.pos[0] = v.pos[0] + c4 * v.force[0]
        v.pos[1] = v.pos[1] + c4 * v.force[1]


def __update():
    __calculateForces()
    __moveNodes()


def recalculatePositions():
    for t in range(M):
        __update()


class AlgDropDownList(DropDown):
    pass

class InputDropDownList(DropDown):
    pass


class ListOfEdgesButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(ListOfEdgesButton, self).__init__(**kwargs)

    def on_press(self):
        if mainViewWidget.ids.listOfEdges_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            mainViewWidget.ids.listOfEdges_btn.background_normal: ''
            mainViewWidget.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            mainViewWidget.ids.adjancyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            mainViewWidget.ids.adjancyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)
            mainViewWidget.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

        """
        else:   # if it is pressed
            mainViewWidget.ids.listOfEdges_btn.background_normal: ''
            mainViewWidget.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            mainViewWidget.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)
        """


class AdjancyListButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(AdjancyListButton, self).__init__(**kwargs)

    def on_press(self):
        if mainViewWidget.ids.adjancyList_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            mainViewWidget.ids.adjancyList_btn.background_normal: ''
            mainViewWidget.ids.adjancyList_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            mainViewWidget.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            mainViewWidget.ids.adjancyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)
            mainViewWidget.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)


        else:   # if it is pressed
            mainViewWidget.ids.adjancyList_btn.background_normal: ''
            mainViewWidget.ids.adjancyList_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            mainViewWidget.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)

class AdjancyMatrixButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(AdjancyMatrixButton, self).__init__(**kwargs)

    def on_press(self):
        if mainViewWidget.ids.adjancyMatrix_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            mainViewWidget.ids.adjancyMatrix_btn.background_normal: ''
            mainViewWidget.ids.adjancyMatrix_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            mainViewWidget.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            mainViewWidget.ids.adjancyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            mainViewWidget.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)


        else:   # if it is pressed
            mainViewWidget.ids.adjancyMatrix_btn.background_normal: ''
            mainViewWidget.ids.adjancyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            mainViewWidget.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)

class CostMatrixButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(CostMatrixButton, self).__init__(**kwargs)

    def on_press(self):
        if mainViewWidget.ids.costMatrix_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            mainViewWidget.ids.costMatrix_btn.background_normal: ''
            mainViewWidget.ids.costMatrix_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            mainViewWidget.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            mainViewWidget.ids.adjancyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            mainViewWidget.ids.adjancyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)


        else:   # if it is pressed
            mainViewWidget.ids.costMatrix_btn.background_normal: ''
            mainViewWidget.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            mainViewWidget.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)

class UndirectedButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(UndirectedButton, self).__init__(**kwargs)

    def on_press(self):
        if mainViewWidget.ids.undirected_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            # print(mainViewWidget.ids.undirected_btn.background_normal)
            mainViewWidget.ids.undirected_btn.background_normal: ''
            mainViewWidget.ids.undirected_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graphManager.setisDirected(False)

            # The directed and undirected buttons can't be pressed at the same time
            mainViewWidget.ids.directed_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:   # if it is pressed
            mainViewWidget.ids.undirected_btn.background_normal: ''
            mainViewWidget.ids.undirected_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The directed and undirected buttons can't be unpressed at the same time
            mainViewWidget.ids.directed_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graphManager.setisDirected(True)

        globals.graphManager.parse_graph_data(mainViewWidget.ids.input_nodes.text)
        globals.graphManager.update_canvas()


class DirectedButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(DirectedButton, self).__init__(**kwargs)

    def on_press(self):
        if mainViewWidget.ids.directed_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            #print(mainViewWidget.ids.directed_btn.background_normal)
            mainViewWidget.ids.directed_btn.background_normal: ''
            mainViewWidget.ids.directed_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graphManager.setisDirected(True)

            # The directed and undirected buttons can't be pressed at the same time
            mainViewWidget.ids.undirected_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:   # if it is pressed
            mainViewWidget.ids.directed_btn.background_normal: ''
            mainViewWidget.ids.directed_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The directed and undirected buttons can't be unpressed at the same time
            mainViewWidget.ids.undirected_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graphManager.setisDirected(False)

        globals.graphManager.parse_graph_data(mainViewWidget.ids.input_nodes.text)
        globals.graphManager.update_canvas()



class MainViewWidget(Widget):
    def on_touch_down(self, touch):
        if self.ids.graph_canvas.collide_point(*touch.pos):
            #node_widget.maxid += 1
            nx = touch.pos[0] - self.ids.graph_canvas.pos[0] - 25
            ny = touch.pos[1] - self.ids.graph_canvas.pos[1] - 25

            if nx < 10:
                nx = 10

            if ny < 10:
                ny = 10

            if nx > self.ids.graph_canvas.size[0] - 30:
                nx = self.ids.graph_canvas.size[0] - 30

            if ny > self.ids.graph_canvas.size[1] - 30:
                ny = self.ids.graph_canvas.size[1] - 30

            n = node_widget.NodeWidget(node_widget.getnextid(), [nx, ny])
            self.ids.graph_canvas.add_widget(n)
            if self.ids.input_nodes.text != "" and self.ids.input_nodes.text[len(self.ids.input_nodes.text) - 1] == '\n':
                self.ids.input_nodes.text += str(n.nr)
            else:
                self.ids.input_nodes.text += "\n" + str(n.nr)
            globals.graphManager.addNodeFromDrawing(n)
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
                globals.graphManager.parse_graph_data(text)
                #recalculatePositions()
                lastInputText = text


class GraphViewerApp(App):
    def build(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand') # disable multi-touch emulation

        global mainViewWidget
        mainViewWidget = MainViewWidget()

        globals.graphManager = GraphManager(False, mainViewWidget)

        mainViewWidget.ids.input_nodes.bind(text=mainViewWidget.text_event)

        dropdown = AlgDropDownList()
        mainViewWidget.ids.algorithm_btn.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainViewWidget.ids.algorithm_btn, 'Algorithms', x))

        dropdown = InputDropDownList()
        mainViewWidget.ids.input_btn.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainViewWidget.ids.input_btn, 'Input', x))

        mainViewWidget.ids.undirected_btn.bind(on_press=UndirectedButton.on_press)
        mainViewWidget.ids.directed_btn.bind(on_press=DirectedButton.on_press)
        # mainViewWidget.ids.listOfEdges_btn.bind(on_press=ListOfEdgesButton.on_press)
        # mainViewWidget.ids.adjancyList_btn.bind(on_press=AdjancyListButton.on_press)
        # mainViewWidget.ids.adjancyMatrix_btn.bind(on_press=AdjancyMatrixButton.on_press)
        # mainViewWidget.ids.costMatrix_btn.bind(on_press=CostMatrixButton.on_press)

        mainViewWidget.ids.draw_lbl.multiline = True

        return mainViewWidget

