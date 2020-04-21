from kivy.uix.behaviors import ButtonBehavior
from globals import globals
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from graph import node_widget
from graph import edge_widget
from gui import popup_widget


class SettingsButton(ButtonBehavior):

    def on_release(self):
        globals.popupWidget = popup_widget.PopupWidget()
        globals.popupWindow = Popup(title="Settings", content=globals.popupWidget, size_hint=(None, None), size=(450, 425))
        globals.popupWindow.open()

        dropdown1 = ChangeColorDropDownList()
        globals.popupWidget.ids.changeColor_btn1.bind(on_release=dropdown1.open)
        globals.changeColorDropDownList = dropdown1
        globals.changeColorDropDownList.ids.white_btn.bind(on_press=WhiteButton.dropdown1)
        globals.changeColorDropDownList.ids.black_btn.bind(on_press=BlackButton.dropdown1)
        globals.changeColorDropDownList.ids.red_btn.bind(on_press=RedButton.dropdown1)
        globals.changeColorDropDownList.ids.yellow_btn.bind(on_press=YellowButton.dropdown1)
        globals.changeColorDropDownList.ids.orange_btn.bind(on_press=OrangeButton.dropdown1)
        globals.changeColorDropDownList.ids.blue_btn.bind(on_press=BlueButton.dropdown1)
        globals.changeColorDropDownList.ids.purple_btn.bind(on_press=PurpleButton.dropdown1)
        globals.changeColorDropDownList.ids.green_btn.bind(on_press=GreenButton.dropdown1)
        globals.changeColorDropDownList.ids.pink_btn.bind(on_press=PinkButton.dropdown1)

        dropdown2 = ChangeColorDropDownList()
        globals.popupWidget.ids.changeColor_btn2.bind(on_release=dropdown2.open)
        globals.changeColorDropDownList = dropdown2
        globals.changeColorDropDownList.ids.white_btn.bind(on_press=WhiteButton.dropdown2)
        globals.changeColorDropDownList.ids.black_btn.bind(on_press=BlackButton.dropdown2)
        globals.changeColorDropDownList.ids.red_btn.bind(on_press=RedButton.dropdown2)
        globals.changeColorDropDownList.ids.yellow_btn.bind(on_press=YellowButton.dropdown2)
        globals.changeColorDropDownList.ids.orange_btn.bind(on_press=OrangeButton.dropdown2)
        globals.changeColorDropDownList.ids.blue_btn.bind(on_press=BlueButton.dropdown2)
        globals.changeColorDropDownList.ids.purple_btn.bind(on_press=PurpleButton.dropdown2)
        globals.changeColorDropDownList.ids.green_btn.bind(on_press=GreenButton.dropdown2)
        globals.changeColorDropDownList.ids.pink_btn.bind(on_press=PinkButton.dropdown2)

        dropdown3 = ChangeColorDropDownList()
        globals.popupWidget.ids.changeColor_btn3.bind(on_release=dropdown3.open)
        globals.changeColorDropDownList = dropdown3
        globals.changeColorDropDownList.ids.white_btn.bind(on_press=WhiteButton.dropdown3)
        globals.changeColorDropDownList.ids.black_btn.bind(on_press=BlackButton.dropdown3)
        globals.changeColorDropDownList.ids.red_btn.bind(on_press=RedButton.dropdown3)
        globals.changeColorDropDownList.ids.yellow_btn.bind(on_press=YellowButton.dropdown3)
        globals.changeColorDropDownList.ids.orange_btn.bind(on_press=OrangeButton.dropdown3)
        globals.changeColorDropDownList.ids.blue_btn.bind(on_press=BlueButton.dropdown3)
        globals.changeColorDropDownList.ids.purple_btn.bind(on_press=PurpleButton.dropdown3)
        globals.changeColorDropDownList.ids.green_btn.bind(on_press=GreenButton.dropdown3)
        globals.changeColorDropDownList.ids.pink_btn.bind(on_press=PinkButton.dropdown3)


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


class WhiteButton():

    def onPress(self):
        if globals.changeColorDropDownList.ids.white_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.changeColorDropDownList.ids.white_btn.background_normal: ''
            globals.changeColorDropDownList.ids.white_btn.background_color = [0.8, 0.8, 0.8, 1]

            # The other buttons can't be pressed at the same time
            globals.changeColorDropDownList.ids.black_btn.background_color = [0.34, 0.34, 0.34, 1]
            globals.changeColorDropDownList.ids.red_btn.background_color = [0.34, 0.34, 0.34, 1]
            globals.changeColorDropDownList.ids.yellow_btn.background_color = [0.34, 0.34, 0.34, 1]
            globals.changeColorDropDownList.ids.orange_btn.background_color = [0.34, 0.34, 0.34, 1]
            globals.changeColorDropDownList.ids.blue_btn.background_color = [0.34, 0.34, 0.34, 1]
            globals.changeColorDropDownList.ids.purple_btn.background_color = [0.34, 0.34, 0.34, 1]
            globals.changeColorDropDownList.ids.green_btn.background_color = [0.34, 0.34, 0.34, 1]
            globals.changeColorDropDownList.ids.pink_btn.background_color = [0.34, 0.34, 0.34, 1]

    def dropdown1(self):
       # white = WhiteButton()
       # white.onPress()
        node_widget.changeNodeWidgetBackgroundColor('white')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()

    def dropdown2(self):
        #white = WhiteButton()
        #white.onPress()
        node_widget.changeNodeWidgetColor('white')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()

    def dropdown3(self):
        #white = WhiteButton()
        #white.onPress()
        edge_widget.changeEdgeWidgetColor('white')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
        globals.graphManager.update_canvas()


class BlackButton():

    def onPress(self):
        if globals.changeColorDropDownList.ids.black_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.changeColorDropDownList.ids.black_btn.background_normal: ''
            globals.changeColorDropDownList.ids.black_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The other buttons can't be pressed at the same time
            globals.changeColorDropDownList.ids.white_btn.background_normal: ''
            globals.changeColorDropDownList.ids.white_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.red_btn.background_normal: ''
            globals.changeColorDropDownList.ids.red_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.yellow_btn.background_normal: ''
            globals.changeColorDropDownList.ids.yellow_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.orange_btn.background_normal: ''
            globals.changeColorDropDownList.ids.orange_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.blue_btn.background_normal: ''
            globals.changeColorDropDownList.ids.blue_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.purple_btn.background_normal: ''
            globals.changeColorDropDownList.ids.purple_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.green_btn.background_normal: ''
            globals.changeColorDropDownList.ids.green_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.pink_btn.background_normal: ''
            globals.changeColorDropDownList.ids.pink_btn.background_color = (0.34, 0.34, 0.34, 1)

    def dropdown1(self):
        #black = BlackButton()
        #black.onPress()
        node_widget.changeNodeWidgetBackgroundColor('black')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()

    def dropdown2(self):
        #black = BlackButton()
        #black.onPress()
        node_widget.changeNodeWidgetColor('black')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()

    def dropdown3(self):
        #black = BlackButton()
        #black.onPress()
        edge_widget.changeEdgeWidgetColor('black')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
        globals.graphManager.update_canvas()

class RedButton():

    def onPress(self):
        if globals.changeColorDropDownList.ids.red_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.changeColorDropDownList.ids.red_btn.background_normal: ''
            globals.changeColorDropDownList.ids.red_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The other buttons can't be pressed at the same time
            globals.changeColorDropDownList.ids.black_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.white_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.yellow_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.orange_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.blue_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.purple_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.green_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.pink_btn.background_color = (0.34, 0.34, 0.34, 1)

    def dropdown1(self):
        #red = RedButton()
        #red.onPress()
        node_widget.changeNodeWidgetBackgroundColor('red')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()

    def dropdown2(self):
        #red = RedButton()
        #red.onPress()
        node_widget.changeNodeWidgetColor('red')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()

    def dropdown3(self):
        #red = RedButton()
        #red.onPress()
        edge_widget.changeEdgeWidgetColor('red')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()
        globals.graphManager.update_canvas()


class YellowButton():

    def onPress(self):
        if globals.changeColorDropDownList.ids.yellow_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.changeColorDropDownList.ids.yellow_btn.background_normal: ''
            globals.changeColorDropDownList.ids.yellow_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The other buttons can't be pressed at the same time
            globals.changeColorDropDownList.ids.black_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.white_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.red_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.orange_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.blue_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.purple_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.green_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.pink_btn.background_color = (0.34, 0.34, 0.34, 1)

    def dropdown1(self):
        #yellow = YellowButton()
        #yellow.onPress()
        node_widget.changeNodeWidgetBackgroundColor('yellow')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()

    def dropdown2(self):
        #yellow = YellowButton()
        #yellow.onPress()
        node_widget.changeNodeWidgetColor('yellow')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()

    def dropdown3(self):
        #yellow = YellowButton()
        #yellow.onPress()
        edge_widget.changeEdgeWidgetColor('yellow')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()


class OrangeButton():

    def onPress(self):
        if globals.changeColorDropDownList.ids.orange_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.changeColorDropDownList.ids.orange_btn.background_normal: ''
            globals.changeColorDropDownList.ids.orange_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The other buttons can't be pressed at the same time
            globals.changeColorDropDownList.ids.black_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.white_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.red_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.yellow_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.blue_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.purple_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.green_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.pink_btn.background_color = (0.34, 0.34, 0.34, 1)

    def dropdown1(self):
        #orange = OrangeButton()
        #orange.onPress()
        node_widget.changeNodeWidgetBackgroundColor('orange')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()

    def dropdown2(self):
        #orange = OrangeButton()
        #orange.onPress()
        node_widget.changeNodeWidgetColor('orange')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()

    def dropdown3(self):
        #orange = OrangeButton()
        #orange.onPress()
        edge_widget.changeEdgeWidgetColor('orange')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()

class BlueButton():

    def onPress(self):
        if globals.changeColorDropDownList.ids.blue_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.changeColorDropDownList.ids.blue_btn.background_normal: ''
            globals.changeColorDropDownList.ids.blue_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The other buttons can't be pressed at the same time
            globals.changeColorDropDownList.ids.black_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.white_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.red_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.yellow_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.orange_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.purple_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.green_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.pink_btn.background_color = (0.34, 0.34, 0.34, 1)

    def dropdown1(self):
        #blue = BlueButton()
        #blue.onPress()
        node_widget.changeNodeWidgetBackgroundColor('blue')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()

    def dropdown2(self):
        #blue = BlueButton()
        #blue.onPress()
        node_widget.changeNodeWidgetColor('blue')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()

    def dropdown3(self):
        #blue = BlueButton()
        #blue.onPress()
        edge_widget.changeEdgeWidgetColor('blue')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()


class PurpleButton():

    def onPress(self):
        if globals.changeColorDropDownList.ids.purple_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.changeColorDropDownList.ids.purple_btn.background_normal: ''
            globals.changeColorDropDownList.ids.purple_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The other buttons can't be pressed at the same time
            globals.changeColorDropDownList.ids.black_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.white_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.red_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.yellow_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.orange_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.blue_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.green_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.pink_btn.background_color = (0.34, 0.34, 0.34, 1)

    def dropdown1(self):
        #purple = PurpleButton()
        #purple.onPress()
        node_widget.changeNodeWidgetBackgroundColor('purple')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()

    def dropdown2(self):
        #purple = PurpleButton()
        #purple.onPress()
        node_widget.changeNodeWidgetColor('purple')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()

    def dropdown3(self):
        #purple = PurpleButton()
        #purple.onPress()
        edge_widget.changeEdgeWidgetColor('purple')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()


class GreenButton():

    def onPress(self):
        if globals.changeColorDropDownList.ids.green_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.changeColorDropDownList.ids.green_btn.background_normal: ''
            globals.changeColorDropDownList.ids.green_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The other buttons can't be pressed at the same time
            globals.changeColorDropDownList.ids.black_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.white_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.red_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.yellow_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.orange_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.blue_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.purple_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.pink_btn.background_color = (0.34, 0.34, 0.34, 1)

    def dropdown1(self):
        #green = GreenButton()
        #green.onPress()
        node_widget.changeNodeWidgetBackgroundColor('green')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()

    def dropdown2(self):
        #green = GreenButton()
        #green.onPress()
        node_widget.changeNodeWidgetColor('green')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()

    def dropdown3(self):
        #green = GreenButton()
        #green.onPress()
        edge_widget.changeEdgeWidgetColor('green')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()


class PinkButton():

    def onPress(self):
        if globals.changeColorDropDownList.ids.pink_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.changeColorDropDownList.ids.pink_btn.background_normal: ''
            globals.changeColorDropDownList.ids.pink_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The other buttons can't be pressed at the same time
            globals.changeColorDropDownList.ids.black_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.white_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.red_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.yellow_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.orange_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.blue_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.purple_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.changeColorDropDownList.ids.green_btn.background_color = (0.34, 0.34, 0.34, 1)

    def dropdown1(self):
        #pink = PinkButton()
        #pink.onPress()
        node_widget.changeNodeWidgetBackgroundColor('pink')
        globals.popupWidget.ids.nodeWidgetBackground_lbl.bcolor = globals.popupWidget.getNodeWidgetBackgroundColor()

    def dropdown2(self):
        #pink = PinkButton()
        #pink.onPress()
        node_widget.changeNodeWidgetColor('pink')
        globals.popupWidget.ids.nodeWidgetColor_lbl.bcolor = globals.popupWidget.getNodeWidgetColor()

    def dropdown3(self):
        #pink = PinkButton()
        #pink.onPress()
        edge_widget.changeEdgeWidgetColor('pink')
        globals.popupWidget.ids.edgeWidgetColor_lbl.bcolor = globals.popupWidget.getEdgeWidgetColor()