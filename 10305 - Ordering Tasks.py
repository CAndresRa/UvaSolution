from sys import stdin
from collections import deque
def dfs(x):
    global topo,visitados
    visitados[x] = True
    for u in graph[x]:
        if visitados[u] == False:
            dfs(u)
    topo.appendleft(x)
    
def main():
    global visitados , graph, topo
    nodos,aristas = [int(x) for x in stdin.readline().strip().split()]
    while nodos+aristas:
        graph = {}
        visitados = {}
        topo = deque()
        for x in range(1,nodos+1):
            graph[x] = []
            visitados[x] = False
        for x in range(aristas):
            a,b = [int(x) for x in stdin.readline().strip().split()]
            graph[a].append(b)
        for x in range(1,nodos+1):
            if visitados[x] == False:
                dfs(x)
        print(*topo)
        nodos,aristas = [int(x) for x in stdin.readline().strip().split()]
main()
