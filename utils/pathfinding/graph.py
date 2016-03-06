class Graph:
    def __init__(self):
        self.edges = {}

    def get_neighbors(self, id):
        return self.edges[id]
