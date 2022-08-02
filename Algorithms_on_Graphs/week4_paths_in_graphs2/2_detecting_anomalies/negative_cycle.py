#Uses python3

import sys


def negative_cycle(adj, cost):
    adj.append(list(range(len(adj))))
    cost.append([0]*len(cost))
    n = len(adj)
    dist = [float("inf")]*n
    dist[-1] = 0
    count = 0
    for _ in range(n) :
        change = 0
        for u in range(n) :
            for v, weight in zip(adj[u], cost[u]) :
                if dist[v] > dist[u] + weight :
                    dist[v] = dist[u] + weight
                    change += 1
        if change == 0 :
            return 0
    return 1


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
    print(negative_cycle(adj, cost))
