def dijkstra(graph, start):
    import heapq

    distance = {}
    previous = {}
    heap = []

    for vertex in graph:
        distance[vertex] = float('inf')
        previous[vertex] = None
    distance[start] = 0
    heap.append((0, start))

    while heap:
        vertex_dist, vertex_name = heapq.heappop(heap)
        for neighbour_dist, neighbour_name in graph[vertex_name]:
            new_dist = distance[vertex_name] + neighbour_dist
            if new_dist < distance[neighbour_name]:
                distance[neighbour_name] = new_dist
                previous[neighbour_name] = vertex_name
                heapq.heappush(heap, (new_dist, neighbour_name))

    return distance, previous


def main():
    from pprint import pprint

    graph = {
        'a': [(2, 'b')],
        'b': [(1, 'c'), (5, 'd')],
        'c': [(1, 'd')],
        'd': []
    }
    pprint(dijkstra(graph, 'b'))


if __name__ == '__main__':
    main()
