#Uses python3

import sys
import queue
import heapq

def distance(adj, cost, s, t):
    n = len(adj)
    dist_heap = [[0,s]]
    #dist_heap[s][0] = 0
    dist_min = [float("inf")]*n
    dist_min[s] = 0
    heapq.heapify(dist_heap)

    while dist_heap :
        d, u = heapq.heappop(dist_heap)
        if dist_min[u] == d :
            if u == t : return d
            for v, weight in zip(adj[u], cost[u]) :
                if dist_min[v] > dist_min[u] + weight :
                    dist_min[v] = dist_min[u] + weight
                    heapq.heappush(dist_heap, [dist_min[v], v])
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
