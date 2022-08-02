#Uses python3

import sys


def acyclic(adj):
    n = len(adj)
    visited = [False]*n
    ranks = [None]*n

    def dfs(u, rank) :
        ranks[u] = rank
        visited[u] = True
        for v in adj[u] :
            #print(v, ranks[v], rank)
            if visited[v] and ranks[v] != None and ranks[v] <= rank :
                return True
            elif dfs(v, rank+1) :
                return True
        ranks[u] = None
        return False

    for u in range(n) :
        if not visited[u] and dfs(u, 0) :
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
