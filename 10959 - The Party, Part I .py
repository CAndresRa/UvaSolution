from sys import stdin
from collections import deque
def bfs(graph):
    global inf
    inf = float('inf')
    distancia = [inf]*nodos
    distancia[0] = 0
    Q = deque()
    Q.append(0)
    while Q:
        u = Q.popleft()
        print(graph)
        for v in graph[u]:
            if distancia[v] == inf:
                distancia[v] = distancia[u] + 1
                Q.append(v)
    return distancia
    
def main():
    global nodos
    casos = int(stdin.readline().strip())
    for x in range(casos):
        if x != 0:
            print()
        graph = {}
        stdin.readline().strip()
        nodos , aristas = [int(x) for x in stdin.readline().strip().split()]
        for w in range(nodos):
            if w not in graph:
                graph[w] = []
        for w in range(aristas):
            a,b = [int(x) for x in stdin.readline().strip().split()]
            graph[a].append(b)
            graph[b].append(a)
        solution = bfs(graph)
        for x in solution:
            if x != 0 and x != inf:
                print(x)
main()
            
