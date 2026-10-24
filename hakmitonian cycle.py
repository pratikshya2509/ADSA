def hamiltonian(n, graph):
    path = [-1] * n
    path[0] = 0

    def solve(pos):
        if pos == n:
            if graph[path[n - 1]][path[0]] == 1:
                print("Hamiltonian Cycle:", path + [path[0]])
                return True
            return False

        for v in range(1, n):
            if graph[path[pos - 1]][v] == 1 and v not in path:
                path[pos] = v

                if solve(pos + 1):
                    return True

                path[pos] = -1

        return False

    if not solve(1):
        print("No Hamiltonian Cycle exists.")


n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix row by row:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

hamiltonian(n, graph)
