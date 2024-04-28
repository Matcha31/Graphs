# In the last question you have coded a generalised version of the Floyd-Warshall algorithm to take into account different operations.
# In this question you will extend its capabilities to not only compute the distance matrix, but also the "generalised shortest" paths.
#
# To allow for the computation of the shortest paths, you have to use an additional data-structure. This structure holds information about the predescessor or successor (depending on the implementation) of the vertices and is updated during the execution of the algorithm.
#
# In the course (for the case of ⊕ = min and ⊗ = addition) , this was presented as:
# if k-1Mij > k-1Mik + k-1Mkj:
#     #Update distance matrix
#     #Update data-structure
#
# As not all sets are ordered, this notion has to be generalised and becomes:
# # Compute kMij
# if kMij != k-1Mij:
#     #Update data-structure
#
# You have to code two functions:
# A new version of the Floyd-Warshall algorithm that returns not only the distance matrix, but also the data-structure holding the necessary information to compute the path (The inputs remain the same as in the first part).
# A function path(D, source, destination) that outputs the "shortest path" from the vertex source to destination as a function of the data-structure D.
#
# We use the following convention:
# If no path exists from source to destination, path(D, source, destination) is expected to return an empty list [].
# If source==destination, path is expected to return [source]
# Otherwise the returned path has to contain all vertices visited by the path from source to destination in the correct order, including source and destination.
#
# You can rely on the same assumptions as for the first part of the question.
#
# Example of how your code will be called:
# M,D = floyd_warshall(n, edges, op_min, math.inf, op_add, 0)
# Pij = path(D,source,destination)

# Example :
#
# n = 5
# edges = [(0,1,1), (1,0,3), (3,2,1), (1,4,4), (4,3,-1), (3,4,2)]
# print(evaluate_path_pa1(n,edges,op_min, math.inf, op_add, 0, floyd_warshall, path))
# True


def path(succ, i, j):
  if succ[i][j] is None:
    return []
  path = [i]
  while i != j:
    i = succ[i][j]
    path.append(i)
  return path

def floyd_warshall(n, edges, op_plus, e_plus, op_times, e_times):
  succ = [[None for j in range(n)] for i in range(n)]
  last = [[e_plus for j in range(n)] for i in range(n)]
  for i in range(n):
    succ[i][i] = i
    last[i][i] = e_times
  for (a,b,c) in edges:
    succ[a][b] = b
    last[a][b] = c
  for k in range(n):
    curr = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
      for j in range(n):
        curr[i][j] = op_plus(last[i][j], op_times(last[i][k], last[k][j]))
        if curr[i][j] != last[i][j]:
          succ[i][j] = succ[i][k]
    last = curr
  return curr, succ
