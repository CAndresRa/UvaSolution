from sys import stdin
import heapq
def djk_relax(u,v,w):
    global Q, distancia, padre
    if distancia[v] > distancia[u] + w:
        distancia[v] = distancia[u] + w
        padre[v] = u
        heapq.heappush(Q,(distancia[v],v))
def djk(inicial):
    global distancia, visitados, padre, Q , inf
    inf = float('inf')
    visitados = set()
    padre = [None]*nodos
    distancia = [inf]*nodos
    Q = []
    for x in inicial:
        distancia[x] = 0
        heapq.heappush(Q,(distancia[x],x))
    while Q:
        d,u = heapq.heappop(Q)
        for x in graph[u]:
            if x not in visitados:
                visitados.add(x)
                v = x[0]
                w = x[1]
                djk_relax(u,v,w)
    return distancia
def main():
    global nodos,graph
    s = [int(x) for x in stdin.readline().strip().split()]
    while s != []:
        nodos = s[0]
        aristas = s[1]
        bancos = s[2]
        estaciones = s[3]
        graph = {}
        for x in range(nodos):
            if x not in graph:
                graph[x] = []
        for x in range(aristas):
            a,b,c = [int(x) for x in stdin.readline().strip().split()]
            graph[a].append((b,c))
            graph[b].append((a,c))
        if bancos > 0:
            d = [int(x) for x in stdin.readline().strip().split()]
        else:
            d = []
        if estaciones > 0:
            e = [int(x) for x in stdin.readline().strip().split()]
        else:
            e = []
        djk(e)
        maximo = -float('inf')
        cont = 0
        solution = []
        for x in range(len(distancia)):
            if x in d:
                maximo = max(distancia[x],maximo)
        for x in range(len(distancia)):
            if distancia[x] == maximo and x in d:
                solution.append(x)
        if maximo == inf:
            maximo = '*'
        print(len(solution),maximo)
        solution.sort()
        print(*solution)
        s = [int(x) for x in stdin.readline().strip().split()]
main()
