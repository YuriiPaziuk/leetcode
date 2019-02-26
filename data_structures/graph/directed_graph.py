class DirectedGraph:

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
                result.add(tuple((vertex, neighbour)))
        return result

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph.update({vertex: set()})

    def add_edge(self, edge):
        vertex1, vertex2 = tuple(edge)
        self.graph[vertex1].add(vertex2)

    def neighbours(self, vertex):
        assert vertex in self.graph, vertex
        return self.graph[vertex]


def main():
    # Simple:
    graph1 = {
        "a": ["b", "c", "d"],
        "b": [],
        "c": ["d"],
        "d": []
    }

    # 2 components
    graph2 = {
        "a": ["b", "c", "d"],
        "b": [],
        "c": ["d"],
        "d": [],
        "e": ["g", "f"],
        "g": [],
        "f": []
    }

    # cycle
    graph3 = {
        "a": ["b", "c", "d"],
        "b": [],
        "c": ["d", "e"],
        "d": [],
        "e": ["g", "f"],
        "g": ["c"],
        "f": []
    }

    from pprint import pprint

    for g in [graph1, graph2, graph3]:
        graph = DirectedGraph(g)
        pprint(g)
        pprint(sorted(graph.vertices()))
        pprint(sorted(graph.edges()))


if __name__ == '__main__':
    main()
