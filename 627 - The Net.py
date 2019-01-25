from sys import stdin
import heapq
def path(v):
    global graph, visitados, pad , inicial , solution
    solution.append(v)
    if v == inicial:
        return v
    return path(pad[v])
    
def djk_relax(u,v,w):
    global Q , distancia , pad
    if distancia[v] > distancia[u] + w:
        distancia[v] = distancia[u] + w
        pad[v] = u
        heapq.heappush(Q,(distancia[v],v))
        
def djk(inicial,final):
    global distancia , graph , Q , inf , visitados, pad
    visitados = set()
    inf = float('inf')
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
   
    return distancia[final]
def main():
    global nodos, graph ,inicial , final, solution 
    nodos = stdin.readline().strip()
    while nodos != '':
        nodos = int(nodos)
        print('-----')
        graph = {}
        for x in range(1,nodos+1):
            graph[x] = []
        for x in range(nodos):
            a = stdin.readline().strip().split("-")
            aux = []
            if a[1] != "":
                aux = a[1]
                aux = aux.split(",")
            for w in aux:
                if w != '':
                    graph[int(a[0])].append((int(w),1))

        recorrido = int(stdin.readline().strip())
        for x in range(recorrido):
            solution = []
            inicial, final = [int(x) for x in stdin.readline().strip().split()]
            resp = djk(inicial,final)
            if resp != inf:
                path(final)
                solution.reverse()
                print(*solution)
            else:
                print('connection impossible')
            
        nodos = stdin.readline().strip()
main()
