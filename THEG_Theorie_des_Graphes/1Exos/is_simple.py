# Decides whether an undirected graph is simple.
#
# Argument n specifies that the graph has n>0 vertices numbered from 0 to n-1. Argument edges is a list of pairs of vertices denoting undirected edges. If vertex i is connected to vertex j, then edges contains either the pair (i,j) or the pair (j,i). If a pair appears multiple times in edges (in any order), this means the corresponding vertices are linked multiple times.
#
# A graph is simple if no two vertices are connected more than once, and the graph has no loop of the form (i,i).
#
# The function should return True if the graph is simple, and False otherwise.

# Examples :
#  Königsberg 7 bridges
# print(is_simple(4, [(0,2),(2,3),(3,0),(2,0),(2,1),(3,1),(1,2)])) ->False
# print(is_simple(5,[(0,1),(1,2),(3,2),(0,3),(2,0),(1,3),(4,1),(4,2)])) -> True


def is_simple(n, edges):
    visited_edges = set()

    for edge in edges:
        if edge[0] == edge[1]:
            return False
        
        sorted_edge = tuple(sorted(edge))

        if sorted_edge in visited_edges:
            return False
        
        visited_edges.add(sorted_edge)

    return True
