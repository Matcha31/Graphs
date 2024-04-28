# Your task is to write a function find_maximum_matching(n,edges) which will generate and return a maximum matching for the graph.   Your function should return a list of edges, i.e. a list of pairs of vertices.
#
# n is number of vertices, numbered 0 through n-1
# edges is a valid list of UNDIRECTED edges.
# Remember, that in this exercise the matching you return is a list of edges, i.e., a list of pairs of verices.  In a previous exercise you returned a path as a list of vertices.
#
# Also remember that the function should never return None.   Why?  Because a maximum matching always exists.   If the graph has no edges, then the maximum matching is [], and if the graph has at least one edge, (a,b)  then at least one matching exists, namely [(a,b)].
#
# Important note: You can assume that a working implementation of the function  find_augmenting_path(n,edges,matching), specified in a previous exercice, is available.  So all you need to do here is update a matching using the result of find_augmenting_path until no more augmenting is found.

# Examples :
#
# edges_2_3 = [(1,2),(1,6),(2,3),(2,4),(3,4),(3,5),(3,6),(4,0),(5,7),(5,0),(6,7),(7,0)]
# best_matching = find_maximum_matching(8,edges_2_3)
# print(SA_is_matching(8,edges_2_3,best_matching), len(best_matching)) -> True 4
#
# args1 = (18, [(0, 1), (1, 2), (2, 3), (2, 4), (3, 6), (4, 5), (5, 6), (6, 7),
#               (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (11, 13), (12, 14),
#               (13, 15), (14, 15), (15, 16), (16, 17)])
# m = find_maximum_matching(*args1)
# print(SA_is_matching(*args1, m), len(m)) -> True 9


def normalize(a):
    """Normalize"""
    if a[0] > a[1]:
        a = (a[1], a[0])
    return a

def find_maximum_matching(n, edges):
    pairs = []
    p = find_augmenting_path(n, edges, pairs)
    while p is not None:
        pairs = list({ normalize(a) for a in pairs } ^ { normalize(a) for a in zip(p, p[1:]) })
        p = find_augmenting_path(n, edges, pairs)
    return pairs
