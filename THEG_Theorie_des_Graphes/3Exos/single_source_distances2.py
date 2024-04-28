# Single source shortest paths on weighted, DIRECTED graph
#
# You will be given a list of triples [(a,b,w),...] representing weighted, directed edges.
#
# In this exercise the graphs are not necessarily strongly connected.
#
# In this exercise (a,b) represents an directed edge, meaning the distance from a to b is w, but careful, it does not mean the distance from b to a is w.  However, there is at most one edge from a to b and at most one edge from b to a.
#
# You must write a function single_source_distances(n,edges,src) which takes the parameters
#
# n, the number of vertices.  The vertices are numbered from 0 to n-1,
# edges, a list of triples indicating directed weighted edges. Each triple of the form (a,b,w) as described above,
# src, the starting vertex.
# Your function should return None if the graph has a negative weight cycle, otherwise it should return a list dist such that dist[v] is the distance of the shortest path from src to v. If vertex v is not reachable from the given src vertex, then dist[v] should be math.inf.

# Examples:
# edges = [(0,3,2),(0,1,1),(1,2,12),(2,0,-3)]
# print(single_source_distances(4,edges,0))
# -> [0, 1, 13, 2]


def single_source_distances(n,edges,src):
    distances = [math.inf] * n
    distances[src] = 0
    for i in range(n - 1):
        for (a, b, c) in edges:
            distances[b] = min(distances[a] + c, distances[b])
    for (a, b, c) in edges:
        if distances[a] + c < distances[b]:
            return None
    return distances
    
    dist = [math.inf] * n
    dist[src] = 0
    for k in range(n - 1):
        for (s, d, w) in edges:
            dist[d] = min(dist[d], dist[s] + w)
    for (s, d, w) in edges:
        if dist[d] > dist[s] + w:
            return None
    return dist
