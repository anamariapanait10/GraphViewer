from kivy.properties import ObjectProperty
from kivy.properties import ListProperty

colors = { 'white': [0.9, 0.9, 0.9, 1], 'black': [0, 0, 0, 1], 'red': [1, 0, 0, 1], 'yellow': [0.937, 0.87, 0.32, 1],
           'orange': [1, 0.62, 0.088, 1], 'blue': [0.199, 0.7, 1, 1], 'purple': [0.75, 0.5, 1, 1],
           'green': [0.099, 1, 0.66, 1], 'pink': [1, 0.5, 0.875, 1] }

graphManager = None
mainViewWidget = None
inputDropDownList = None
algDropDownList = None
popUpWindow = ObjectProperty()
popUpWidget = None
changeColorDropDownList = None
NodeWidgetBackgroundColor = ListProperty()
NodeWidgetColor = ListProperty()
EdgeWidgetColor = ListProperty()
radiusOfNodeWidget = 50
lengthOfEdgeWidget = 50
minimumDistanceBetweenNodeWidgets = 5


