class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def get_neighbors(self, id):
        return self.edges[id]

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)