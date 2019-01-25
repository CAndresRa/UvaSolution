from sys import stdin
from collections import deque
def bfs(graph,inicial,final):
    inf = float('inf')
    distancia = [inf]*nodos
    distancia[inicial] = 0
    Q = deque()
    Q.append(inicial)
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if distancia[v] == inf:
                distancia[v] = distancia[u] + 1
                Q.append(v)
    return distancia[final] - 1

    
def main():
    global nodos
    casos = int(stdin.readline().strip())
    for c in range(casos):
        if c != 0:
            print()
        stdin.readline().strip()
        nodos = int(stdin.readline().strip())
        graph = {}
        for x in range(nodos):
            if x not in graph:
                graph[x] = []
            a = [int(x) for x in stdin.readline().strip().split()]
            for w in range(len(a)):
                graph[a[0]].append(a[w])
        inicial, final = [int(x) for x in stdin.readline().strip().split()]
        solution = bfs(graph,inicial,final)
        print('{} {} {}'.format(inicial,final,solution))
main()
