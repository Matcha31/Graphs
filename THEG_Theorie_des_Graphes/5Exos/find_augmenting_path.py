# In this exercise you will be given an UNDIRECTED graph including a valid set of edges and a valid matching.
#
# You do not need to validate the edges, nor the matching.  Your task is to implement a function find_augmenting_path(n,edges,matching) which will return None if there is no augmenting path, or return such a path in the form of a LIST OF VERTICES, not a list of edges.
#
# n is number of vertices, numbered 0 through n-1
# edges is a valid list of UNDIRECTED edges.
# matching is a valid matching
# Note that in some cases there are many possible augmenting paths.   You may return any one of them.

# Examples :
#
# matching2 = [(1,6),(2,4),(7,0),(5,3)]
# edges_2_3 = [(1,2),(1,6),(2,3),(2,4),(3,4),(3,5),(3,6),(4,0),(5,7),(5,0),(6,7),(7,0)]
# print(find_augmenting_path(8,edges_2_3,matching2)) -> None
#
# p = find_augmenting_path(4, [(0,1),(1,2),(3,2)], [(2,1)])
# print(p == [0,1,2,3] or p == [3,2,1,0]) -> True


def find_augmenting_path(n, edges, pairs):
    "build a set of edges in both directions"
    edgs = set()
    for (a, b) in pairs:
        edgs.add((a, b))
        edgs.add((b,a))
    free = [True] * n
    for (a, b) in pairs:
        free[a] = free[b] = False
    m = [[] for i in range(n)]
    nm = [[] for i in range(n)]
    for (a, b) in edges:
        if (a, b) not in edgs:
            nm[a].append(b)
            nm[b].append(a)
        else:
            m[a].append(b)
            m[b].append(a)
    visited = [False] * n
    def rec(a):
        visited[a] = True
        for i in nm[a]:
            if visited[i]:
                continue
            if free[i]:
                return [a, i]
            visited[i] = True
            for j in m[i]:
                if visited[j]:
                    continue
                res = rec(j)
                if res is not None:
                    return [a, i] + res
            visited[i] = False
        visited[a] = False
        return None
    for a, b in enumerate(free):
        if b:
            res = rec(a)
            if res:
                return res;
    return None
