# Finds a Eulerian cycle in a graph that we assume to be Eulerian.
#
# Argument m specifies that the graph has m vertices numbered from 0 to m-1. Argument edges is a list of pairs of vertices denoting undirected edges. If vertex i is connected to vertex j, then edges contains either the pair (i,j) or the pair (j,i). If a pair appears multiple times in edges (in any order), it means the corresponding vertices are linked multiple times.
#
# The function should return a list of vertex numbers [v0,v1,v2,...,vn-1] such that the n edges (v0,v1),(v1,v2),(v2,v3),...,(vn-2,vn-1),(vn-1,v0) form a cycle that visits each edge of the graph exactly once.

# Examples:
# g0=(4, [(0,1),(1,2),(2,3),(3,0)])
# print(is_eulerian_cycle(*g0, find_eulerian_cycle(*g0))) -> True
# g1=(4, [(2,0),(2,1),(3,1),(1,2),(0,2),(2,3),(3,0),(3,2),(0,1),(0,0)])
# print(is_eulerian_cycle(*g1, find_eulerian_cycle(*g1))) -> True


def find_eulerian_cycle(m, edges):
    if not edges:
        return []
    
    successors = [[] for a in range(m)]
    for (a, b) in edges:
        successors[a].append(b)
        successors[b].append(a)

    start = 0
    while not successors[start]:
        start += 1
    cycle = []
    stack = [start]
    while stack:
        start = stack[-1]
        if successors[start]:
            y = successors[start][0]
            stack.append(y)
            successors[start].remove(y)
            successors[y].remove(start)
        else:
            cycle.append(stack.pop())
    
    i = 0
    for i in range(len(cycle)):
     start = cycle[i]
     if successors[start]:
         cycle = cycle[:i] + find_cycle(successors, start) + cycle[i + 1:]
     else:
         continue
    # cycle.pop()

    while i < len(cycle):
        start = cycle[i]
        if successors[start]:
            cycle = cycle[:i] + find_cycle(successors, start) + cycle[i + 1:]
        else:
            i += 1
    return cycle[:len(cycle)-1]
