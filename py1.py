class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.vertexx = [''] * size

    def add_egde(self, u, v):
        if 0 <= u < self.size and 0 <= u < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1

    def add_vertex(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertexx[vertex] = data

    def print(self):
        print('ADJ_MATRIX')
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print('\nVertex Data:')
        for vertex, data in enumerate(self.vertexx):
            print(f'vertex{vertex}: {data}')


a = Graph(4)
a.add_vertex(0, 'A')
a.add_vertex(1, 'B')
a.add_vertex(2, 'C')
a.add_vertex(3, 'D')
a.add_vertex(4, 'E')
a.add_egde(0, 1)  # A-B
a.add_egde(0, 2)  # A-C
a.add_egde(0, 3)  # A-D
a.add_egde(1, 2)  # C-Bs
a.print()
