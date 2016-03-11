from utils.pathfinding.graph import Graph
from utils.pathfinding.hexmap import HexMap
from utils.pathfinding.queue import Queue

def breadth_first_search(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print "Visiting {}".format(current)

        if current == goal:
            break

        for location in graph.get_neighbors(current):
            if not is_visited(visited, location):
                frontier.put(location)
                visited[location] = True

def is_visited(visited, coord):
    for visit in visited:
        if visit == coord:
            return True

    return False

def main():
    map = HexMap(10, 8)
    graph = Graph()
    graph.edges = map.get_edges()
    breadth_first_search(graph, (0, 0), (4, 5))


if __name__ == "__main__":
    main()