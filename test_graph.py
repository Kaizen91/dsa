import unittest
#from graph import Graph
from quiz import Graph
from collections import namedtuple

Edge = namedtuple('Edge', ['v', 'weight'])

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph([0,1,2,3,4,5])
        self.graph._edges[0] = [Edge(1, 2), Edge(4, 2)]
        self.graph._edges[1] = [Edge(2, 1), Edge(4, 3)]
        self.graph._edges[2] = [Edge(3, 2), Edge(5, 7)]
        self.graph._edges[3] = [Edge(5, 3)]
        self.graph._edges[5] = [Edge(4, 4)]

    def test_bfs(self):
        correct = [0,1,2,5]
        solution1 = self.graph.bfs(0,5)
        self.assertEqual(solution1, correct)
        solution2 = self.graph.bfs(5,0)
        self.assertIsNone(solution2)

    def test_dfs(self):
        correct = [0,1,2,3,5]
        solution1 = self.graph.dfs(0,5)
        self.assertEqual(solution1, correct)
        solution2 = self.graph.dfs(5,0)
        self.assertEqual(solution2, [])

    def test_dijkstra(self):
        correct = [0,1,2,3,5]
        solution1 = self.graph.dijkstra(0,5)
        self.assertEqual(solution1, correct)
        solution2 = self.graph.dijkstra(5,0)
        self.assertIsNone(solution2)

if __name__ == '__main__':
    unittest.main()
