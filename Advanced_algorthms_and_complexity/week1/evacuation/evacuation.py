# python3
from collections import deque
class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        #self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
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
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].capacity -= flow
        self.edges[id ^ 1].capacity += flow

def max_flow(graph, from_, to):
    flow = 0
    n = graph.n
    # your code goes here
    while True :
        #print("---------------")
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
            break
        else :
            return flow

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

        flow += min_flow

        # for idx in range(len(graph.edges)) :
        #     print(graph.edges[idx].u, graph.edges[idx].v, graph.edges[idx].capacity )

    return flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
