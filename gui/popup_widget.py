from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from globals import globals
from graph import node_widget
from graph import edge_widget
from kivy.properties import ListProperty


class PopupWidget(GridLayout):

    node_background_color_lbl = ListProperty(globals.colors['white'])
    node_border_color_lbl = ListProperty(globals.colors['black'])
    edge_color_lbl = ListProperty(globals.colors['black'])

    def __init__(self, node_background_color, node_border_color, edge_color):
        super().__init__()
        self.node_background_color_lbl = node_background_color
        self.node_border_color_lbl = node_border_color
        self.edge_color_lbl = edge_color

    def closePopUp(self):
        globals.popup_window.dismiss()

    def new_radius(self, *args):
        self.ids.nodeRadius_lbl.text = str(int(args[1]))
        node_widget.radius = (int(args[1]))
        self.ids.radiusSlider.value = int(args[1])

        for edge in globals.graph_manager.edge_widgets:
            edge.updateCoords()

    def new_length(self, *args):
        self.ids.edgeLength_lbl.text = str(int(args[1]))
        edge_widget.changeEdgeLength(int(args[1]))
        self.ids.edgeSlider.value = int(args[1])

    def getEdgeSliderValue(self):
        return globals.edge_length

    def getRadiusSliderValue(self):
        return globals.node_radius


class ErrorPopupWidget(BoxLayout):
    def setText(self, text):
        globals.error_popup_widget.ids.error_popup_lbl.text = text

    def closePopUp(self):
        globals.popup_window.dismiss()