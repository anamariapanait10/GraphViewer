from kivy.properties import ObjectProperty
from kivy.properties import ListProperty


graphManager = None
mainViewWidget = None

inputDropDownList = None
algDropDownList = None
changeColorDropDownList = None

popupWindow = ObjectProperty()
popupWidget = None

NodeWidgetBackgroundColor = ListProperty()
NodeWidgetColor = ListProperty()
EdgeWidgetColor = ListProperty()

radiusOfNodeWidget = 50
lengthOfEdgeWidget = 50
minimumDistanceBetweenNodeWidgets = 5

forces = True

listOfEdgesBtn = True
adjacencyListBtn = False
adjacencyMatrixBtn = False
costMatrixBtn = False

colors = { 'white': [0.9, 0.9, 0.9, 1], 'black': [0, 0, 0, 1], 'red': [1, 0, 0, 1], 'yellow': [0.937, 0.87, 0.32, 1],
           'orange': [1, 0.62, 0.088, 1], 'blue': [0.199, 0.7, 1, 1], 'purple': [0.75, 0.5, 1, 1],
           'green': [0.099, 1, 0.66, 1], 'pink': [1, 0.5, 0.875, 1] }


def binarySearch(arr, l, r, value):

    if r >= l:  # Check base case
        mid = (r + l) // 2

        if int(arr[mid].Id) == value:   # If element is present at the middle itself
            return mid

        elif int(arr[mid].Id) > value:  # If element is smaller than mid, then it can only be present in left subarray
            return binarySearch(arr, l, mid - 1, value)

        else:    # Else the element can only be present in right subarray
            return binarySearch(arr, mid + 1, r, value)

    else:
        return -1  # Element is not present in the array

