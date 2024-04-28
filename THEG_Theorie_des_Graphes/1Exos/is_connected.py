# Decides whether an undirected graph is connected (i.e. there exists a path between any two vertices).
#
# Argument n specifies that the graph has n>0 vertices numbered from 0 to n-1. Argument edges is a list of pairs of vertices denoting undirected edges (if vertex i is connected to vertex j, then edges contains either the pair (i,j) or the pair (j,i)).
#
# The function should return True if the graph is connected, or False otherwise.

# Examples:
# print(is_connected(4,[(0,1),(2,1),(3,0),(3,1)])) -> True
# print(is_connected(5,[(0,1),(2,1),(2,0),(4,3)])) -> False


def is_connected(n, edges):
    adjacency_list = {i: [] for i in range(n)}
    for edge in edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    def dfs(vertex, visited):
        visited.add(vertex)
        for neighbor in adjacency_list[vertex]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited_vertices = set()
    dfs(0, visited_vertices)

    return len(visited_vertices) == n
