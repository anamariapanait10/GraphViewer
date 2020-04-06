from kivy.uix.widget import Widget

maxid = 0

def getmaxid():
    global maxid
    #maxid += 1
    return str(maxid)

class NodeWidget(Widget):

    def __init__(self, nr, pos):
        super().__init__()
        self.size = [50, 50]
        self.pos = pos
        self.nr = nr  # this is the id of the node
        self.force = (0, 0)

    def getId(self):
        return self.nr

    def getmaxid(self):
        global maxid
        maxid += 1
        return str(maxid)