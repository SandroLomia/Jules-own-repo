from collections import defaultdict, deque

class Graph:
    def __init__(self):
        """Initializes an empty graph for topological sorting."""
        self.adj_list = defaultdict(list)
        self.in_degree = defaultdict(int)
        self.vertices = set()

    def add_vertex(self, u):
        """Adds a vertex to the graph."""
        self.vertices.add(u)
        # Ensure it exists in the in_degree map even if it has no incoming edges
        if u not in self.in_degree:
            self.in_degree[u] = 0

    def add_edge(self, u, v):
        """Adds a directed edge from vertex u to vertex v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
        self.in_degree[v] += 1

    def topological_sort(self):
        """
        Performs a topological sort using Kahn's algorithm.
        Returns a list of vertices in topologically sorted order.
        Raises ValueError if a cycle is detected (i.e., graph is not a DAG).
        """
        # Copy the in_degree map to avoid mutating the graph state
        in_degree = self.in_degree.copy()

        # Find all vertices with an in-degree of 0
        queue = deque([v for v in self.vertices if in_degree[v] == 0])

        sorted_order = []

        while queue:
            # Pop a vertex from the queue with 0 in-degree
            u = queue.popleft()
            sorted_order.append(u)

            # Decrease the in-degree of all its neighbors
            for v in self.adj_list[u]:
                in_degree[v] -= 1
                # If a neighbor's in-degree becomes 0, add it to the queue
                if in_degree[v] == 0:
                    queue.append(v)

        # Check if we were able to process all vertices
        if len(sorted_order) != len(self.vertices):
            raise ValueError("Cycle detected in graph; topological sort is not possible.")

        return sorted_order
