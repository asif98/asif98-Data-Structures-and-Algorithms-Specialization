#Uses python3

import sys
from collections import deque

def distance(adj, s, t):
    #write your code here
    queue = deque([s])
    visited = [False]*len(adj)
    dist = [None]*len(adj)
    dist[s] = 0
    while queue :
        u = queue.popleft()
        if u == t :
            return dist[u]
        for v in adj[u] :
            if not visited[v] :
                visited[v] = True
                dist[v] = dist[u] + 1
                queue.append(v)
        # new_queue = []
        # for u in queue :
        #     if u == t : return dist
        #     for v in adj[u] :
        #         if not visited[v] :
        #             new_queue.append(v)
        # dist += 1
        # queue = new_queue.copy()
    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
