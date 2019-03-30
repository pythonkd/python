import heapq

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


def init_dist(graph, s):
    distance = {}
    for i in graph:
        if i == s:
            distance[i] = 0
        else:
            distance[i] = float('inf')
    return distance


def dijkstra(graph, s):
    distance = init_dist(graph, s)
    seen = set()
    pq = []
    heapq.heappush(pq, (0, s))
    parent = {}
    while pq:
        dist, vertex = heapq.heappop(pq)
        seen.add(vertex)
        for w in graph[vertex]:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    distance[w] = dist + graph[vertex][w]
                    parent[w] = vertex
                    heapq.heappush(pq, (distance[w], w))

    return parent, distance


if __name__ == "__main__":
    parent, distance = dijkstra(graph, "A")
    print(parent, distance)