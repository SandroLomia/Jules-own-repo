class DependencyResolver:
    """
    A utility class for resolving dependencies using Topological Sort (Kahn's Algorithm).
    It can detect circular dependencies and properly handle complex and linear dependency graphs.
    """

    def __init__(self):
        # Maps an item to a list of items that depend on it
        self.graph = {}
        # Maps an item to the number of dependencies it has (in-degree)
        self.in_degree = {}

    def add_node(self, node):
        """Adds a node to the graph if it doesn't already exist."""
        if node not in self.graph:
            self.graph[node] = []
            self.in_degree[node] = 0

    def add_dependency(self, item, dependency):
        """
        Declares that `item` depends on `dependency`.
        This means `dependency` must be resolved before `item`.
        """
        # Ensure both items exist in the graph
        self.add_node(item)
        self.add_node(dependency)

        # In our graph, the edge goes from `dependency` -> `item`
        self.graph[dependency].append(item)

        # Increase the in-degree of `item` because it has a new dependency
        self.in_degree[item] += 1

    def resolve(self):
        """
        Resolves the dependencies and returns a valid resolution order.
        Raises ValueError if a circular dependency is detected.
        """
        # Find all nodes with no dependencies (in-degree == 0)
        queue = [node for node in self.in_degree if self.in_degree[node] == 0]

        resolved_order = []

        while queue:
            # Pop a node that has all its dependencies resolved
            current = queue.pop(0)
            resolved_order.append(current)

            # For all items that depend on `current`, reduce their in-degree
            for neighbor in self.graph[current]:
                self.in_degree[neighbor] -= 1
                # If they now have 0 dependencies left to resolve, add them to queue
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If the resolved order doesn't contain all nodes, there is a cycle
        if len(resolved_order) != len(self.in_degree):
            raise ValueError("Circular dependency detected.")

        return resolved_order
