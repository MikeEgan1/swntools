from utils.pathfinding.map import Map

class HexMap(Map):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = []
        self.even_neighbors = [(1,0), (-1,0), (0,1), (0,-1), (1,-1), (-1,-1)]
        self.odd_neighbors = [(1,0), (-1,0), (0,1), (0,-1), (-1,1), (1,1)]

        self.build_map()

    def build_map(self):
        for i in xrange(self.height):
            for j in xrange(self.width):
                self.map.append((j,i))

    def get_edges(self):
        edges = {}

        for coord in self.map:
            edges[coord] = self.get_neighbors(coord)

        return edges


    def get_neighbors(self, coords):
        neighbors = []
        if coords[0] % 2 == 0:
            neighbor_set = self.even_neighbors
        else:
            neighbor_set = self.odd_neighbors

        for item in neighbor_set:
            neighbor = (coords[0] + item[0], coords[1] + item[1])

            if self.check_bounds(neighbor):
                neighbors.append(neighbor)

        return neighbors

    def check_bounds(self, neighbor):
        return 0 <= neighbor[0] < self.width and 0 <= neighbor[1] < self.height

    def get_neighbors_for_location(self, coord):
        return self.neighbors[coord]

    def print_map(self):
        print self.map


def main():
    map = HexMap(10, 8)
    edges = map.get_edges()

    print edges[(0,1)]

if __name__ == "__main__":
    main()
