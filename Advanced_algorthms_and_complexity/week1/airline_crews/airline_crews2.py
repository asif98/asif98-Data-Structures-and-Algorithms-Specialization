# python3
from collections import deque
class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity

class FlowGraph:

    def __init__(self, n):
        self.n = n
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].capacity -= flow
        self.edges[id ^ 1].capacity += flow


def read_data():
    f, c = map(int, input().split())
    graph = FlowGraph(f + c + 2)
    for flight in range(1, f+1) :
        graph.add_edge(0, flight, 1)

    for flight in range(1, f+1) :
        adj = list(map(int, input().split()))
        for crew in range(1, c+1) :
            if adj[crew-1] == 1 :
                graph.add_edge(flight, f+crew, 1)
    for crew in range(1, c+1) :
        graph.add_edge(f+crew, f+c+1, 1)

    return graph, f, c

def write_response(matching):
    line = [str(-1 if x == -1 else x + 1) for x in matching]
    print(' '.join(line))

def find_matching(graph, f, c):
        n = graph.n
        while True :
            queue = deque()
            visited = [False]*n
            parent_edge = [-1]*n
            source = 0
            sink = n-1
            visited[source] = True
            queue.append(source)

            while queue :
                #print(queue)
                u = queue.popleft()
                for idx in graph.graph[u] :
                    v = graph.edges[idx].v
                    capacity = graph.edges[idx].capacity
                    if capacity > 0 and not visited[v] :
                        visited[v] = True
                        queue.append(v)
                        parent_edge[v] = idx
                        if v == sink :
                            break
                else :
                    continue

                path = []
                node = sink
                min_flow = float("inf")
                while node != source :
                    idx = parent_edge[node]
                    path.append(idx)
                    min_flow = min(min_flow, graph.edges[idx].capacity)
                    node = graph.edges[idx].u

                for idx in path :
                    graph.add_flow(idx, min_flow)
                break

            else :

                # print("n = ", len(graph.edges))
                # for edge in graph.edges :
                #     print(edge.u, edge.v, edge.capacity)
                # print("----------")
                matching = [-1] * f
                for edge in graph.edges :
                    if 0 < edge.u <= f and edge.v > 0 and edge.capacity == 0 :
                        matching[edge.u - 1] = edge.v - f -1

                return matching


if __name__ == '__main__':
    graph, f, c = read_data()
    matching = find_matching(graph, f, c)
    write_response(matching)
