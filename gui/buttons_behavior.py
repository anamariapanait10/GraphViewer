from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from globals import globals
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.vector import Vector
from graph import node_widget
from graph import edge_widget
from gui import popup_widget
from graph import force_layout
from gui import algorithms


class CircularButton(ToggleButtonBehavior, Widget):
    def collide_point(self, x, y):
        return Vector(x, y).distance(self.center) <= self.width / 2

    def on_press(self):
        algorithms.BFS().start()

class SettingsButton(ButtonBehavior):

    def on_release(self):
        globals.popupWidget = popup_widget.PopupWidget()
        globals.popupWindow = Popup(title="Settings", content=globals.popupWidget, size_hint=(None, None), size=(450, 425), auto_dismiss=False)
        globals.popupWindow.open()

        dropdown1 = ChangeColorDropDownList()
        globals.popupWidget.ids.changeColor_btn1.bind(on_release=dropdown1.open)
        globals.changeColorDropDownList = dropdown1
        globals.changeColorDropDownList.ids.white_btn.bind(on_press=WhiteButton.dropdown1)
        globals.changeColorDropDownList.ids.white_btn.bind(on_release=dropdown1.dismiss)
        globals.changeColorDropDownList.ids.black_btn.bind(on_press=BlackButton.dropdown1)
        globals.changeColorDropDownList.ids.black_btn.bind(on_release=dropdown1.dismiss)
        globals.changeColorDropDownList.ids.red_btn.bind(on_press=RedButton.dropdown1)
        globals.changeColorDropDownList.ids.red_btn.bind(on_release=dropdown1.dismiss)
        globals.changeColorDropDownList.ids.yellow_btn.bind(on_press=YellowButton.dropdown1)
        globals.changeColorDropDownList.ids.yellow_btn.bind(on_release=dropdown1.dismiss)
        globals.changeColorDropDownList.ids.orange_btn.bind(on_press=OrangeButton.dropdown1)
        globals.changeColorDropDownList.ids.orange_btn.bind(on_release=dropdown1.dismiss)
        globals.changeColorDropDownList.ids.blue_btn.bind(on_press=BlueButton.dropdown1)
        globals.changeColorDropDownList.ids.blue_btn.bind(on_release=dropdown1.dismiss)
        globals.changeColorDropDownList.ids.purple_btn.bind(on_press=PurpleButton.dropdown1)
        globals.changeColorDropDownList.ids.purple_btn.bind(on_release=dropdown1.dismiss)
        globals.changeColorDropDownList.ids.green_btn.bind(on_press=GreenButton.dropdown1)
        globals.changeColorDropDownList.ids.green_btn.bind(on_release=dropdown1.dismiss)
        globals.changeColorDropDownList.ids.pink_btn.bind(on_press=PinkButton.dropdown1)
        globals.changeColorDropDownList.ids.pink_btn.bind(on_release=dropdown1.dismiss)

        dropdown2 = ChangeColorDropDownList()
        globals.popupWidget.ids.changeColor_btn2.bind(on_release=dropdown2.open)
        globals.changeColorDropDownList = dropdown2
        globals.changeColorDropDownList.ids.white_btn.bind(on_press=WhiteButton.dropdown2)
        globals.changeColorDropDownList.ids.white_btn.bind(on_release=dropdown2.dismiss)
        globals.changeColorDropDownList.ids.black_btn.bind(on_press=BlackButton.dropdown2)
        globals.changeColorDropDownList.ids.black_btn.bind(on_release=dropdown2.dismiss)
        globals.changeColorDropDownList.ids.red_btn.bind(on_press=RedButton.dropdown2)
        globals.changeColorDropDownList.ids.red_btn.bind(on_release=dropdown2.dismiss)
        globals.changeColorDropDownList.ids.yellow_btn.bind(on_press=YellowButton.dropdown2)
        globals.changeColorDropDownList.ids.yellow_btn.bind(on_release=dropdown2.dismiss)
        globals.changeColorDropDownList.ids.orange_btn.bind(on_press=OrangeButton.dropdown2)
        globals.changeColorDropDownList.ids.orange_btn.bind(on_release=dropdown2.dismiss)
        globals.changeColorDropDownList.ids.blue_btn.bind(on_press=BlueButton.dropdown2)
        globals.changeColorDropDownList.ids.blue_btn.bind(on_release=dropdown2.dismiss)
        globals.changeColorDropDownList.ids.purple_btn.bind(on_press=PurpleButton.dropdown2)
        globals.changeColorDropDownList.ids.purple_btn.bind(on_release=dropdown2.dismiss)
        globals.changeColorDropDownList.ids.green_btn.bind(on_press=GreenButton.dropdown2)
        globals.changeColorDropDownList.ids.green_btn.bind(on_release=dropdown2.dismiss)
        globals.changeColorDropDownList.ids.pink_btn.bind(on_press=PinkButton.dropdown2)
        globals.changeColorDropDownList.ids.pink_btn.bind(on_release=dropdown2.dismiss)
        dropdown2.dismiss()

        dropdown3 = ChangeColorDropDownList()
        globals.popupWidget.ids.changeColor_btn3.bind(on_release=dropdown3.open)
        globals.changeColorDropDownList = dropdown3
        globals.changeColorDropDownList.ids.white_btn.bind(on_press=WhiteButton.dropdown3)
        globals.changeColorDropDownList.ids.white_btn.bind(on_release=dropdown3.dismiss)
        globals.changeColorDropDownList.ids.black_btn.bind(on_press=BlackButton.dropdown3)
        globals.changeColorDropDownList.ids.black_btn.bind(on_release=dropdown3.dismiss)
        globals.changeColorDropDownList.ids.red_btn.bind(on_press=RedButton.dropdown3)
        globals.changeColorDropDownList.ids.red_btn.bind(on_release=dropdown3.dismiss)
        globals.changeColorDropDownList.ids.yellow_btn.bind(on_press=YellowButton.dropdown3)
        globals.changeColorDropDownList.ids.yellow_btn.bind(on_release=dropdown3.dismiss)
        globals.changeColorDropDownList.ids.orange_btn.bind(on_press=OrangeButton.dropdown3)
        globals.changeColorDropDownList.ids.orange_btn.bind(on_release=dropdown3.dismiss)
        globals.changeColorDropDownList.ids.blue_btn.bind(on_press=BlueButton.dropdown3)
        globals.changeColorDropDownList.ids.blue_btn.bind(on_release=dropdown3.dismiss)
        globals.changeColorDropDownList.ids.purple_btn.bind(on_press=PurpleButton.dropdown3)
        globals.changeColorDropDownList.ids.purple_btn.bind(on_release=dropdown3.dismiss)
        globals.changeColorDropDownList.ids.green_btn.bind(on_press=GreenButton.dropdown3)
        globals.changeColorDropDownList.ids.green_btn.bind(on_press=GreenButton.dropdown3)
        globals.changeColorDropDownList.ids.pink_btn.bind(on_press=PinkButton.dropdown3)
        globals.changeColorDropDownList.ids.pink_btn.bind(on_press=PinkButton.dropdown3)


        globals.popupWidget.ids.apply_btn.bind(on_press=globals.graphManager.parse_graph_data)

def callback(instance, value):
    if value == False:
        globals.forces = False
    else:
        globals.forces = True
        force_layout.recalculatePositions()

class saveBtn(ButtonBehavior):
    def on_press(self):
        globals.mainViewWidget.export_to_png()


class AlgDropDownList(DropDown):
    pass

class InputDropDownList(DropDown):
    pass

class ChangeColorDropDownList(DropDown):
    pass


class ListOfEdgesButton(ButtonBehavior):

    def on_press(self):
        if globals.inputDropDownList.ids.listOfEdges_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.inputDropDownList.ids.listOfEdges_btn.background_normal: ''
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.inputDropDownList.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            globals.listOfEdgesBtn = True
            globals.adjacencyListBtn = False
            globals.adjacencyMatrixBtn = False
            globals.costMatrixBtn = False
            globals.mainViewWidget.ids.input_nodes.hint_text = "node1Id  node2Id\nnode3Id  node4Id"


class AdjacencyListButton(ButtonBehavior):

    def on_press(self):
        if globals.inputDropDownList.ids.adjacencyList_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.inputDropDownList.ids.adjacencyList_btn.background_normal: ''
            globals.inputDropDownList.ids.adjacencyList_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            globals.listOfEdgesBtn = False
            globals.adjacencyListBtn = True
            globals.adjacencyMatrixBtn = False
            globals.costMatrixBtn = False
            globals.mainViewWidget.ids.input_nodes.hint_text = "node: neighbor1, neighbor2, ..."

        else:   # if it is pressed
            globals.inputDropDownList.ids.adjacencyList_btn.background_normal: ''
            globals.inputDropDownList.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


class AdjacencyMatrixButton(ButtonBehavior):

    def on_press(self):
        if globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_normal: ''
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            globals.listOfEdgesBtn = False
            globals.adjacencyListBtn = False
            globals.adjacencyMatrixBtn = True
            globals.costMatrixBtn = False
            globals.mainViewWidget.ids.input_nodes.hint_text = "0 1 1 0\n" \
                                                               "1 0 0 1\n" \
                                                               "0 1 0 1\n" \
                                                               "1 1 1 0"

        else:   # if it is pressed
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_normal: ''
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


class CostMatrixButton(ButtonBehavior):

    def on_press(self):
        if globals.inputDropDownList.ids.costMatrix_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.inputDropDownList.ids.costMatrix_btn.background_normal: ''
            globals.inputDropDownList.ids.costMatrix_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            globals.listOfEdgesBtn = False
            globals.adjacencyListBtn = False
            globals.adjacencyMatrixBtn = False
            globals.costMatrixBtn = True

            globals.mainViewWidget.ids.input_nodes.hint_text = "0 123 78 62\n" \
                                                               "13 0 6 198\n" \
                                                               "26 4 0 17\n" \
                                                               "65 143 31 0"

        else:   # if it is pressed
            globals.inputDropDownList.ids.costMatrix_btn.background_normal: ''
            globals.inputDropDownList.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


class UndirectedButton(ButtonBehavior):

    def on_press(self):
        if globals.mainViewWidget.ids.undirected_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.mainViewWidget.ids.undirected_btn.background_normal: ''
            globals.mainViewWidget.ids.undirected_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graphManager.setisDirected(False)

            # The directed and undirected buttons can't be pressed at the same time
            globals.mainViewWidget.ids.directed_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:   # if it is pressed
            globals.mainViewWidget.ids.undirected_btn.background_normal: ''
            globals.mainViewWidget.ids.undirected_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The directed and undirected buttons can't be unpressed at the same time
            globals.mainViewWidget.ids.directed_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graphManager.setisDirected(True)

        globals.graphManager.parse_graph_data(globals.mainViewWidget.ids.input_nodes.text)
        globals.graphManager.update_canvas()


class DirectedButton(ButtonBehavior):

    def on_press(self):
        if globals.mainViewWidget.ids.directed_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            #print(globals.mainViewWidget.ids.directed_btn.background_normal)
            globals.mainViewWidget.ids.directed_btn.background_normal: ''
            globals.mainViewWidget.ids.directed_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graphManager.setisDirected(True)

            # The directed and undirected buttons can't be pressed at the same time
            globals.mainViewWidget.ids.undirected_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:   # if it is pressed
            globals.mainViewWidget.ids.directed_btn.background_normal: ''
            globals.mainViewWidget.ids.directed_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The directed and undirected buttons can't be unpressed at the same time
            globals.mainViewWidget.ids.undirected_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graphManager.setisDirected(False)

        globals.graphManager.parse_graph_data(globals.mainViewWidget.ids.input_nodes.text)
        globals.graphManager.update_canvas()


class DijkstraButton(ButtonBehavior):

    def on_press(self):
        if globals.algDropDownList.ids.dijkstra_btn.background_color != [0.8, 0.8, 0.8, 1]:  # if is not pressed
            globals.algDropDownList.ids.dijkstra_btn.background_normal: ''
            globals.algDropDownList.ids.dijkstra_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The buttons from the dropdown list can't be pressed at the same time
            globals.algDropDownList.ids.bfs_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.algDropDownList.ids.dfs_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:  # if it is pressed
            globals.algDropDownList.ids.dijkstra_btn.background_normal: ''
            globals.algDropDownList.ids.dijkstra_btn.background_color = (0.34, 0.34, 0.34, 1)


class BfsButton(ButtonBehavior):

    def on_press(self):
        if globals.algDropDownList.ids.bfs_btn.background_color != [0.8, 0.8, 0.8, 1]:  # if is not pressed
            globals.algDropDownList.ids.bfs_btn.background_normal: ''
            globals.algDropDownList.ids.bfs_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The buttons from the dropdown list can't be pressed at the same time
            globals.algDropDownList.ids.dfs_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.algDropDownList.ids.dijkstra_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:  # if it is pressed
            globals.algDropDownList.ids.bfs_btn.background_normal: ''
            globals.algDropDownList.ids.bfs_btn.background_color = (0.34, 0.34, 0.34, 1)

        globals.mainViewWidget.ids.bfs_txt_input.visible = True
        globals.mainViewWidget.ids.bfs_txt_lbl.visible = True
        globals.mainViewWidget.ids.down_btns.visible = True
        globals.mainViewWidget.ids.play_btn.visible = True
        globals.mainViewWidget.ids.play_btn.bind(on_press=CircularButton.on_press)


class DfsButton(ButtonBehavior):

    def on_press(self):
        if globals.algDropDownList.ids.dfs_btn.background_color != [0.8, 0.8, 0.8, 1]:  # if is not pressed
            globals.algDropDownList.ids.dfs_btn.background_normal: ''
            globals.algDropDownList.ids.dfs_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The buttons from the dropdown list can't be pressed at the same time
            globals.algDropDownList.ids.bfs_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.algDropDownList.ids.dijkstra_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:  # if it is pressed
            globals.algDropDownList.ids.dfs_btn.background_normal: ''
            globals.algDropDownList.ids.dfs_btn.background_color = (0.34, 0.34, 0.34, 1)

        globals.mainViewWidget.ids.bfs_txt_input.visible = True
        globals.mainViewWidget.ids.bfs_txt_lbl.visible = True
        #globals.graphManager.DFS(globals.mainViewWidget.ids.bfs_txt_input.text)


class WhiteButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('white')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()
        #dr = ChangeColorDropDownList()
        #dr.ids.color_dropdown.dismiss()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('white')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()
        #globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('white')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
        globals.graphManager.update_canvas()
       # globals.popupWidget.ids.changeColor_btn3.close()


class BlackButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('black')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()
      #  globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('black')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()
       # globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('black')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
        globals.graphManager.update_canvas()
      #  globals.popupWidget.ids.changeColor_btn3.close()

class RedButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('red')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()
       # globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('red')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('red')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
        globals.graphManager.update_canvas()
      #  globals.popupWidget.ids.changeColor_btn3.close()

class YellowButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('yellow')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()
      #  globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('yellow')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('yellow')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn3.close()

class OrangeButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('orange')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()
       # globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('orange')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('orange')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
        #globals.popupWidget.ids.changeColor_btn3.close()

class BlueButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('blue')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()
       # globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('blue')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('blue')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
       # globals.popupWidget.ids.changeColor_btn3.close()

class PurpleButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('purple')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()
        #globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('purple')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('purple')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
       # globals.popupWidget.ids.changeColor_btn3.close()

class GreenButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('green')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()
       # globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('green')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()
        #globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('green')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
       # globals.popupWidget.ids.changeColor_btn3.close()

class PinkButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('pink')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()
        #globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('pink')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()
       # globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('pink')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn3.close()