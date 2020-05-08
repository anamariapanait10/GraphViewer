from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from globals import globals

import os

class OpenSaveWidget(GridLayout):

    mode = StringProperty()

    def __init__(self, mode='Open'):
        super().__init__()
        self.mode = mode

    def closePopup(self):
        globals.openSaveDialog.dismiss()

    def on_select_file(self):
        globals.openSaveDialog.content.ids.path_input.text = globals.openSaveDialog.content.ids.fc.selection and globals.openSaveDialog.content.ids.fc.selection[0] or ''


    def on_opensave(self):
        self.closePopup()
        if self.mode == 'Open':
            self.load(globals.openSaveDialog.content.ids.fc.path, globals.openSaveDialog.content.ids.fc.selection)
        if self.mode == 'Save':
            self.save(globals.openSaveDialog.content.ids.path_input.text)

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            text = stream.read()
            lines = text.splitlines(keepends=True)
            if lines[0].startswith('type_1'):
                globals.input_drop_down_list.ids.listOfEdges_btn.on_press()
            elif lines[0].startswith('type_2'):
                globals.input_drop_down_list.ids.adjacencyList_btn.on_press()
            elif lines[0].startswith('type_3'):
                globals.input_drop_down_list.ids.adjacencyMatrix_btn.on_press()
            elif lines[0].startswith('type_4'):
                globals.input_drop_down_list.ids.costMatrix_btn.on_press()

            lines = lines[1:]
            globals.main_view_widget.ids.input_text.text = ''.join(lines)

    def save(self, filename):
        with open(filename, 'w') as stream:
            text = ''
            if globals.edge_list_input_btn:
                text += 'type_1'
            elif globals.adjacency_list_input_btn:
                text += 'type_2'
            elif globals.adjacency_matrix_input_btn:
                text += 'type_3'
            else:
                text += 'type_4'
            text += '\n'
            text += globals.main_view_widget.ids.input_text.text
            stream.write(text)