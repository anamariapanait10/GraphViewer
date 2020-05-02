#import kivy
from kivy.config import Config

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '620')

Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'minimum_width', '800')
Config.set('graphics', 'minimum_height', '620')

from kivy.app import App
from graph.graph_manager import GraphManager
from graph.force_layout import *
from gui.buttons_behavior import *
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.factory import Factory
from datetime import datetime
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from gui import screen_manager

#kivy.require('2.0.0')

def millis():
    return datetime.now().microsecond / 1000

lastInputText = ""

def isOnNode(touch):
    for nodeWidget in globals.graph_manager.node_widgets:
        x2 = nodeWidget.pos[0] + globals.node_radius + globals.main_view_widget.ids.graph_canvas.pos[0]
        y2 = nodeWidget.pos[1] + globals.node_radius + globals.main_view_widget.ids.graph_canvas.pos[1]
        dist = sqrt((x2 - touch.pos[0]) ** 2 + (y2 - touch.pos[1]) ** 2)
        if dist <= globals.node_radius:
            return nodeWidget

    return None

class MainViewWidget(Widget):

    grabbedNode = None
    lastSelectedNode = None
    isSelectedANode = False
    ismoved = False

    def on_touch_down(self, touch):
        if self.ids.graph_canvas.collide_point(*touch.pos):
            print("Touch down")

            self.ismoved = False
            self.grabbedNode = isOnNode(touch)
            if self.grabbedNode != None:
                self.isSelectedANode = True
                touch.grab(self)
                if self.lastSelectedNode != None and self.grabbedNode != None and self.lastSelectedNode != self.grabbedNode:
                    globals.graph_manager.addEdgeWidget(self.lastSelectedNode.Id, self.grabbedNode.Id)
                    self.lastSelectedNode.border_width = 5
                    self.lastSelectedNode = None
                    globals.graph_manager.update_text_on_edgeAdd()

                    self.isSelectedANode = False
                    self.grabbedNode = None
                    touch.ungrab(self)

                    print("Add edge")


                elif self.lastSelectedNode == None:
                    self.lastSelectedNode = self.grabbedNode
                    self.lastSelectedNode.border_width = 10


            elif self.lastSelectedNode != None:
                self.lastSelectedNode.border_width = 5
                self.lastSelectedNode = None

            return True

        else:
            return super().on_touch_down(touch)



    def on_touch_move(self, touch):
        if self.ids.graph_canvas.collide_point(*touch.pos) and touch.grab_current is self:

            self.ismoved = True

            self.grabbedNode.pos = [touch.pos[0] - globals.node_radius - globals.main_view_widget.ids.graph_canvas.pos[0],
                                    touch.pos[1] - globals.node_radius - globals.main_view_widget.ids.graph_canvas.pos[1]]


            if globals.forces == True:
                recalculatePositions(gn=self.grabbedNode.Id)
            else:
                for edge in globals.graph_manager.edge_widgets:
                    edge.updateCoords()

    def on_touch_up(self, touch):
        if self.ids.graph_canvas.collide_point(*touch.pos):
            print("Touch Up")

            if self.ismoved == True and self.grabbedNode != None:
                self.grabbedNode.border_width = 5
                self.grabbedNode = None
                self.lastSelectedNode = None
                self.isSelectedANode = False
                self.ismoved = False
                touch.ungrab(self)
                if globals.forces== True:
                    recalculatePositions()
            elif not(touch.grab_current is self.grabbedNode and self.grabbedNode is not None):
                if touch.is_double_tap:
                    if touch.grab_current != None:
                        touch.ungrab(touch.grab_current)
                    self.on_double_press(touch)
                else:
                    node = isOnNode(touch)
                    if node is None and self.isSelectedANode == False:
                        self.on_single_press(touch)
                    elif node is None:
                        self.isSelectedANode = False

            # print("Selected: " + str(self.isSelectedANode))
            return True

        else:
            return super().on_touch_up(touch)


    def on_double_press(self, touch):
        nodeToBeDeletedFromText = globals.graph_manager.deleteNodeWidgetByCoords(touch.pos[0], touch.pos[1])
        globals.graph_manager.deleteEdgeWidgetByCoords(touch.pos[0], touch.pos[1])
        globals.graph_manager.update_text_on_delete(globals.main_view_widget.ids.input_text.text, nodeToBeDeletedFromText)
        self.lastSelectedNode = None
        self.isSelectedANode = False
        self.grabbedNode = None
        print("Double press")

    def on_single_press(self, touch):

        print("Single press")
        nx = touch.pos[0] - self.ids.graph_canvas.pos[0] - globals.node_radius
        ny = touch.pos[1] - self.ids.graph_canvas.pos[1] - globals.node_radius

        # print("nx =" + str(nx) + " ny = " + str(ny))

        if nx < 9:
            nx = 9

        if ny < 8:
            ny = 8

        if nx > self.ids.graph_canvas.size[0] - 55:
            nx = self.ids.graph_canvas.size[0] - 55

        if ny > self.ids.graph_canvas.size[1] - 55:
            ny = self.ids.graph_canvas.size[1] - 55


        n = globals.graph_manager.addNodeWidget(node_widget.getnextid(), [nx, ny])

        text = self.ids.input_text.text
        length = len(text)
        if text != "" and text[length - 1] == '\n':
            while text[length - 1] == '\n':
                text = text[:length - 1]
                length -= 1
            self.ids.input_text.text = text + "\n" + str(n.Id)
        else:
            if text == "":
                self.ids.input_text.text = str(n.Id)
            else:
                self.ids.input_text.text += "\n" + str(n.Id)


        if globals.forces == True:
            recalculatePositions()

    def keyIsEnter(self, text):
        if text[len(text)-1] == '\n':   # Trebuie adaugat si spatiile/enterurile de la mijolc
            return True
        return False

    def text_event(self, event, text):
        if text != "":
            global lastInputText

           # globals.main_view_widget.ids.input_text._lines_labels[0].background_color = [1, 0, 0, 1]

            max_length = self.getTextWidth()
            globals.main_view_widget.ids.input_text.width = max_length

           # if self.keyIsEnter(text) == True or len(lastInputText) > len(text):
               # self.ids.graph_canvas.clear_widgets()
            globals.graph_manager.parse_graph_data(data=text)
            if globals.forces == True:
                recalculatePositions()

            lastInputText = text

    def getTextWidth(self):

        max_length = globals.main_view_widget.ids.scroller.width

        for line in globals.main_view_widget.ids.input_text._lines_labels:
            max_length = max(max_length, line.width + 20)

        return max_length



class LabelB(Label):
    background_color = ListProperty(globals.colors['white'])


class GraphViewerApp(App):
    def build(self):

        Config.set('input', 'mouse', 'mouse,multitouch_on_demand') # disable multi-touch emulation

        self.icon = '../GraphViewer/images/Icon.png'    # set the app icon

        globals.main_view_widget = MainViewWidget()
        globals.graph_manager = GraphManager(False)
        globals.main_view_widget.ids.input_text.bind(text=globals.main_view_widget.text_event)

        dropdown = AlgDropDownList()
        globals.main_view_widget.ids.algorithm_btn.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(globals.main_view_widget.ids.algorithm_btn, 'Algorithms', x))

        globals.algorithms_drop_down_list = dropdown
        globals.algorithms_drop_down_list.ids.bfs_btn.bind(on_press=BfsButton.on_press)
        globals.algorithms_drop_down_list.ids.dfs_btn.bind(on_press=DfsButton.on_press)
        globals.algorithms_drop_down_list.ids.dijkstra_btn.bind(on_press=DijkstraButton.on_press)

        dropdown = InputDropDownList()
        globals.main_view_widget.ids.input_btn.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(globals.main_view_widget.ids.input_btn, 'Input', x))

        globals.input_drop_down_list = dropdown
        globals.input_drop_down_list.ids.listOfEdges_btn.bind(on_press=ListOfEdgesButton.on_press)
        globals.input_drop_down_list.ids.adjacencyList_btn.bind(on_press=AdjacencyListButton.on_press)
        globals.input_drop_down_list.ids.adjacencyMatrix_btn.bind(on_press=AdjacencyMatrixButton.on_press)
        globals.input_drop_down_list.ids.costMatrix_btn.bind(on_press=CostMatrixButton.on_press)

        globals.main_view_widget.ids.undirected_btn.bind(on_press=UndirectedButton.on_press)
        globals.main_view_widget.ids.directed_btn.bind(on_press=DirectedButton.on_press)

        globals.main_view_widget.ids.draw_lbl.multiline = True

        globals.main_view_widget.ids.settings_btn.bind(on_release=SettingsButton.on_release)

        globals.NodeWidgetBackgroundColor = globals.colors['white'] # it used to be [0.9, 0.9, 0.9, 1]
        globals.NodeWidgetColor = globals.colors['black'] # it used to be [0, 0, 0, 1]
        globals.EdgeWidgetColor = globals.colors['black'] # it used to be [0, 0, 0, 1]

        globals.main_view_widget.ids.switch.bind(active=callback)

        Factory.register('KivyB', module='LabelB')

        globals.main_screen = screen_manager.MainScreen()
        globals.main_screen.add_widget(globals.main_view_widget)
        globals.theory_screen = screen_manager.TheoryScreen()
        globals.screen_manager = screen_manager.ScreenManager(transition=FadeTransition(duration=.05))
        globals.screen_manager.add_widget(globals.main_screen)
        globals.screen_manager.add_widget(globals.theory_screen)

        with open("../GraphViewer/theory/chapter1.txt", encoding='utf-8') as f:
            content = f.read()
            globals.theory_screen.ids.theory_lbl.text = content

        return globals.screen_manager
        # return globals.main_view_widget

