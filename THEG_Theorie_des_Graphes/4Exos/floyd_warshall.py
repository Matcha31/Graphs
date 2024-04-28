# In the course the Floyd-Warshall algorithm has been presented to you for computing the distance matrix of a directed weighted graph. We will denote this matrix M.
# To compute M, the instructions
# kMij = min(k-1Mij, k-1Mik+k-1Mkj)
# are repeated for k from 0 to the number of vertices minus one.
# -1Mij corresponds to the initialization and we have three cases:
#
# i==j : -1Mij = 0
# there exist an edge (i,j,w) : -1Mij = w
# None of the above : -1Mij = +inf
# This notation can be generalised to:
#
# kMij = k-1Mij ⊕ (k-1Mik ⊗ k-1Mkj)
# where (kMij ∈ H, ⊕, ⊗) is a semiring.
# The operations ⊕ and ⊗ also have neutral elements in H. For instance, in the case of H being the integers, the neutral element
# of min (operation ⊕) is +inf, the neutral element of + (operation ⊗) is 0.
#
# Depending on which operations (⊕, ⊗) and neutral elements (from the set H) are used, different properties of the graph can be computed using Floyd-Warshall.
#
# In this exercice you are expected to code a generalised version of the Floyd-Warshall-algorithm
# floyd_warshall(n,edges, op_plus, e_plus, op_times, e_times)
# which takes the inputs:
# n: number of vertices labeled 0 to n-1
# edges: weighted edges as list of tuples of the form [(src_0, dst_0, weight_0), (src_1, dst_1, weight_1), ...]
# op_plus : The operation ⊕
# e_plus : The neutral element of ⊕
# op_times : The operation ⊗
# e_times : The neutral element of ⊗
#
# Some operations are already predefined, and will be passed as arguments to your function by the test cases. The operations are given as the functions:
#
# op_add
# op_min
# op_max
# The algorithm is expected to return the distance matrix kM as a list of lists, so that Mij denotes the element in the i-th row and j-th column, corresponding to the minimal the distance to go from the i-th to the j-th vertex.
#
# Example how your algorithm will be called:
# M = floyd_warshall(n, edges, op_min, math.inf, op_add, 0)
#
# Remarks
#
# Take care: ⊕/⊗ ("plus"/"times") can denote any of the above defined operations and must not be confused with +/*, the usual addition and multiplication operations over the integers or reals.
# It is important to actually implement Floyd-Warshall. The operators used for ⊕ and ⊗ have internal mechanisms that detect repeated calls of Bellmann-Ford for instance.
# For the exercices, you can assume that:
# There exists only a single edge between any pair of vertices
# You do not need to implement a detection of negative cycles (or the generalisation thereof), the graphs used for testing do not contain such cycles.
# There are no self-loops (src and dst of an edge are equal)

# Examples :
#
# n = 5
# edges = [(0,1,1), (1,0,3), (3,2,1), (1,4,4), (4,3,-1), (3,4,2)]
# print(floyd_warshall(n,edges,op_min, math.inf, op_add, 0))
# [[0, 1, 5, 4, 5], [3, 0, 4, 3, 4], [inf, inf, 0, inf, inf], [inf, inf, 1, 0, 2], [inf, inf, 0, -1, 0]]
#
# n = 5
# edges = [(0,1,7), (1,0,3), (3,2,1), (1,4,4), (4,3,3), (3,4,2), (0,3,1)]
# print(floyd_warshall(n,edges,op_max, 0, op_min, math.inf))
# [[inf, 7, 1, 3, 4], [3, inf, 1, 3, 4], [0, 0, inf, 0, 0], [0, 0, 1, inf, 2], [0, 0, 1, 3, inf]]


def floyd_warshall(n, edges, op_plus, e_plus, op_times, e_times):
  last = [[e_plus for j in range(n)] for i in range(n)]
  for i in range(n):
    last[i][i] = e_times
  for (a,b,c) in edges:
    last[a][b] = c
  for i in range(n):
    curr = [[None for _ in range(n)] for _ in range(n)]
    for j in range(n):
      for k in range(n):
        curr[j][k] = op_plus(last[j][k], op_times(last[j][i], last[i][k]))
    last = curr
  return curr
