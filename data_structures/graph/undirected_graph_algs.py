from undirected_graph import UndirectedGraph

class UndirectedGraphAlgs(UndirectedGraph):

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

        previous = {vertex: None for vertex in self.vertices()}

        queue = deque()
        queue.append(start)

        while queue:
            current_vertex = queue.pop()
            for neighbour in self.neighbours(current_vertex):
                if previous[neighbour] is None:
                    queue.append(neighbour)
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

    def parse_path(self, previous, start, end):
        import collections
        path = collections.deque()

        while end:
            path.appendleft(end)
            end = previous[end]

        return path

    def dfs(self, start, end):
        stack = []
        visited = set()

        stack.append(start)

        while stack:
            current = stack.pop()
            visited.add(current)
            if current == end:
                return True
            for neighbour in self.neighbours(current):
                if neighbour not in visited:
                    stack.append(neighbour)

        return False

    def dfs_path(self, start, end):
        stack = []
        visited = set()
        previous = dict()

        stack.append(start)
        previous[start] = None

        while stack:
            current = stack.pop()
            visited.add(current)
            if current == end:
                return self.parse_path(previous, start, end)
            for neighbour in self.neighbours(current):
                if neighbour not in visited:
                    stack.append(neighbour)
                    previous[neighbour] = current

        return []

    def bfs(self, start, end):
        import collections
        queue = collections.deque()
        visited = set()

        queue.append(start)

        while queue:
            current = queue.popleft()
            visited.add(current)
            if current == end:
                return True
            for neighbour in self.neighbours(current):
                if neighbour not in visited:
                    queue.append(neighbour)

        return False

    def bfs_path(self, start, end):
            import collections
            queue = collections.deque()
            visited = set()
            previous = dict()

            queue.append(start)
            previous[start] = None

            while queue:
                current = queue.popleft()
                visited.add(current)
                if current == end:
                    return self.parse_path(previous, start, end)
                for neighbour in self.neighbours(current):
                    if neighbour not in visited:
                        queue.append(neighbour)
                        previous[neighbour] = current

            return []

def main():
    from pprint import pprint

    g = {'a': {'d'},
         'b': {'c'},
         'c': {'d', 'b', 'e', 'c'},
         'd': {'c', 'a'},
         'e': {'c'},
         'f': set()}

    graph = UndirectedGraphAlgs(g)
    #pprint(graph.distances_bfs('a'))
    #pprint(graph.shortest_path_tree__bfs('a'))
    #pprint(graph.shortest_path('a', 'e'))
    pprint(graph.dfs_path('a', 'b'))
    pprint(graph.bfs_path('a', 'b'))


if __name__ == '__main__':
    main()
