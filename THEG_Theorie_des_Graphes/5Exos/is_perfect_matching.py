# You must implement a function that takes list of edges and determines whether it designates a perfect matching.
#
# You must implement the function is_perfect_matching(n,edges,pairs).
#
# n is number of vertices, numbered 0 through n-1
# edges is a valid list of UNDIRECTED edges.
# pairs is a list of pairs of integers, warning there is no guarantee they correspond to actual edges.
# Your function must return True if the list pairs designates a perfect matching for the graph, and must return False otherwise.

# Examples :
# print(is_perfect_matching(4,[(0,1),(1,2),(2,3),(3,0)],[(0,1),(3,2)])) -> True
# print(is_perfect_matching(4,[(0,1),(1,2),(2,3),(3,0)],[(1,2)])) -> False


def is_matching(n, edges, pairs):
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
    return True

def is_perfect_matching(n, edges, pairs):
    if (len(pairs) != n/2) or (n % 2):
        return False
    return is_matching(n, edges, pairs)
