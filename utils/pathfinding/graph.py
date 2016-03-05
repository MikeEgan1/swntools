class Graph:
    def __init__(self):
        self.edges = {}
        self.even_neighbors = [(1,0), (-1,0), (0,1), (0,-1), (1,-1),(-1,-1)]
        self.odd_neighbors = [(1,0), (-1,0), (0,1), (0,-1), (-1,1),(1,1)]

    def get_neighbors(self, id):
        return self.find_neighbors(id)

    def find_neighbors(self, id):
        neighbors = []

        if id[0] % 2 == 0:
            neighbor_set = self.even_neighbors
        else:
            neighbor_set = self.odd_neighbors

        for coords in neighbor_set:
            neighbors.append([id[0] + coords[0], id[1] + coords[1]])


        return neighbors