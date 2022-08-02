#Uses python3
import sys
import math

def minimum_distance(x, y):
    n = len(x)
    distances = []
    for i in range(n-1) :
        for j in range(i+1,n) :
            dist = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            distances.append([dist, i, j])
    distances.sort()
    #print(distances)

    parent = list(range(n))
    def find(u) :
        while parent[u] != u :
            u = parent[u]
        return u

    def union(u, v) :
        u = find(u)
        v = find(v)
        parent[u] = v

    components = n
    total_length = 0
    for d, u, v in distances :
        if find(u) != find(v) :
            total_length += d
            union(u, v)
            components -= 1
            if components == 1 :
                break

    return total_length


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
