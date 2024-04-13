class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end='-')
        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex):
        visited = [False] * self.size
        start = self.vertex_data.index(start_vertex)
        self.dfs_util(start, visited)


g = Graph(10)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
g.add_vertex_data(7, 'H')
g.add_vertex_data(8, 'I')
g.add_vertex_data(9, 'E')

g.add_edge(0, 1)  # A - B
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - E
g.add_edge(1, 0)  # B - A
g.add_edge(1, 3)  # B - D
g.add_edge(2, 0)  # C - A
g.add_edge(2, 5)  # C - F
g.add_edge(2, 6)  # C - G
g.add_edge(2, 8)  # C - I
g.add_edge(8, 7)  # I - H
g.add_edge(7, 9)  # H - E

g.print_graph()

print("\nDepth First Search starting from vertex A:")
g.dfs('A')


