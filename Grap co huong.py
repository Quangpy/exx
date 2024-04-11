class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.vertices = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= u < self.size:
            self.adj_matrix[u][v] = weight  # đồ thị có hướng có thêm trọng số weight

    def add_vertex(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertices[vertex] = data

    def print(self):
        print('ADJ_Matrix:')
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        for vertex, data in enumerate(self.vertices):
            print(f'vertex{vertex}:{data}')


g = Graph(4)
g.add_vertex(0, 'A')
g.add_vertex(1, 'B')
g.add_vertex(2, 'C')
g.add_vertex(3, 'D')
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 2)
g.add_edge(3, 0, 4)
g.add_edge(2, 1, 1)
g.print()
