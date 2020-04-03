import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config

from gui.graph_manager import GraphManager

kivy.require('2.0.0')

maxid = 0

graphManager = GraphManager()


class NodeWidget(Widget):

    def __init__(self, nr, pos):
        super().__init__()
        self.size = [50, 50]
        self.pos = [pos[0] - self.size[0] / 2, pos[1] - self.size[1] / 2]
        self.nr = nr  # this is the id of the node


class MainViewWidget(Widget):
    def on_touch_down(self, touch):
        if self.ids.graph_canvas.collide_point(*touch.pos):
            global maxid
            maxid += 1
            nx = touch.pos[0] - self.ids.graph_canvas.pos[0]
            ny = touch.pos[1] - self.ids.graph_canvas.pos[1]

            if nx < 30:
                nx = 30

            if ny < 30:
                ny = 30

            if nx > self.ids.graph_canvas.size[0] - 30:
                nx = self.ids.graph_canvas.size[0] - 30

            if ny > self.ids.graph_canvas.size[1] - 30:
                ny = self.ids.graph_canvas.size[1] - 30

            n = NodeWidget(maxid, [nx, ny])
            self.ids.graph_canvas.add_widget(n)
            return True
        else:
            return super().on_touch_down(touch)

    def text_event(self, event, text):
        graphManager.parse_graph_data(text)

class GraphGeneratorApp(App):
    def build(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand') # disable multi-touch emulation
        mainViewWidget = MainViewWidget()

        mainViewWidget.ids.input_nodes.bind(text=mainViewWidget.text_event)

        return mainViewWidget
