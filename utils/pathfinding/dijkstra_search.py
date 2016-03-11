from utils.pathfinding.priority_queue import PriorityQueue
from utils.pathfinding.graph import Graph
from utils.pathfinding.hexmap import HexMap

def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for location in graph.get_neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, location)
            if location not in cost_so_far or new_cost < cost_so_far[location]:
                cost_so_far[location] = new_cost
                frontier.put(location, new_cost)
                came_from[location] = current

    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def main():
    map = HexMap(10, 8)
    graph = Graph()
    graph.edges = map.get_edges()
    came_from, cost_so_far = dijkstra_search(graph, (0, 0), (7, 3))
    path = reconstruct_path(came_from, (0, 0), (7, 3))
    print path
    print len(path)


if __name__ == "__main__":
    main()