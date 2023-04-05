class Graph:
    def __init__(self, vertices):
        self.graph = []
        self.vertices = vertices

    def addEdge(self, edge):
        # edge between VertexU and VertexV with weight W - [u,v,w]
        self.graph.append(edge)

    def printGraph(self):
        for [u, v, w] in self.graph:
            print(u, v, w)


def bellmanFord(graph: Graph, source: int):
    distances = [float('inf')] * graph.vertices
    distances[source] = 0
    n_vertices = graph.vertices
    for _ in range(n_vertices - 1):
        for u, v, w in graph.graph:

            if distances[u] != float('inf'):
                # Shortest distance to get to the vertex V from vertex U that is currently under consideration
                g_v = distances[u] + w
                # h_v is the distance from the vertex U to the vertex V. To be replaced with Heuristic from vertex V to destination vertex
                h_v = 0

                if g_v < distances[v]:
                    # TODO update the heuristic and f value
                    # f_v = g_v + h_v
                    distances[v] = g_v

    for u, v, w in graph.graph:
        if distances[u] != float("inf") and distances[u] + w < distances[v]:
            print("Graph contains negative weight cycle")
            return
    for i in range(graph.vertices):
        print("Distance from Vertex {0} to vertex {1} is {2}".format(source,i,distances[i]))

    return distances

if __name__ == "__main__":
    ipFile = open('input.txt', "r")
    inputs = [x.rstrip() for x in ipFile.readlines()]
    g = Graph(int(inputs[0]))
    for i in inputs[1:]:
        edge = [int(x) for x in i.split(',')]
        g.addEdge(edge)
    bellmanFord(g,0)
