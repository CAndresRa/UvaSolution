from sys import stdin
def kruskal(nodos):
    for x in range(nodos):
        create_set(x)
    cont = 0
    n = nodos 
    for x in graph:
        if n == 1:
            break
        if find(x[1]) != find(x[2]):
            union(x[1],x[2])
            cont += x[0]
            n -= 1
    return cont 
    
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
    cont = 0
    n = nodos 
    for x in graph:
        if n == 1:
            break
        if find(x[1]) != find(x[2]):
            union(x[1],x[2])
            cont += x[0]
            n -= 1
    return cont 
def main():
    global graph , padres, rango
    n,b = [int(x) for x in stdin.readline().strip().split()]
    while n+b:
        graph = []
        rango = {}
        padres = {}
        conta = 0
        for x in range(b):
            a = [int(x) for x in stdin.readline().strip().split()]
            conta+=a[2]
            graph.append([a[2],a[0],a[1]])
        graph.sort(key = lambda r:r[0])
        print(conta-kruskal(n))
            
        n,b = [int(x) for x in stdin.readline().strip().split()]
        
main()
