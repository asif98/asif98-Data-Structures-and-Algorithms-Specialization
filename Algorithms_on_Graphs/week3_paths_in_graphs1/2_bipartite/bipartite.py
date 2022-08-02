#Uses python3

import sys
import queue

def bipartite(adj):

    n = len(adj)
    visited = [False]*n

    def dfs(u, eps) :
        visited[u] = eps
        for v in adj[u] :
            if visited[v] == eps :
                return False
            elif visited[v] == False :
                if dfs(v, -eps) == False :
                    return False
        return True

    for u in range(n) :
        if visited[u] == False and dfs(u, 1) == False :
            #print(visited)
            return 0
    #print(visited)

    return 1

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
    print(bipartite(adj))
