from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from globals import globals
from graph import node_widget
from graph import edge_widget

class PopupWidget(GridLayout):

    def closePopUp(self):
        globals.popup_window.dismiss()
       # globals.graph_manager.update_canvas()

    def new_radius(self, *args):
        self.ids.nodeRadius_lbl.text = str(int(args[1]))
        node_widget.changeNodeRadius(int(args[1]))
        self.ids.radiusSlider.value = int(args[1])
       # globals.graph_manager.update_canvas()
        for edge in globals.graph_manager.edgeWidgets:
            edge.updateCoords()

    def new_length(self, *args):
        self.ids.edgeLength_lbl.text = str(int(args[1]))
        edge_widget.changeEdgeLength(int(args[1]))
        self.ids.edgeSlider.value = int(args[1])

    def getNodeWidgetBackgroundColor(self):
        return globals.NodeWidgetBackgroundColor

    def getNodeWidgetColor(self):
        return globals.NodeWidgetColor

    def getEdgeWidgetColor(self):
        return globals.EdgeWidgetColor

    def getEdgeSliderValue(self):
        return globals.edge_length

    def getRadiusSliderValue(self):
        return globals.node_radius

class ErrorPopupWidget(BoxLayout):
    def setText(self, text):
        globals.error_popup_widget.ids.error_popup_lbl.text = text

    def closePopUp(self):
        globals.popup_window.dismiss()