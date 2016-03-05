from unittest import TestCase
from utils.pathfinding.graph import Graph

class TestGraph(TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_get_odd_neighbors(self):
        neighbors = self.graph.get_neighbors([1,1])
        self.assertEqual(neighbors, [[2, 1], [0, 1], [1, 2], [1, 0], [0, 2], [2, 2]])