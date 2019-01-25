from sys import stdin
from collections import deque

def path(v):
    global graph, visitados, padre, src,tgt
    if v == src:
        return v[0]
    return path(padre[v])+v[0]

def bfs():
    global graph, visitados, padre, src,tgt
    padre = dict();
    for u in graph:
        padre[u]=-1
    visitados = set()
    Q = deque()
    Q.append(src)
    visitados.add(src)
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if not v in visitados:
                padre[v] = u
                Q.append(v)
                visitados.add(v)
    return path(tgt)
    
def main():
    global graph, visitados, padre, src, tgt
    casos = int(stdin.readline().strip())
    for x in range(casos):
        if x != 0:
            print()
        stdin.readline().strip()
        graph = {}
        aristas,recorridos = [int(x) for x in stdin.readline().strip().split()]
        for w in range(aristas):
            a = [x for x in stdin.readline().strip().split()]
     
            for u in range(len(a)):
                if a[u] not in graph:
                    graph[a[u]] = []
                    if u == 0:
                        graph[a[u]].append(a[1])
                    else:
                        graph[a[u]].append(a[0])
                else:
                    if u == 0:
                        graph[a[u]].append(a[1])
                    else:
                        graph[a[u]].append(a[0])
  
        for z in range(recorridos):
            src,tgt = [x for x in stdin.readline().strip().split()]
            print(bfs())
main()
            
