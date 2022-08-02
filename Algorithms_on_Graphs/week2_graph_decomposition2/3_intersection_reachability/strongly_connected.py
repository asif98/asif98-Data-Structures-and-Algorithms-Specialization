#Uses python3

import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj):
    result = 0
    n = len(adj)
    rev_adj = [[] for _ in range(n)]
    for u in range(n) :
        for v in adj[u] :
            rev_adj[v].append(u)

    visited = [False]*n
    post_order = []
    def dfs(u):
        visited[u] = True
        for v in adj[u] :
            if not visited[v] :
                dfs(v)
        post_order.append(u)

    for u in range(n) :
        if not visited[u] :
            dfs(u)

    #print(post_order)
    #########################
    #########################
    rev_visited = [False]*n

    def rev_dfs(u) :
        rev_visited[u] = True
        for v in rev_adj[u] :
            if not rev_visited[v] :
                rev_dfs(v)

    while post_order :
        u = post_order.pop()
        if not rev_visited[u] :
            result += 1
            rev_dfs(u)
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
    print(number_of_strongly_connected_components(adj))
