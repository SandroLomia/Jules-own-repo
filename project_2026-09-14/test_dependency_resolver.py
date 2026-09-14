import unittest
from dependency_resolver import DependencyResolver

class TestDependencyResolver(unittest.TestCase):

    def test_linear_dependency(self):
        resolver = DependencyResolver()
        resolver.add_dependency('B', 'A') # B depends on A
        resolver.add_dependency('C', 'B') # C depends on B

        result = resolver.resolve()
        self.assertEqual(result, ['A', 'B', 'C'])

    def test_complex_dependency(self):
        resolver = DependencyResolver()
        resolver.add_dependency('D', 'B')
        resolver.add_dependency('D', 'C')
        resolver.add_dependency('B', 'A')
        resolver.add_dependency('C', 'A')

        result = resolver.resolve()

        # 'A' must be first, 'D' must be last. 'B' and 'C' can be in any order.
        self.assertEqual(result[0], 'A')
        self.assertEqual(result[-1], 'D')
        self.assertIn(result[1], ['B', 'C'])
        self.assertIn(result[2], ['B', 'C'])
        self.assertNotEqual(result[1], result[2])

    def test_circular_dependency(self):
        resolver = DependencyResolver()
        resolver.add_dependency('B', 'A')
        resolver.add_dependency('C', 'B')
        resolver.add_dependency('A', 'C') # Circle: A -> B -> C -> A

        with self.assertRaises(ValueError) as context:
            resolver.resolve()

        self.assertTrue("Circular dependency detected" in str(context.exception))

    def test_isolated_nodes(self):
        resolver = DependencyResolver()
        resolver.add_node('A')
        resolver.add_node('B')
        resolver.add_node('C')

        result = resolver.resolve()

        # All nodes have 0 in-degree, they can be resolved in any order
        self.assertCountEqual(result, ['A', 'B', 'C'])

    def test_multiple_independent_graphs(self):
        resolver = DependencyResolver()
        resolver.add_dependency('B', 'A')
        resolver.add_dependency('Y', 'X')

        result = resolver.resolve()

        # A must come before B, X must come before Y
        self.assertTrue(result.index('A') < result.index('B'))
        self.assertTrue(result.index('X') < result.index('Y'))
        self.assertCountEqual(result, ['A', 'X', 'B', 'Y'])


if __name__ == '__main__':
    unittest.main()
