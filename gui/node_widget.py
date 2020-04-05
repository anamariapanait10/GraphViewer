from kivy.uix.widget import Widget

maxid = 0

class NodeWidget(Widget):

    def __init__(self, nr, pos):
        super().__init__()
        self.size = [50, 50]
        self.pos = pos
        self.nr = nr  # this is the id of the node
        self.force = (0, 0)