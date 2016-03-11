from utils.pathfinding.dijkstra_search import dijkstra_search

class Grid:
    def __init__(self, map):
        self.map = map

    def calculate_distance(self, start, goal):
        dijkstra_search(self.map, start, goal)
