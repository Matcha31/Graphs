# In the last part of the question you have implemented a generalised version of the Floyd-Warshall algorithm and how to use it in order to find the shortest/optimal path in the graph.
#
# In this question you are asked to implement a specific version of the algorithm (i.e. using suitable operations and neutral elements) to answer the following question:
#
# The vertices correspond to cities, the edges correspond to the transition from one city to another. The weight on the edges (reals taken from the interval [0,1]) corresponds to the success rate of the transition. So if the edge is (0,1,0.9) you have a 10% chance to die in a horrible plane crash when going from city 0 to city 1.
#
# Your task is to use Floyd-Warshall to compute the safest path between two cities called source and destination.
#
# Code the function:
# safest_path(n,edges,source,destination)
# returning the safest path in the same style as in the last question.
#
# The same assumptions as for the first two parts hold.

# Examples :
#
# for _ in range(10):
#     res = evaluate_safest_path_random(safest_path)
#     if not res:
#         print(False)
#         break
# if res:
#     print(True)
# True
#
# g = (3, [(0,1,0.8), (1,2,0.5), (0,2,0.3)])
# print(safest_path(*g, 0, 2))
# print(safest_path(*g, 1, 2))
# print(safest_path(*g, 1, 1))
# print(safest_path(*g, 2, 0))
# [0, 1, 2]
# [1, 2]
# [1]
# []


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

def safest_path(n, edges, i, j):
  M, s = floyd_warshall(n,edges, op_max, 0., op_mul, 1.)
  return path(s, i, j)
