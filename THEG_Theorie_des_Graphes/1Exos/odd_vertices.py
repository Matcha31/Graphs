# Returns the list of odd-degree vertices sorted in ascending order.
#
# The degree of a vertex is the number of edges incident to that vertex.
#
# Argument n specifies that the graph has n>0 vertices numbered from 0 to n-1. Argument edges is a list of pairs of vertices denoting undirected edges. If vertex i is connected to vertex j, then edges contains either the pair (i,j) or the pair (j,i). If a vertex does not appear in any edge, it is an isolated vertex and thus has degree 0 (which is even). If a pair appears multiple times in edges (in either order), this means the corresponding vertices are linked multiple times. A loop of the form (i,i) contributes 2 to the degree of vertex i.

# Examples :
# print(odd_vertices(4, [(0,3),(3,2),(1,2),(3,1)])) -> [0, 3]
# print(odd_vertices(3, [(1,1)])) -> []


def odd_vertices(n, edges):
    degrees = {i: 0 for i in range(n)}
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    odd_vertices = [vertex for vertex, degree in degrees.items() if degree % 2 != 0]
    odd_vertices.sort()
    return odd_vertices
