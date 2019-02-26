class DirectedGraph:

    def __init__(self, graph_dict=None):
        import collections
        self.graph = collections.defaultdict(set)
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


class DirectedGraphOperations(DirectedGraph):

    def __init__(self, graph_dict=None):
        super().__init__(graph_dict)

    def connected_to(self, start):

        def dfs(start):
            visited.add(start)
            for neighbour in self.graph[start]:
                if neighbour not in visited:
                    dfs(neighbour)

        visited = set()
        dfs(start)
        visited.remove(start)
        return visited

    def topological_sort(self):

        def visit(node):
            node_state = state.get(node, None)
            if node_state == BLACK: return
            if node_state == GREY: raise ValueError('Cycle, not a DAG')
            state[node] = GREY
            for neighbour in self.graph[node]:
                visit(neighbour)
            state[node] = BLACK
            nodes.discard(node)
            order.appendleft(node)

        from collections import deque

        order = deque()
        state = dict()
        nodes = set(self.vertices())
        GREY, BLACK = 0, 1  # a temporary and a permanent markers

        while nodes:
            visit(nodes.pop())
        return order

    def topological_sort_unsafe(self):
        """ Not checking for cycles"""
        def dfs(node):
            visited.add(node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
            order.appendleft(node)
            nodes.discard(node)

        from collections import deque
        visited = set()
        order = deque()
        nodes = set(self.vertices())
        while nodes:
            dfs(nodes.pop())
        return order


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
        "e": ["g", "f", "q"],
        "g": ["c"],
        "f": []
    }

    from pprint import pprint

    for g in [graph1, graph2, graph2]:
        graph = DirectedGraphOperations(g)
        #pprint(graph.vertices())
        #pprint(graph.edges())
        #pprint(graph.connected_to('a'))
        pprint(graph.topological_sort_unsafe())


if __name__ == '__main__':
    main()
