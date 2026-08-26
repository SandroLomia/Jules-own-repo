import unittest
from topological_sort import Graph

class TestTopologicalSort(unittest.TestCase):

    def test_standard_dag(self):
        g = Graph()
        g.add_edge(5, 2)
        g.add_edge(5, 0)
        g.add_edge(4, 0)
        g.add_edge(4, 1)
        g.add_edge(2, 3)
        g.add_edge(3, 1)

        result = g.topological_sort()
        # Verify valid ordering
        # For a valid topological sort, if edge (u, v) exists, u must appear before v in result
        self.assertEqual(len(result), 6)

        index_map = {node: i for i, node in enumerate(result)}
        self.assertTrue(index_map[5] < index_map[2])
        self.assertTrue(index_map[5] < index_map[0])
        self.assertTrue(index_map[4] < index_map[0])
        self.assertTrue(index_map[4] < index_map[1])
        self.assertTrue(index_map[2] < index_map[3])
        self.assertTrue(index_map[3] < index_map[1])

    def test_empty_graph(self):
        g = Graph()
        self.assertEqual(g.topological_sort(), [])

    def test_disconnected_graph(self):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        # No edges
        result = g.topological_sort()
        self.assertEqual(set(result), {'A', 'B', 'C'})
        self.assertEqual(len(result), 3)

    def test_graph_with_cycle_raises_value_error(self):
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A') # Creates a cycle

        with self.assertRaises(ValueError):
            g.topological_sort()

    def test_graph_with_self_loop_raises_value_error(self):
        g = Graph()
        g.add_edge('A', 'A') # Self loop

        with self.assertRaises(ValueError):
            g.topological_sort()

    def test_linear_graph(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 4)

        self.assertEqual(g.topological_sort(), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
