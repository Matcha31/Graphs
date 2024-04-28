# Écrire une fonction scc(n,edges) qui retoure un tableau indiquant le numéro de la composante fortement connexe maximal contenant chaque sommet.  La numérotation des composantes peut être choisie arbitrarirement, tant que chaque composante possède un numéro unique et que tous les sommets de cette composante ont cet unique numéro dans le tableau retourné par scc.
#
# Comme dans les autres exercices, on suppose que n et strictement positif et que edges est une liste de paire de sommets représentant les arcs d'un graphe orienté.

# Pour le graphe du png, qui contient quatre composantes fortement connexes maximales {0,8}, {1,2,4,5,7}, {3,6}, et {9}, le tableau retourné par la fonction scc peut être par exemple [0, 2, 2, 1, 2, 2, 1, 2, 0, 3] ou bien encore [13, 27, 27, 41, 27, 27, 41, 27, 13, 8]. 
#
# La fonction renumber_sccs(sccarray) utilisée dans les tests, réécrit ces deux tableaux sous la forme [0, 1, 1, 2, 1, 1, 2, 1, 0, 3] (c'est-à-dire que les composantes sont renumérotées dans l'ordre de leur plus petit état) afin de comparer les solutions.

def scc(n, edges):
    succ = [[] for _ in range(n)]
    for (a, b) in edges:
        succ[a].append(b)
    inscc = [None] * n
    scc.n = 0
    index = [0] * n
    scc.next_index = 1

    def dfs(s):
        stack = [s]
        live = [s]
        index[s] = scc.next_index
        roots = [scc.next_index]
        scc.next_index += 1
        while stack:
            src = stack[-1]
            if len(succ[src]) == 0:
                stack.pop()
                if index[src] == roots[-1]:
                    while True:
                        x = live.pop()
                        inscc[x] = scc.n
                        if x == src:
                            break
                    scc.n += 1
                    roots.pop()
            else:
                dst = succ[src].pop()
                idst = index[dst]
                if idst > 0:
                    if inscc[dst] is None:
                        while roots[-1] > idst:
                            roots.pop()
                else:
                    index[dst] = scc.next_index
                    roots.append(scc.next_index)
                    scc.next_index += 1
                    stack.append(dst)
                    live.append(dst)
    for i in range(n):
        if inscc[i] is None:
            dfs(i)
    return inscc
