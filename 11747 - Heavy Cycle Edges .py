from sys import stdin
def create_set(e):
    padre[e] = e
    rango[e] = 0
def find(e):
    if padre[e] == e:
        return e
    else:
        return find(padre[e])
def union(u,v):
    ru = find(u)
    rv = find(v)
    if ru != rv:
        if rango[ru] > rango[rv]:
            padre[rv] = ru
        else:
            padre[ru] = rv
            if rango[ru] == rango[rv]:
                rango[rv] += 1
def kruskal(nodos):
    for x in range(nodos):
        create_set(x)
    cont = 0
    u = []
    for x in graph:
        if find(x[0]) != find(x[1]):
            union(x[0],x[1])
            cont += x[2]
            
        else:
            u.append(x[2])
    return u 
def main():
    global graph, padre, rango 
    nodos,aristas = [int(x) for x in stdin.readline().strip().split()]
    while nodos:
        graph = []
        padre = {}
        rango = {}
        for x in range(aristas):
            a = [int(x) for x in stdin.readline().strip().split()]
            graph.append(a)
        graph.sort(key = lambda r:r[2])
        solution = kruskal(nodos)
        if solution == []:
            print('forest')
        else:
            solution.sort()
            print(*solution)
        nodos,aristas = [int(x) for x in stdin.readline().strip().split()]
main()
