def min_key(key, mst_set, V):
    minimum = float('inf')
    min_index = -1

    for v in range(V):
        if not mst_set[v] and key[v] < minimum:
            minimum = key[v]
            min_index = v

    return min_index


def prim_mst(graph):
    V = len(graph)

    parent = [-1] * V
    key = [float('inf')] * V
    mst_set = [False] * V

    key[0] = 0

    for _ in range(V - 1):
        u = min_key(key, mst_set, V)
        mst_set[u] = True

        for v in range(V):
            if graph[u][v] != 0 and not mst_set[v] and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    print("Edge\tWeight")

    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])


V = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

prim_mst(graph)
