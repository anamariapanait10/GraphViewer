
class GraphException(Exception):

    def __init__(self, text):
        self.message = text