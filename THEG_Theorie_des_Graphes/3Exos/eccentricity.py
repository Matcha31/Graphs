# Write a function eccentricity(n,edge,i) that compute the eccentricity of vertex i.
#
# Argument n specifies that the directed graph has n>0 vertices numbered from 0 to n-1. Argument edges is a list of pairs of vertices denoting directed edges. If vertex i has an outgoing edge going to vertex j, then edges contains the pair (i,j).
#
# The distance dist(i,j) between two vertices i and j is the minimum number of edges of paths that connect i to j. If i=j, their distance is 0. The eccentricity of vertex i is the maximum distance dist(i,j) to all other vertices j. If the graph is not connected, the eccentricity of all vertices is math.inf.

# Examples:
# print(eccentricity(5,[(0,1),(1,2),(2,3),(3,0),(1,4),(4,2),(0,3)],0)) -> 2
# print(eccentricity(5,[(1,2),(0,0),(3,0),(1,4),(4,2)],4)) -> inf


def eccentricity(n,edges,i):
    successors = [[] for i in range(n)]
    for (a,b) in edges:
        successors[a].append(b)
    visited = [False] * n
    visited[i] = True
    distances = [math.inf] * n
    distances[i] = 0
    stack = [i]
    while stack:
        a = stack.pop(0)
        for s in successors[a]:
            if not visited[s]:
                stack.append(s)
                visited[s] = True
                distances[s] = distances[a] + 1
    return max(distances)
