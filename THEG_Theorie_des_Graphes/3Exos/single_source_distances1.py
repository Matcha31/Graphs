# Single source shortest paths on weighted, UNDIRECTED graph
#
# You will be given a list of triples [(a,b,w),...] representing weighted edges of an undirected graph.
#
# In this exercise we are only interested in connected graphs. There will be no test cases containing disconnected graphs.  You may also assume that for any two vertices a and b, there is at most one edge between a and b.
#
# In this exercise (a,b) represents an undirected edge, meaning the distance from a to b is w, and also the distance from b to a is w.
# You must write a function single_source_distances(n,edges,src) which takes the parameters
#
# n, the number of vertices.  The vertices are numbered from 0 to n-1,
# edges, a list of triples indicating undirected weighted edges. Each triple of the form (a,b,w) as described above,
# src, the starting vertex.
# Your function should return None if the graph has a negative weight cycle, otherwise it should return a list dist such that dist[v] is the distance of the shortest path from src to v. 

# Examples:
# edges = [(0,1,1),(2,1,2),(2,0,4)]
# print(single_source_distances(3,edges,0))
# -> [0, 1, 3]

def single_source_distances(n,edges,src):
    distances = [math.inf] * n
    distances[src] = 0
    for i in range(n - 1):
        for (a, b, c) in edges:
            distances[b] = min(distances[a] + c, distances[b])
            distances[a] = min(distances[b] + c, distances[a])
    for (a, b, c) in edges:
        if distances[a] > distances[b] + c or distances[b] > distances[a] + c:
            return None
    return distances
