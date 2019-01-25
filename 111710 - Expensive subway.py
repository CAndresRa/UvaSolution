from sys import stdin
def create_set(e):
    padres[e] = e
    rango[e] = 0
def find(e):
    if padres[e] == e:
        return e
    else:
        return find(padres[e])
def union(u,v):
    ru = find(u)
    rv = find(v)
    if ru != rv:
        if rango[ru] > rango[rv]:
            padres[rv] = ru
        else:
            padres[ru] = rv
            if rango[ru] == rango[rv]:
                rango[rv] += 1
                
def kruskal(nodos):
    for x in range(nodos):
        create_set(x)
    cont = 0; n=nodos
    for x in graph:
        if find(x[0]) != find(x[1]):
            union(x[0],x[1])
            cont += x[2];
            n-=1
    if n!=1: return 'Impossible'
    return cont
def main():
    global graph, rango, padres 
    nodos, aristas = [int(x) for x in stdin.readline().strip().split()]
    while nodos:
        padres = {}
        rango = {}
        ciudades = {}
        graph = []
        for x in range(nodos):
            a = stdin.readline().strip()
            ciudades[a] = x
        for x in range(aristas):
            b = [x for x in stdin.readline().strip().split()]
            graph.append([ciudades[b[0]],ciudades[b[1]],int(b[2])])
        graph.sort(key=lambda r:r[2])
        inicio = stdin.readline().strip()
        print(kruskal(nodos))
        nodos, aristas = [int(x) for x in stdin.readline().strip().split()]

main()
        
