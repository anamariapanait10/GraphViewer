from kivy.properties import ObjectProperty, ListProperty


graph_manager = None
main_view_widget = None

input_drop_down_list = None
algorithms_drop_down_list = None
change_color_drop_down_list = None

popup_window = ObjectProperty()
popup_widget = None
error_popup_widget = None

node_radius = 25
edge_length = 50
minimum_distance_between_nodes = 5

forces = True

edge_list_input_btn = True
adjacency_list_input_btn = False
adjacency_matrix_input_btn = False
cost_matrix_input_btn = False

colors = { 'white': [0.9, 0.9, 0.9, 1], 'black': [0, 0, 0, 1], 'red': [1, 0, 0, 1], 'yellow': [0.937, 0.87, 0.32, 1],
           'orange': [1, 0.62, 0.088, 1], 'blue': [0.199, 0.7, 1, 1], 'purple': [0.75, 0.5, 1, 1],
           'green': [0.099, 1, 0.66, 1], 'pink': [1, 0.5, 0.875, 1] }

node_background_color = colors['white']
node_border_color = colors['black']
edge_color = colors['black']


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

