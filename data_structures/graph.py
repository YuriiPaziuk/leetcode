class Graph:

    def __init__(self, graph_dict=None):
        """
        :param graph_dict: dict(vertex: set(vertices))
        :return:
        """
        import collections
        self.graph_dict = collections.defaultdict(set)
        self.graph_dict.update(graph_dict)

    def nodes(self):
        """Return the nodes of the graph as a set"""
        return set(self.graph_dict.keys())

    def edges(self):
        """Return edges of the graph as a set of tuples"""
        result = set()
        for node, neighbours in self.graph_dict.items():
            for neighbour in neighbours:
                result.add(tuple(sorted((node, neighbour))))
        return result

    def add_edge(self, edge):
        """Add a new edge. edge is set, tuple, or list of two vertices"""
        node1, node2 = tuple(edge)
        self.graph_dict[node1].add(node2)
        self.graph_dict[node2].add(node1)

    def add_node(self, node):
        """Add a new vertex if it doesn't exist"""
        if node not in self.graph_dict:
            self.graph_dict.update({node: {}})

    def find_path(self, start, end):
        assert start in self.graph_dict
        assert end in self.graph_dict

        def dfs(start, end, path=None):
            if not path: path = []
            path = path + [start]
            if start == end: return path
            for node in self.graph_dict[start]:
                if node not in path:
                    next_path = dfs(node, end, path)
                    if next_path: return next_path
            return None

        return dfs(start, end)

    def connected_to(self, node):
        assert node in self.graph_dict

        import queue
        q = queue.deque()
        q.append(node)
        result = set()
        while q:
            current_node = q.pop()
            result.add(current_node)
            for t in self.graph_dict[current_node]:
                if t not in result:
                    q.append(t)
        return result


def main():
    from pprint import pprint
    g = {'a': {'d'},
         'b': {'c'},
         'c': {'d', 'b', 'e', 'c'},
         'd': {'c', 'a'},
         'e': {'c'},
         'f': {}}
    graph = Graph(g)
    """
    graph.add_edge(('e', 'b'))
    graph.add_node('g')

    pprint(graph.edges())
    pprint(graph.nodes())
    """
    pprint(graph.graph_dict)
    pprint(graph.find_path('a', 'b'))
    pprint(graph.connected_to('d'))
    print(graph.nodes())
    print(graph.edges())


if __name__ == '__main__':
    main()
