class UndirectedGraph:

    def __init__(self, graph_dict=None):
        from collections import defaultdict
        self.graph = defaultdict(set)
        if graph_dict: self.graph.update(graph_dict)

    def vertices(self):
        result = set()
        for vertex, neighbours in self.graph.items():
            result.add(vertex)
            result.update(neighbours)
        return result

    def edges(self):
        result = set()
        for vertex, neighbours in self.graph.items():
            for neighbour in neighbours:
                result.add(tuple(sorted((vertex, neighbour))))
        return result

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph.update({vertex: set()})

    def add_edge(self, edge):
        vertex1, vertex2 = tuple(edge)
        self.graph[vertex1].add(vertex2)
        self.graph[vertex2].add(vertex1)

    def neighbours(self, vertex):
        assert vertex in self.graph
        return self.graph[vertex]


def main():
    from pprint import pprint
    g = {'a': {'d'},
         'b': {'c'},
         'c': {'d', 'b', 'e', 'c'},
         'd': {'c', 'a'},
         'e': {'c'},
         'f': set()}
    graph = UndirectedGraph(g)

    graph.add_edge(('e', 'b'))
    graph.add_vertex('g')

    pprint(sorted(graph.edges()))
    pprint(sorted(graph.vertices()))

    pprint(graph.graph)


if __name__ == '__main__':
    main()
