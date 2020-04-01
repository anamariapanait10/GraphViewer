import kivy
from kivy.app import App
from kivy.uix.widget import Widget

kivy.require('2.0.0')

maxid = 0

class NodeWidget(Widget):

    def __init__(self, nr, pos):
        super().__init__()
        self.pos = [pos[0] - 25, pos[1] - 27]
        self.nr = nr  # this is the id of the node

class MainViewWidget(Widget):
    def on_touch_down(self, touch):
        if self.ids.graph_canvas.collide_point(*touch.pos):
            global maxid
            maxid += 1
            n = NodeWidget(maxid, touch.pos)
            self.add_widget(n)


class GraphGeneratorApp(App):
    def build(self):
        mainViewWidget = MainViewWidget()

        return mainViewWidget