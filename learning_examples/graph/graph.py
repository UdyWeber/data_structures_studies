class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex in self.adjacency_list:
            return False

        self.adjacency_list[vertex] = []
        return True

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return False

        for edged_vertex in self.adjacency_list[vertex]:
            self.adjacency_list[edged_vertex].remove(vertex)

        del self.adjacency_list[vertex]
        return True

    def add_edge(self, first_vertex, second_vertex):
        vertexes = self.adjacency_list.keys()

        if first_vertex not in vertexes or second_vertex not in vertexes:
            return False

        self.adjacency_list[first_vertex].append(second_vertex)
        self.adjacency_list[second_vertex].append(first_vertex)

        return True

    def remove_edge(self, first_vertex, second_vertex):
        vertexes = self.adjacency_list.keys()

        if first_vertex not in vertexes or second_vertex not in vertexes:
            return False

        try:
            self.adjacency_list[first_vertex].remove(second_vertex)
            self.adjacency_list[second_vertex].remove(first_vertex)
        except ValueError:
            return False

        return True

    def print_graph(self):
        for k, v in self.adjacency_list.items():
            print(f"Vertex {k}: edges {v}")


if __name__ == '__main__':
    g = Graph()
    g.add_vertex("Robson")
    g.add_vertex("Cleison")
    g.add_vertex("C")

    g.add_edge("Robson", "Cleison")
    g.add_edge("Cleison", "D")
    g.print_graph()

    g.remove_edge("C", "Cleison")
    print(g.remove_edge("D", "Z"))
    g.remove_vertex("Robson")

    g.print_graph()
