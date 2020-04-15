from kivy.uix.behaviors import ButtonBehavior
from gui import globals
from kivy.uix.dropdown import DropDown
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget


class MyPopUpWidget(Widget):
    pass

class SettingsButton(ButtonBehavior):
    def on_press(self):
        popUpWidget = MyPopUpWidget()
        popUpWindow = Popup(title="Settings", content=popUpWidget, size_hint=(0.7, 0.7))
        popUpWindow.open()

class AlgDropDownList(DropDown):
    pass

class InputDropDownList(DropDown):
    pass

class ListOfEdgesButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(ListOfEdgesButton, self).__init__(**kwargs)

    def on_press(self):
        if globals.inputDropDownList.ids.listOfEdges_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.inputDropDownList.ids.listOfEdges_btn.background_normal: ''
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.inputDropDownList.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)


class AdjacencyListButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(AdjacencyListButton, self).__init__(**kwargs)

    def on_press(self):
        if globals.inputDropDownList.ids.adjacencyList_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.inputDropDownList.ids.adjacencyList_btn.background_normal: ''
            globals.inputDropDownList.ids.adjacencyList_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)


        else:   # if it is pressed
            globals.inputDropDownList.ids.adjacencyList_btn.background_normal: ''
            globals.inputDropDownList.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


class AdjacencyMatrixButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(AdjacencyMatrixButton, self).__init__(**kwargs)

    def on_press(self):
        if globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_normal: ''
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)


        else:   # if it is pressed
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_normal: ''
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


class CostMatrixButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(CostMatrixButton, self).__init__(**kwargs)

    def on_press(self):
        if globals.inputDropDownList.ids.costMatrix_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            globals.inputDropDownList.ids.costMatrix_btn.background_normal: ''
            globals.inputDropDownList.ids.costMatrix_btn.background_color = (0.8, 0.8, 0.8, 1)


            # The buttons from the dropdown list can't be pressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.adjacencyList_btn.background_color = (0.34, 0.34, 0.34, 1)
            globals.inputDropDownList.ids.adjacencyMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)


        else:   # if it is pressed
            globals.inputDropDownList.ids.costMatrix_btn.background_normal: ''
            globals.inputDropDownList.ids.costMatrix_btn.background_color = (0.34, 0.34, 0.34, 1)

            # The buttons can't be unpressed at the same time
            globals.inputDropDownList.ids.listOfEdges_btn.background_color = (0.8, 0.8, 0.8, 1)


class UndirectedButton(ButtonBehavior):
    def __init__(self, **kwargs):
        super(UndirectedButton, self).__init__(**kwargs)

    def on_press(self):
        if globals.mainViewWidget.ids.undirected_btn.background_color != [0.8, 0.8, 0.8, 1]: # if is not pressed
            # print(globals.mainViewWidget.ids.undirected_btn.background_normal)
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
    def __init__(self, **kwargs):
        super(DirectedButton, self).__init__(**kwargs)

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
    def __init__(self, **kwargs):
        super(DijkstraButton, self).__init__(**kwargs)

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
    def __init__(self, **kwargs):
        super(BfsButton, self).__init__(**kwargs)

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
    def __init__(self, **kwargs):
        super(DfsButton, self).__init__(**kwargs)

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
