from sys import stdin
from collections import deque
def bfs(n_nodos):
    global graph ,colores
    q = deque([0])
    colores[0] = 1
    while q:
        u = q.popleft()
        for v in range(n_nodos):
            if not graph[u][v]:
                continue
            if colores[v] == None:
                colores[v] = 1 if colores[u] == 2 else 2
                q.append(v)
            elif  colores[u] == colores[v]:
                return False
    return True 
def main():
    global graph , colores 
    n_nodos = int(stdin.readline().strip())
    while n_nodos:
        colores = [None]*n_nodos
        graph = []
        for x in range(n_nodos):
            graph.append([0]*n_nodos)
        n_aristas = int(stdin.readline().strip())
        for x in range(n_aristas):
            u,v = [int(x) for x in stdin.readline().strip().split()]
            graph[u][v] = 1
            graph[v][u] = 1
        resp = bfs(n_nodos)
        if resp:
            print('BICOLORABLE.')
        else:
            print('NOT BICOLORABLE.')
        n_nodos = int(stdin.readline().strip())
main()
