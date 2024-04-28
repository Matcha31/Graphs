# Decides if a cycle is Eulerian, i.e., it visit each edge of the given graph exactly once.
#
# Argument m specifies that the graph has m vertices numbered from 0 to m-1. Argument edges is a list of pairs of vertices denoting undirected edges. If vertex i is connected to vertex j, then edge contains either the pair (i,j) or the pair (j,i). If a pair appears multiple time in edge (in any order), it means the corresponding vertices are linked multiple times.
#
# Argument cycle is a list of n>=0 vertex numbers [v0,v1,v2,...,vn-1] denoting a cycle consisting of n edges (v0,v1),(v1,v2),(v2,v3),...,(vn-2,vn-1),(vn-1,v0). Note that if the input graph contains multiple occurrences of some edge (i,j), then a Eulerian cycle must have as many occurences of this edge.
#
# The function should return True if the given cycle is Eulerian and False otherwise.

# Examples :
# print(is_eulerian_cycle(4, [(0,2),(2,3),(3,0),(2,0),(2,1),(3,1),(1,2),(3,2),(0,1),(0,0)],[0,3,2,0,0,2,1,2,3,1])) -> True

def is_eulerian_cycle(m, edge, cycle):
    if not edge and not cycle:
        return True
    elif edge and not cycle:
        return False

    for i in range(len(cycle) - 1):
        edg = (cycle[i], cycle[i+1])
        if edg in edge:
            edge.remove(edg)
        elif edg[::-1] in edge:
            edge.remove(edg[::-1])
        else:
            return False
    edg = (cycle[0], cycle[-1])
    if edg in edge:
        edge.remove(edg)
    elif edg[::-1] in edge:
        edge.remove(edg[::-1])
    else:
        return False
    return not edge
