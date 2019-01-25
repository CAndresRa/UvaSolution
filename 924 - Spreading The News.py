from sys import stdin
from collections import deque
def bfs():
    global visitados , graph , inicial
    Q = deque()
    Q.append([inicial,0])
    visitados[inicial]=True
    dias=[0]*(nodos+1)
    while Q:
        u,d = Q.popleft()
        for v in graph[u]:
            if not  visitados[v]:
                Q.append([v,d+1])
                dias[d+1]+=1
                visitados[v]=True
    x=max(dias)
    print(dias)
    print(x,dias.index(x))
def main():
    global graph, inicial , nodos,visitados
    nodos = int(stdin.readline().strip())
    graph = {}
    for x in range(nodos):
        if x not in graph:
            graph[x] = []
        a = [int(x) for x in stdin.readline().strip().split()]
        if len(a) > 1:
            for w in range(1,len(a)):
                graph[x].append(a[w])
    cases = int(stdin.readline().strip())
    for x in range(cases):
        inicial = int(stdin.readline().strip())
        
        if graph[inicial] == []:
            print(0)
        else:
            visitados=[False]*nodos
            bfs()

main()  
