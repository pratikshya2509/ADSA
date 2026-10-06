def dijkstra(graph, source):
    n = len(graph)

    distance = [float('inf')] * n
    visited = [False] * n

    distance[source] = 0

    for _ in range(n):
        u = -1
        minimum = float('inf')

        for i in range(n):
            if not visited[i] and distance[i] < minimum:
                minimum = distance[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if (not visited[v] and
                graph[u][v] != 0 and
                distance[u] + graph[u][v] < distance[v]):

                distance[v] = distance[u] + graph[u][v]

    return distance


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source vertex: "))

distance = dijkstra(graph, source)

print("Shortest distances from source vertex", source)

for i in range(n):
    print(source, "to", i, "=", distance[i])
