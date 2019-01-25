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
    solution = -float('inf')
    for x in range(nodos):
        create_set(x)
    cont = 0
    n = nodos
    for x in graph:
        if find(x[0]) != find(x[1]):
            union(x[0],x[1])
            cont += x[2]
            n-= 1
            solution = max(x[2],solution)
            
    if n != 1:
        return 'IMPOSSIBLE'
    return solution
def main():
    global graph, padres, rango
    city,roads = [int(x) for x in stdin.readline().strip().split()]
    while city:
        padres = {}
        rango = {}
        graph = []
        for x in range(roads):
            a = [int(x) for x in stdin.readline().strip().split()]
            graph.append(a)
        graph.sort(key=lambda r:r[2])
        print(kruskal(city))
        city,roads = [int(x) for x in stdin.readline().strip().split()]
main()
