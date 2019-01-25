from sys import stdin
def bell_relax(u,v,w):
    global distancia,pad
    if distancia[v] > distancia[u] + w:
        distancia[v] = distancia[u] + w
        pad[v] = u
def bell(graph,inicial):
    global inf,distancia,pad

    inf = float('inf')
    distancia = [inf]*nodos
    pad= [None]*nodos
    distancia[inicial] = 0
    for x in range(nodos-1):
        for u in graph:
            for tup in graph[u]:
                v = tup[0]
                w = tup[1]
                bell_relax(u,v,w)
    for u in graph:
        for tup in graph[u]:
            v = tup[0]
            w = tup[1]
            if distancia[v] > distancia[u] + w:
                return "possible"
    return "not possible"
def main():
    global nodos
    casos = int(stdin.readline().strip())
    for x in range(casos):
        graph = {}
        nodos,aristas = [int(x) for x in stdin.readline().strip().split()]
        for z in range(nodos):
            if z not in graph:
                graph[z] = []
        for w in range(aristas):
            inicial,final,tiempo = [int(x) for x in stdin.readline().strip().split()]
            graph[inicial].append((final,tiempo))
        print(bell(graph,0))
main()
