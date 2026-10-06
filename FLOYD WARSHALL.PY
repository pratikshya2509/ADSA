def floyd_warshall(graph, n):
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (dist[i][k] != float('inf') and
                    dist[k][j] != float('inf') and
                    dist[i][k] + dist[k][j] < dist[i][j]):

                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")
print("Use INF for no direct edge.")

for i in range(n):
    row = input().split()
    converted_row = []

    for value in row:
        if value.upper() == "INF":
            converted_row.append(float('inf'))
        else:
            converted_row.append(int(value))

    graph.append(converted_row)

dist = floyd_warshall(graph, n)

print("Shortest distance matrix:")

for i in range(n):
    for j in range(n):
        if dist[i][j] == float('inf'):
            print("INF", end="\t")
        else:
            print(dist[i][j], end="\t")
    print()
