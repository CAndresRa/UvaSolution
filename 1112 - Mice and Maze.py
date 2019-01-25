from sys import stdin
import heapq
def djk_relax(u,v,w):
    global distancia , graph , Q , pad
    if distancia[v] > distancia[u] + w:
        distancia[v] = distancia[u] + w
        pad[v] = u
        heapq.heappush(Q,(distancia[v],v))
def djk(inicial):
    global graph , Q, distancia, visitados , pad
    inf = float('inf')
    visitados = set()
    distancia = [inf]*(nodos+1)
    pad = [None]*(nodos+1)
    distancia[inicial] = 0 
    Q = []
    heapq.heappush(Q,(distancia[inicial],inicial))
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
    global graph , nodos 
    casos = int(stdin.readline().strip())
    
    for x in range(casos):
        stdin.readline().strip()
        if x != 0:
            print()
        graph = {}
        nodos = int(stdin.readline().strip())
        final = int(stdin.readline().strip())
        tiempo = int(stdin.readline().strip())
        aristas = int(stdin.readline().strip())
        for x in range(1,nodos+1):
            graph[x] = []
        for x in range(aristas):
            a,b,c = [int(x) for x in stdin.readline().strip().split()]
            graph[b].append((a,c))
        solution = djk(final)
        cont = 0
        for x in solution:
            if x <= tiempo:
                cont+=1
        print(cont)
main()
            
