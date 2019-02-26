"""
Word ladder puzzle: transform the word FOOL into the word SAGE.
The change must occur gradually one letter at a time. At each step
you must transform one word into another word, you are not allowed
to transform a word into a non-word. One possible solution of the
puzzle is:

FOOL
POOL
POLL
POLE
PALE
SALE
SAGE
"""


class Graph:

    def __init__(self, graph_dict=None):
        import collections
        self.graph = collections.defaultdict(set)
        if graph_dict:
            self.graph.update(graph_dict)

    def vertices(self):
        return set(self.graph.keys())

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


class WordLadderGraph(Graph):

    def __init__(self, filename, word_len):
        super().__init__()
        self.words = self.load_words_of_len_n(filename, word_len)
        buckets = self.build_buckets(self.words)
        self.build_graph(buckets)

    def load_words_of_len_n(self, filename, n):
        words = []
        with open(filename) as file:
            for line in file:
                line = line.strip().lower()
                if len(line) == n:
                    words.append(line)
        return words

    def build_buckets(self, words):
        from collections import defaultdict
        d = defaultdict(set)
        for word in words:
            for i in range(len(word)):
                d[word[:i] + '_' + word[i+1:]].add(word)
        return d

    def build_graph(self, buckets):
        buckets = {vertex: neighbours for vertex,
                   neighbours in buckets.items() if len(neighbours) > 1}
        for bucket in buckets:
            for word1 in buckets[bucket]:
                for word2 in buckets[bucket]:
                    if word1 != word2:
                        self.add_edge((word1, word2))

    def path(self, start, end):
        import collections
        q = collections.deque()
        visited = set()
        previous = dict()
        q.append(start)
        visited.add(start)
        current = start
        while q:
            current = q.popleft()
            if current == end:
                break
            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour)
                    previous[neighbour] = current
        if current == end:
            result = collections.deque()
            t = current
            while t in previous:
                result.appendleft(t)
                t = previous[t]
            result.appendleft(t)
            return result
        else:
            return 'not found'


def main():
    from pprint import pprint

    start, end = 'fool', 'sage'
    assert len(start) == len(end)

    graph = WordLadderGraph('linuxwords.txt', len(start))
    pprint(graph.graph)
    print('Number of vertices: ', len(graph.vertices()))
    print('Number of edges: ', len(graph.edges()))
    print(graph.path(start, end))


def test_graph():
    from pprint import pprint
    graph = Graph()
    vertices = {'c', 'a', 'e', 'f', 'd', 'b'}
    edges = {('c', 'c'), ('c', 'e'), ('a', 'd'), ('c', 'd'), ('b', 'c')}
    for vertex in vertices:
        graph.add_vertex(vertex)
    pprint(graph.graph)
    for edge in edges:
        graph.add_edge(edge)
    pprint(graph.graph)
    print(graph.vertices())
    print(graph.edges())


if __name__ == '__main__':
    main()
