#import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from gui.graph_manager import GraphManager
from gui.force_layout import *
from gui import node_widget
from gui.buttons_behavior import *
from kivy.config import Config
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.factory import Factory



#kivy.require('2.0.0')


lastInputText = ""

class MainViewWidget(Widget):

    def on_touch_up(self, touch):
        if self.ids.graph_canvas.collide_point(*touch.pos):
            if touch.is_double_tap:
                globals.graphManager.deleteNodeWidget(touch.pos[0], touch.pos[1])
                globals.graphManager.deleteEdgeWidget(touch.pos[0], touch.pos[1])
            else:
                nx = touch.pos[0] - self.ids.graph_canvas.pos[0] - 25
                ny = touch.pos[1] -  self.ids.graph_canvas.pos[1] - 25

                # print("nx =" + str(nx) + " ny = " + str(ny))

                if nx < 9:
                    nx = 9

                if ny < 8:
                    ny = 8

                if nx > self.ids.graph_canvas.size[0] - 55:
                    nx = self.ids.graph_canvas.size[0] - 55

                if ny > self.ids.graph_canvas.size[1] - 55:
                    ny = self.ids.graph_canvas.size[1] - 55

                n = node_widget.NodeWidget(node_widget.getnextid(), [nx, ny])
                self.ids.graph_canvas.add_widget(n)

                text = self.ids.input_nodes.text
                length = len(text)
                if text != "" and text[length - 1] == '\n':
                    while text[length - 1] == '\n':
                        text = text[:length-1]
                        length -= 1
                    self.ids.input_nodes.text = text + "\n" + str(n.nr)
                else:
                    if text == "":
                        self.ids.input_nodes.text = str(n.nr)
                    else:
                        self.ids.input_nodes.text += "\n" + str(n.nr)

                globals.graphManager.addNodeFromDrawing(n)
                return True
        else:
            return super().on_touch_up(touch)

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
              #  recalculatePositions()

                lastInputText = text


class LabelB(Label):
  bcolor = ListProperty([1,1,1,1])


class GraphViewerApp(App):
    def build(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand') # disable multi-touch emulation

        self.icon = '../GraphViewer/images/Sigla.png'    # set the app icon

        globals.mainViewWidget = MainViewWidget()
        globals.graphManager = GraphManager(False, globals.mainViewWidget)
        globals.mainViewWidget.ids.input_nodes.bind(text=globals.mainViewWidget.text_event)

        dropdown = AlgDropDownList()
        globals.mainViewWidget.ids.algorithm_btn.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(globals.mainViewWidget.ids.algorithm_btn, 'Algorithms', x))

        globals.algDropDownList = dropdown
        globals.algDropDownList.ids.bfs_btn.bind(on_press=BfsButton.on_press)
        globals.algDropDownList.ids.dfs_btn.bind(on_press=DfsButton.on_press)
        globals.algDropDownList.ids.dijkstra_btn.bind(on_press=DijkstraButton.on_press)

        dropdown = InputDropDownList()
        globals.mainViewWidget.ids.input_btn.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(globals.mainViewWidget.ids.input_btn, 'Input', x))

        globals.inputDropDownList = dropdown
        globals.inputDropDownList.ids.listOfEdges_btn.bind(on_press=ListOfEdgesButton.on_press)
        globals.inputDropDownList.ids.adjacencyList_btn.bind(on_press=AdjacencyListButton.on_press)
        globals.inputDropDownList.ids.adjacencyMatrix_btn.bind(on_press=AdjacencyMatrixButton.on_press)
        globals.inputDropDownList.ids.costMatrix_btn.bind(on_press=CostMatrixButton.on_press)

        globals.mainViewWidget.ids.undirected_btn.bind(on_press=UndirectedButton.on_press)
        globals.mainViewWidget.ids.directed_btn.bind(on_press=DirectedButton.on_press)

        globals.mainViewWidget.ids.draw_lbl.multiline = True

        globals.mainViewWidget.ids.settings_btn.bind(on_release=SettingsButton.on_release)

        globals.NodeWidgetBackgroundColor = [0.9, 0.9, 0.9, 1]
        globals.NodeWidgetColor = [0, 0, 0, 1]
        globals.EdgeWidgetColor = [0, 0, 0, 1]

        Factory.register('KivyB', module='LabelB')

        return globals.mainViewWidget

