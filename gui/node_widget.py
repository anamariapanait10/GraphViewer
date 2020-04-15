from kivy.properties import StringProperty
from kivy.uix.behaviors import DragBehavior
from kivy.uix.widget import Widget
from gui import globals


def binarySearch(arr, l, r, x):

    # Check base case
    if r >= l:
        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid].nr == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid].nr > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


def getnextid():
    nextid = 1

    globals.graphManager.nodeWidgets.sort(key=lambda node: node.nr)
    # print(globals.graphManager.nodeWidgets)

    while True:
        result = binarySearch(globals.graphManager.nodeWidgets, 0, len(globals.graphManager.nodeWidgets) - 1, nextid)

        if result == -1: # means that it does not exists a node with that id
            return nextid

        nextid += 1


class NodeWidget(Widget):

    nodeId = StringProperty()

    def __init__(self, nr, pos):
        super().__init__()
        self.size = [50, 50]
        self.pos = pos
        self.nr = nr  # this is the id of the node
        self.nodeId = str(nr)
        self.force = (0, 0)

    def on_touch_down(self, touch):
        pass

    def on_touch_move(self, touch):
        pass

    def on_touch_up(self, touch):
        pass

    def getId(self):
        return self.nr

    def getNextId(self):
        return getnextid()