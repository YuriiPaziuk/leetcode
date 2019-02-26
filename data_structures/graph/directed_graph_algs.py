from directed_graph import DirectedGraph

class DirectedGraphAlgs(DirectedGraph):

    def __init__(self, graph_dict=None):
        super().__init__(graph_dict)

    def distances_bfs(self, start):
        """Find distances from start vertex to all vertices"""
        from queue import deque

        assert start in self.graph

        distance = {vertex: None for vertex in self.vertices()}
        distance[start] = 0

        queue = deque()
        queue.append(start)

        while queue:
            current_vertex = queue.pop()
            for neighbour in self.neighbours(current_vertex):
                if distance[neighbour] is None:
                    queue.append(neighbour)
                    distance[neighbour] = distance[current_vertex] + 1

        return distance

    def shortest_path_tree__bfs(self, start):
        """Find paths from start vertex to all vertices"""
        from queue import deque

        assert start in self.graph

        distance = {vertex: None for vertex in self.vertices()}
        distance[start] = 0

        previous = {vertex: None for vertex in self.vertices()}

        queue = deque()
        queue.append(start)

        while queue:
            current_vertex = queue.pop()
            for neighbour in self.neighbours(current_vertex):
                if distance[neighbour] is None:
                    queue.append(neighbour)
                    distance[neighbour] = distance[current_vertex] + 1
                    previous[neighbour] = current_vertex

        return previous

    def shortest_path(self, start, end):
        from queue import deque

        assert start in self.vertices()
        assert end in self.vertices()

        distances = self.distances_bfs(start)
        if distances[end] is None: return None

        previous = self.shortest_path_tree__bfs(start)
        path = deque()

        while end != start:
            path.appendleft(end)
            end = previous[end]

        return path


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
        graph = DirectedGraphAlgs(g)
        pprint(graph.distances_bfs('a'))
        pprint(graph.shortest_path_tree__bfs('a'))
        pprint(graph.shortest_path('a', 'd'))
        print('----------------------------------')


if __name__ == '__main__':
    main()
