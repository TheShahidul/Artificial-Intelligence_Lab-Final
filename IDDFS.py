from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_limit(self, node, limit, visited, stack):
        if visited[node]:
            return False
        visited[node] = True
        if limit == 0:
            return True
        for neighbor in self.graph[node]:
            if self.dfs_limit(neighbor, limit - 1, visited, stack):
                if neighbor not in stack:
                    stack.append(neighbor)
                return True
        visited[node] = False
        return False

    def topological_sort_IDDFS(self):
        max_depth = len(self.graph)  # Maximum depth for IDDFS
        stack = []

        for depth in range(max_depth):
            visited = {node: False for node in self.graph}
            for node in self.graph:
                if not visited[node]:  # Only start DFS if the node has not been visited
                    self.dfs_limit(node, depth, visited, stack)

        return stack[::-1]  # Return in topological order (reverse of stack)


if __name__ == "__main__":
    g = Graph()

    graph_matrix = [
        [0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1]
    ]

    # Convert the matrix to an adjacency list and add edges to the graph
    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix[0])):
            if graph_matrix[i][j] == 1:
                g.add_edge(i, j)

    # Find the topological order using IDDFS
    top_order = g.topological_sort_IDDFS()
    print("Topological Order:", top_order)
