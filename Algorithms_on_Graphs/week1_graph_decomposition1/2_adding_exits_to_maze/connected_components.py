#Uses python3

import sys


def number_of_components(adj):

    n = len(adj)
    visited = [False]*n
    result = 0

    def dfs(u) :
        visited[u] = True
        for v in adj[u] :
            if not visited[v] :
                dfs(v)

    for u in range(n) :
        if not visited[u] :
            dfs(u)
            result += 1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
