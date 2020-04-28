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
        globals.popup_widget = popup_widget.PopupWidget()
        globals.popup_window = Popup(title="Settings", content=globals.popup_widget, size_hint=(None, None), size=(450, 425), auto_dismiss=False)
        globals.popup_window.open()

        dropdown1 = ChangeColorDropDownList()
        globals.popup_widget.ids.changeColor_btn1.bind(on_release=dropdown1.open)
        globals.change_color_drop_down_list = dropdown1
        globals.change_color_drop_down_list.ids.white_btn.bind(on_press=WhiteButton.dropdown1)
        globals.change_color_drop_down_list.ids.white_btn.bind(on_release=dropdown1.dismiss)
        globals.change_color_drop_down_list.ids.black_btn.bind(on_press=BlackButton.dropdown1)
        globals.change_color_drop_down_list.ids.black_btn.bind(on_release=dropdown1.dismiss)
        globals.change_color_drop_down_list.ids.red_btn.bind(on_press=RedButton.dropdown1)
        globals.change_color_drop_down_list.ids.red_btn.bind(on_release=dropdown1.dismiss)
        globals.change_color_drop_down_list.ids.yellow_btn.bind(on_press=YellowButton.dropdown1)
        globals.change_color_drop_down_list.ids.yellow_btn.bind(on_release=dropdown1.dismiss)
        globals.change_color_drop_down_list.ids.orange_btn.bind(on_press=OrangeButton.dropdown1)
        globals.change_color_drop_down_list.ids.orange_btn.bind(on_release=dropdown1.dismiss)
        globals.change_color_drop_down_list.ids.blue_btn.bind(on_press=BlueButton.dropdown1)
        globals.change_color_drop_down_list.ids.blue_btn.bind(on_release=dropdown1.dismiss)
        globals.change_color_drop_down_list.ids.purple_btn.bind(on_press=PurpleButton.dropdown1)
        globals.change_color_drop_down_list.ids.purple_btn.bind(on_release=dropdown1.dismiss)
        globals.change_color_drop_down_list.ids.green_btn.bind(on_press=GreenButton.dropdown1)
        globals.change_color_drop_down_list.ids.green_btn.bind(on_release=dropdown1.dismiss)
        globals.change_color_drop_down_list.ids.pink_btn.bind(on_press=PinkButton.dropdown1)
        globals.change_color_drop_down_list.ids.pink_btn.bind(on_release=dropdown1.dismiss)

        dropdown2 = ChangeColorDropDownList()
        globals.popup_widget.ids.changeColor_btn2.bind(on_release=dropdown2.open)
        globals.change_color_drop_down_list = dropdown2
        globals.change_color_drop_down_list.ids.white_btn.bind(on_press=WhiteButton.dropdown2)
        globals.change_color_drop_down_list.ids.white_btn.bind(on_release=dropdown2.dismiss)
        globals.change_color_drop_down_list.ids.black_btn.bind(on_press=BlackButton.dropdown2)
        globals.change_color_drop_down_list.ids.black_btn.bind(on_release=dropdown2.dismiss)
        globals.change_color_drop_down_list.ids.red_btn.bind(on_press=RedButton.dropdown2)
        globals.change_color_drop_down_list.ids.red_btn.bind(on_release=dropdown2.dismiss)
        globals.change_color_drop_down_list.ids.yellow_btn.bind(on_press=YellowButton.dropdown2)
        globals.change_color_drop_down_list.ids.yellow_btn.bind(on_release=dropdown2.dismiss)
        globals.change_color_drop_down_list.ids.orange_btn.bind(on_press=OrangeButton.dropdown2)
        globals.change_color_drop_down_list.ids.orange_btn.bind(on_release=dropdown2.dismiss)
        globals.change_color_drop_down_list.ids.blue_btn.bind(on_press=BlueButton.dropdown2)
        globals.change_color_drop_down_list.ids.blue_btn.bind(on_release=dropdown2.dismiss)
        globals.change_color_drop_down_list.ids.purple_btn.bind(on_press=PurpleButton.dropdown2)
        globals.change_color_drop_down_list.ids.purple_btn.bind(on_release=dropdown2.dismiss)
        globals.change_color_drop_down_list.ids.green_btn.bind(on_press=GreenButton.dropdown2)
        globals.change_color_drop_down_list.ids.green_btn.bind(on_release=dropdown2.dismiss)
        globals.change_color_drop_down_list.ids.pink_btn.bind(on_press=PinkButton.dropdown2)
        globals.change_color_drop_down_list.ids.pink_btn.bind(on_release=dropdown2.dismiss)
        dropdown2.dismiss()

        dropdown3 = ChangeColorDropDownList()
        globals.popup_widget.ids.changeColor_btn3.bind(on_release=dropdown3.open)
        globals.change_color_drop_down_list = dropdown3
        globals.change_color_drop_down_list.ids.white_btn.bind(on_press=WhiteButton.dropdown3)
        globals.change_color_drop_down_list.ids.white_btn.bind(on_release=dropdown3.dismiss)
        globals.change_color_drop_down_list.ids.black_btn.bind(on_press=BlackButton.dropdown3)
        globals.change_color_drop_down_list.ids.black_btn.bind(on_release=dropdown3.dismiss)
        globals.change_color_drop_down_list.ids.red_btn.bind(on_press=RedButton.dropdown3)
        globals.change_color_drop_down_list.ids.red_btn.bind(on_release=dropdown3.dismiss)
        globals.change_color_drop_down_list.ids.yellow_btn.bind(on_press=YellowButton.dropdown3)
        globals.change_color_drop_down_list.ids.yellow_btn.bind(on_release=dropdown3.dismiss)
        globals.change_color_drop_down_list.ids.orange_btn.bind(on_press=OrangeButton.dropdown3)
        globals.change_color_drop_down_list.ids.orange_btn.bind(on_release=dropdown3.dismiss)
        globals.change_color_drop_down_list.ids.blue_btn.bind(on_press=BlueButton.dropdown3)
        globals.change_color_drop_down_list.ids.blue_btn.bind(on_release=dropdown3.dismiss)
        globals.change_color_drop_down_list.ids.purple_btn.bind(on_press=PurpleButton.dropdown3)
        globals.change_color_drop_down_list.ids.purple_btn.bind(on_release=dropdown3.dismiss)
        globals.change_color_drop_down_list.ids.green_btn.bind(on_press=GreenButton.dropdown3)
        globals.change_color_drop_down_list.ids.green_btn.bind(on_press=GreenButton.dropdown3)
        globals.change_color_drop_down_list.ids.pink_btn.bind(on_press=PinkButton.dropdown3)
        globals.change_color_drop_down_list.ids.pink_btn.bind(on_press=PinkButton.dropdown3)


        globals.popup_widget.ids.apply_btn.bind(on_press=globals.graph_manager.parse_graph_data)

def callback(instance, value):
    if value == False:
        globals.forces = False
    else:
        globals.forces = True
        force_layout.recalculatePositions()

class saveBtn(ButtonBehavior):
    def on_press(self):
        globals.main_view_widget.export_to_png()


class AlgDropDownList(DropDown):
    pass

class InputDropDownList(DropDown):
    pass

class ChangeColorDropDownList(DropDown):
    pass


class ListOfEdgesButton(ButtonBehavior):

    def on_press(self):
        if globals.input_drop_down_list.ids.listOfEdges_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.input_drop_down_list.ids.listOfEdges_btn.background_normal: ''
            globals.input_drop_down_list.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.input_drop_down_list.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.input_drop_down_list.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.input_drop_down_list.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            globals.edge_list_input_btn = True
            globals.adjacency_list_input_btn = False
            globals.adjacency_matrix_input_btn = False
            globals.cost_matrix_input_btn = False
            globals.main_view_widget.ids.input_nodes.hint_text = "node1Id  node2Id\nnode3Id  node4Id"


class AdjacencyListButton(ButtonBehavior):

    def on_press(self):
        if globals.input_drop_down_list.ids.adjacencyList_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.input_drop_down_list.ids.adjacencyList_btn.background_normal: ''
            globals.input_drop_down_list.ids.adjacencyList_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.input_drop_down_list.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.input_drop_down_list.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.input_drop_down_list.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            globals.edge_list_input_btn = False
            globals.adjacency_list_input_btn = True
            globals.adjacency_matrix_input_btn = False
            globals.cost_matrix_input_btn = False
            globals.main_view_widget.ids.input_nodes.hint_text = "node: neighbor1, neighbor2, ..."

        else:   # if it is pressed
            globals.input_drop_down_list.ids.adjacencyList_btn.background_normal: ''
            globals.input_drop_down_list.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            globals.input_drop_down_list.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


class AdjacencyMatrixButton(ButtonBehavior):

    def on_press(self):
        if globals.input_drop_down_list.ids.adjacencyMatrix_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.input_drop_down_list.ids.adjacencyMatrix_btn.background_normal: ''
            globals.input_drop_down_list.ids.adjacencyMatrix_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.input_drop_down_list.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.input_drop_down_list.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.input_drop_down_list.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            globals.edge_list_input_btn = False
            globals.adjacency_list_input_btn = False
            globals.adjacency_matrix_input_btn = True
            globals.cost_matrix_input_btn = False
            globals.main_view_widget.ids.input_nodes.hint_text = "0 1 1 0\n" \
                                                               "1 0 0 1\n" \
                                                               "0 1 0 1\n" \
                                                               "1 1 1 0"

        else:   # if it is pressed
            globals.input_drop_down_list.ids.adjacencyMatrix_btn.background_normal: ''
            globals.input_drop_down_list.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            globals.input_drop_down_list.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


class CostMatrixButton(ButtonBehavior):

    def on_press(self):
        if globals.input_drop_down_list.ids.costMatrix_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.input_drop_down_list.ids.costMatrix_btn.background_normal: ''
            globals.input_drop_down_list.ids.costMatrix_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.input_drop_down_list.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.input_drop_down_list.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.input_drop_down_list.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            globals.edge_list_input_btn = False
            globals.adjacency_list_input_btn = False
            globals.adjacency_matrix_input_btn = False
            globals.cost_matrix_input_btn = True

            globals.main_view_widget.ids.input_nodes.hint_text = "0 123 78 62\n" \
                                                               "13 0 6 198\n" \
                                                               "26 4 0 17\n" \
                                                               "65 143 31 0"

        else:   # if it is pressed
            globals.input_drop_down_list.ids.costMatrix_btn.background_normal: ''
            globals.input_drop_down_list.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            globals.input_drop_down_list.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


class UndirectedButton(ButtonBehavior):

    def on_press(self):
        if globals.main_view_widget.ids.undirected_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed

            globals.main_view_widget.ids.undirected_btn.background_normal: ''
            globals.main_view_widget.ids.undirected_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graph_manager.setisDirected(False)

            # The directed and undirected buttons can't be pressed at the same time
            globals.main_view_widget.ids.directed_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:   # if it is pressed
            globals.main_view_widget.ids.undirected_btn.background_normal: ''
            globals.main_view_widget.ids.undirected_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The directed and undirected buttons can't be unpressed at the same time
            globals.main_view_widget.ids.directed_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graph_manager.setisDirected(True)

        globals.graph_manager.parse_graph_data(globals.main_view_widget.ids.input_nodes.text)
       # # globals.graph_manager.update_canvas()


class DirectedButton(ButtonBehavior):

    def on_press(self):
        if globals.main_view_widget.ids.directed_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            #print(globals.mainViewWidget.ids.directed_btn.background_normal)
            globals.main_view_widget.ids.directed_btn.background_normal: ''
            globals.main_view_widget.ids.directed_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graph_manager.setisDirected(True)

            # The directed and undirected buttons can't be pressed at the same time
            globals.main_view_widget.ids.undirected_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:   # if it is pressed
            globals.main_view_widget.ids.directed_btn.background_normal: ''
            globals.main_view_widget.ids.directed_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The directed and undirected buttons can't be unpressed at the same time
            globals.main_view_widget.ids.undirected_btn.background_color = (0.8, 0.8, 0.8, 1)
            globals.graph_manager.setisDirected(False)

        globals.graph_manager.parse_graph_data(globals.main_view_widget.ids.input_nodes.text)
       # # globals.graph_manager.update_canvas()


class DijkstraButton(ButtonBehavior):

    def on_press(self):
        if globals.algorithms_drop_down_list.ids.dijkstra_btn.background_color != [0.8, 0.8, 0.8, 1]:  # if is not pressed
            globals.algorithms_drop_down_list.ids.dijkstra_btn.background_normal: ''
            globals.algorithms_drop_down_list.ids.dijkstra_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The buttons from the dropdown list can't be pressed at the same time
            globals.algorithms_drop_down_list.ids.bfs_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.algorithms_drop_down_list.ids.dfs_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:  # if it is pressed
            globals.algorithms_drop_down_list.ids.dijkstra_btn.background_normal: ''
            globals.algorithms_drop_down_list.ids.dijkstra_btn.background_color = (0.34, 0.34, 0.34, 1)


class BfsButton(ButtonBehavior):

    def on_press(self):
        if globals.algorithms_drop_down_list.ids.bfs_btn.background_color != [0.8, 0.8, 0.8, 1]:  # if is not pressed
            globals.algorithms_drop_down_list.ids.bfs_btn.background_normal: ''
            globals.algorithms_drop_down_list.ids.bfs_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The buttons from the dropdown list can't be pressed at the same time
            globals.algorithms_drop_down_list.ids.dfs_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.algorithms_drop_down_list.ids.dijkstra_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:  # if it is pressed
            globals.algorithms_drop_down_list.ids.bfs_btn.background_normal: ''
            globals.algorithms_drop_down_list.ids.bfs_btn.background_color = (0.34, 0.34, 0.34, 1)

        globals.main_view_widget.ids.bfs_txt_input.visible = True
        globals.main_view_widget.ids.bfs_txt_lbl.visible = True
        globals.main_view_widget.ids.down_btns.visible = True
        globals.main_view_widget.ids.play_btn.visible = True
        globals.main_view_widget.ids.play_btn.bind(on_press=CircularButton.on_press)


class DfsButton(ButtonBehavior):

    def on_press(self):
        if globals.algorithms_drop_down_list.ids.dfs_btn.background_color != [0.8, 0.8, 0.8, 1]:  # if is not pressed
            globals.algorithms_drop_down_list.ids.dfs_btn.background_normal: ''
            globals.algorithms_drop_down_list.ids.dfs_btn.background_color = (0.8, 0.8, 0.8, 1)

            # The buttons from the dropdown list can't be pressed at the same time
            globals.algorithms_drop_down_list.ids.bfs_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.algorithms_drop_down_list.ids.dijkstra_btn.background_color = (0.34, 0.34, 0.34, 1)

        else:  # if it is pressed
            globals.algorithms_drop_down_list.ids.dfs_btn.background_normal: ''
            globals.algorithms_drop_down_list.ids.dfs_btn.background_color = (0.34, 0.34, 0.34, 1)

        globals.main_view_widget.ids.bfs_txt_input.visible = True
        globals.main_view_widget.ids.bfs_txt_lbl.visible = True
        #globals.graphManager.DFS(globals.mainViewWidget.ids.bfs_txt_input.text)


class WhiteButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('white')
        globals.popup_widget.ids.nodeWidgetBackground_lbl.bcolor = globals.popup_widget.getNodeWidgetBackgroundColor()
        #dr = ChangeColorDropDownList()
        #dr.ids.color_dropdown.dismiss()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('white')
        globals.popup_widget.ids.nodeWidgetColor_lbl.bcolor = globals.popup_widget.getNodeWidgetColor()
        #globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('white')
        globals.popup_widget.ids.edgeWidgetColor_lbl.bcolor = globals.popup_widget.getEdgeWidgetColor()
      #  # globals.graph_manager.update_canvas()
       # globals.popupWidget.ids.changeColor_btn3.close()


class BlackButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('black')
        globals.popup_widget.ids.nodeWidgetBackground_lbl.bcolor = globals.popup_widget.getNodeWidgetBackgroundColor()
      #  globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('black')
        globals.popup_widget.ids.nodeWidgetColor_lbl.bcolor = globals.popup_widget.getNodeWidgetColor()
       # globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('black')
        globals.popup_widget.ids.edgeWidgetColor_lbl.bcolor = globals.popup_widget.getEdgeWidgetColor()
       # # globals.graph_manager.update_canvas()
      #  globals.popupWidget.ids.changeColor_btn3.close()

class RedButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('red')
        globals.popup_widget.ids.nodeWidgetBackground_lbl.bcolor = globals.popup_widget.getNodeWidgetBackgroundColor()
       # globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('red')
        globals.popup_widget.ids.nodeWidgetColor_lbl.bcolor = globals.popup_widget.getNodeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('red')
        globals.popup_widget.ids.edgeWidgetColor_lbl.bcolor = globals.popup_widget.getEdgeWidgetColor()
        # globals.graph_manager.update_canvas()
      #  globals.popupWidget.ids.changeColor_btn3.close()

class YellowButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('yellow')
        globals.popup_widget.ids.nodeWidgetBackground_lbl.bcolor = globals.popup_widget.getNodeWidgetBackgroundColor()
      #  globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('yellow')
        globals.popup_widget.ids.nodeWidgetColor_lbl.bcolor = globals.popup_widget.getNodeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('yellow')
        globals.popup_widget.ids.edgeWidgetColor_lbl.bcolor = globals.popup_widget.getEdgeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn3.close()

class OrangeButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('orange')
        globals.popup_widget.ids.nodeWidgetBackground_lbl.bcolor = globals.popup_widget.getNodeWidgetBackgroundColor()
       # globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('orange')
        globals.popup_widget.ids.nodeWidgetColor_lbl.bcolor = globals.popup_widget.getNodeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('orange')
        globals.popup_widget.ids.edgeWidgetColor_lbl.bcolor = globals.popup_widget.getEdgeWidgetColor()
        #globals.popupWidget.ids.changeColor_btn3.close()

class BlueButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('blue')
        globals.popup_widget.ids.nodeWidgetBackground_lbl.bcolor = globals.popup_widget.getNodeWidgetBackgroundColor()
       # globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('blue')
        globals.popup_widget.ids.nodeWidgetColor_lbl.bcolor = globals.popup_widget.getNodeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('blue')
        globals.popup_widget.ids.edgeWidgetColor_lbl.bcolor = globals.popup_widget.getEdgeWidgetColor()
       # globals.popupWidget.ids.changeColor_btn3.close()

class PurpleButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('purple')
        globals.popup_widget.ids.nodeWidgetBackground_lbl.bcolor = globals.popup_widget.getNodeWidgetBackgroundColor()
        #globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('purple')
        globals.popup_widget.ids.nodeWidgetColor_lbl.bcolor = globals.popup_widget.getNodeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('purple')
        globals.popup_widget.ids.edgeWidgetColor_lbl.bcolor = globals.popup_widget.getEdgeWidgetColor()
       # globals.popupWidget.ids.changeColor_btn3.close()

class GreenButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('green')
        globals.popup_widget.ids.nodeWidgetBackground_lbl.bcolor = globals.popup_widget.getNodeWidgetBackgroundColor()
       # globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('green')
        globals.popup_widget.ids.nodeWidgetColor_lbl.bcolor = globals.popup_widget.getNodeWidgetColor()
        #globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('green')
        globals.popup_widget.ids.edgeWidgetColor_lbl.bcolor = globals.popup_widget.getEdgeWidgetColor()
       # globals.popupWidget.ids.changeColor_btn3.close()

class PinkButton():

    def dropdown1(self):
        node_widget.changeNodeWidgetBackgroundColor('pink')
        globals.popup_widget.ids.nodeWidgetBackground_lbl.bcolor = globals.popup_widget.getNodeWidgetBackgroundColor()
        #globals.popupWidget.ids.changeColor_btn1.close()

    def dropdown2(self):
        node_widget.changeNodeWidgetColor('pink')
        globals.popup_widget.ids.nodeWidgetColor_lbl.bcolor = globals.popup_widget.getNodeWidgetColor()
       # globals.popupWidget.ids.changeColor_btn2.close()

    def dropdown3(self):
        edge_widget.changeEdgeWidgetColor('pink')
        globals.popup_widget.ids.edgeWidgetColor_lbl.bcolor = globals.popup_widget.getEdgeWidgetColor()
      #  globals.popupWidget.ids.changeColor_btn3.close()