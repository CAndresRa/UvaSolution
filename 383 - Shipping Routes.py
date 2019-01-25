from sys import stdin
import heapq
def djk_relax(u,v,w):
    global Q, dis , pad
    if distancia[v] > distancia[u] + w:
        distancia[v] = distancia[u] + w
        pad[v] = u
        heapq.heappush(Q,(distancia[v],v))
def djk(inicial, final):
    global graph , nodos , distancia , pad , Q  , inf , visitados
    visitados = set()
    inf = float('inf')
    distancia = [inf]*nodos
    pad = [None]*nodos
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
                if v == final:
                    break
    return distancia[final]
    
def main():
    global graph, nodos , distancia , pad , Q
    casos = int(stdin.readline().strip())
    print('SHIPPING ROUTES OUTPUT')
    print()
    for c in range(casos):
        print('DATA SET  {}'.format(c+1))
        print()
        numbs = {}
        graph = {}
        cont = 0
        nodos,aristas,envios = [int(x) for x in stdin.readline().strip().split()]
        if aristas + envios == 0:
            lnodos = [x for x in stdin.readline().strip().split()]
            print()
        elif aristas == 0 and envios != 0:
            lnodos = [x for x in stdin.readline().strip().split()]
            print('NO SHIPMENT POSSIBLE')
            for x in range(envios):
                b = [x for x in stdin.readline().strip().split()]
            print()
 
        else:
            lnodos = [x for x in stdin.readline().strip().split()]
            for x in lnodos:
                if x not in graph:
                    numbs[x] = cont
                    cont += 1
            for x in range(aristas):
                a = [x for x in stdin.readline().strip().split()]
                if numbs[a[0]] not in graph:
                    graph[numbs[a[0]]] = []
                if numbs[a[1]] not in graph:
                    graph[numbs[a[1]]] = []
                graph[numbs[a[0]]].append((numbs[a[1]],1))
                graph[numbs[a[1]]].append((numbs[a[0]],1))
            if graph == {}:
                print('NO SHIPMENT POSSIBLE')
                break
            for x in range(envios):
                b = [x for x in stdin.readline().strip().split()]
                inicio = numbs[b[1]]
                final = numbs[b[2]]
                if inicio not in graph or final not in graph:
                    print('NO SHIPMENT POSSIBLE')
                else:
                    solution = djk(inicio,final)
                    if solution != inf:
                        print('{}{}'.format('$',(solution*int(b[0]))*100))
                    else:
                        print('NO SHIPMENT POSSIBLE')
            print()
            if c+1 == casos:
                print('END OF OUTPUT')

main()
