class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0] * self.size for _ in range(size)]
        self.vertices = [''] * size

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertices[vertex] = data

    def print(self):
        print("ADJ_MATRIX:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print('Data vertex:')
        for vertex, data in enumerate(self.vertices):
            print(f'vertex:{vertex}:{data}')

    def bfs(self, start_vertex):
        queue = [self.vertices.index(start_vertex)]
        visited = [False] * self.size
        visited[queue[0]] = True
        while queue:
            current_vertex = queue.pop(0)
            print(self.vertices[current_vertex], end='-')
            for i in range(self.size):
                if self.adj_matrix[i][current_vertex] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True


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
g.add_vertex_data(9, 'K')
g.add_edge(0, 1)
g.add_edge(0, 2)

g.add_edge(0, 4)

g.add_edge(0, 9)

g.add_edge(1, 3)

g.add_edge(2, 5)

g.add_edge(2, 6)

g.add_edge(2, 8)

g.add_edge(5, 6)

g.add_edge(8, 7)

g.add_edge(7, 4)

g.print()

print("\nBreadth First Search starting from vertex A:")
g.bfs('A')

# Python
