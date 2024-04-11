class Graph:
    def __init__(self, size):
        self.size = size
        self.adjacency_matrix = [[0] * size for _ in range(size)]
        self.vertices = [''] * size

    def add_vertex(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertices[vertex] = data

    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adjacency_matrix[u][v] = 1
            self.adjacency_matrix[u][v] = 1

    def print(self):
        print('ADJ_MATRIX:')
        for row in self.adjacency_matrix:
            print(' '.join(map(str, row)))
        for vertex, data in enumerate(self.vertices):
            print(f'Vertex {vertex}: {data}')


g = Graph(4)
g.add_vertex(0, 'A')
g.add_vertex(1, 'B')
g.add_vertex(2, 'C')
g.add_vertex(3, 'D')
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.print()
