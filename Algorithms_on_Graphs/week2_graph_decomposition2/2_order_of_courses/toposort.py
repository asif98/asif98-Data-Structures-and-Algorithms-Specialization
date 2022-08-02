#Uses python3

import sys

def toposort(adj):
    n = len(adj)
    visited = [False] * n
    order = []

    def dfs(u):
        visited[u] = True
        for v in adj[u] :
            if not visited[v] :
                dfs(v)
        order.append(u)

    for u in range(n) :
        if not visited[u] :
            dfs(u)

    order.reverse()
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    # for x in adj:
    #     print(x )
    for x in order:
        print(x + 1, end=' ')
