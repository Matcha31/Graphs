# You must implement a function that takes list of edges and determines whether it designates a maximal matching.
#
# You must implement the function is_maximal_matching(n,edges,pairs).
#
# n is number of vertices, numbered 0 through n-1
# edges is a valid list of UNDIRECTED edges.
# pairs is a list of pairs of integers, warning there is no guarantee they are edges.
# Your function must return True if the list pairs designates a maximal matching for the graph, and must return False otherwise.

# Examples :
# print(is_maximal_matching(4, [(0,1),(1,2),(2,3),(3,0)], [(0,1), (2,1)])) -> False
# print(is_maximal_matching(4, [(0,1),(1,2),(2,3),(3,0)], [(0,1), (2,3)])) -> True
    

def is_maximal_matching(n, edges, pairs):
    edgs = set()
    for (a, b) in edges:
        edgs.add((a, b))
        edgs.add((b, a))
    visited = [False] * n
    for (a, b) in pairs:
        if (a, b) not in edgs or visited[a] or visited[b]:
            return False
        visited[a] = True
        visited[b] = True
    return all(visited[a] or visited[b] for (a,b) in edges)
