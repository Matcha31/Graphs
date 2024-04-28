# Decides if a graph is Eulerian.
#
# Argument n specifies that the graph has n vertices numbered from 0 to n-1. Argument edges is a list of pairs of vertices denoting undirected edges. If vertex i is connected to vertex j, then edge contains either the pair (i,j) or the pair (j,i). If a pair appears multiple time in edge (in any order), it means the corresponding vertices are linked multiple times.
#
# A graph is simple if any two vertices are connected at most once, and the graph has no loop of the form (i,i).
#
# The function should return True if the graph contains a Eulerian cycle (i.e., a cycle that visit each edge exactly once), and False otherwise. Note that a graph with no edge is Eulerian (an empty cycle will visit all edges).


# Examples :
# print(is_eulerian(5, [(0,1),(0,2),(0,3),(0,4),(1,2),(3,1),(4,1),(3,2),(2,4),(4,3)])) -> True
#  Königsberg 7 bridges
# print(is_eulerian(4, [(0,2),(2,3),(3,0),(2,0),(2,1),(3,1),(1,2)])) -> False
# print(is_eulerian(4, [])) -> True

def is_edge_connected(n, edges):
    successors = [[] for a in range(n)]
    for (a, b) in edges:
        successors[a].append(b)
        successors[b].append(a)
    visited = [False] * n
    visited[edges[0][0]] = True
    to_visit = [edges[0][0]]
    while to_visit:
        current = to_visit.pop()
        for neighboor in successors[current]:
            if not visited[neighboor]:
                visited[neighboor] = True
                to_visit.append(neighboor)
    return all(visited[a] or not successors[a] for a in range(n))

def all_even_degree(n, edges):
    degrees = [0] * n
    for (a, b) in edges:
        degrees[a] += 1
        degrees[b] += 1
    for i in range(len(degrees)):
        if degrees[i] % 2 == 1:
            return False
    return True


def is_eulerian(n, edges):
    if n == 0 or len(edges) == 0:
        return True;
    if (is_edge_connected(n, edges) and all_even_degree(n, edges)):
        return True
    else:
        return False

