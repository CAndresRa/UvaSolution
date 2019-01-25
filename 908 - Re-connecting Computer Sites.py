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
    for x in range(1,nodos+1):
        create_set(x)
    cont = 0
    for x in graph:
        if find(x[0]) != find(x[1]):
            union(x[0],x[1])
            cont += x[2]
    return cont
def main():
    global graph , rango , padre 
    nodos = stdin.readline().strip()
    while nodos != '':
        nodos = int(nodos)
        cont = 0
        graph = []
        padre = {}
        rango = {}
        for x in range(nodos-1):
            a = [int(x) for x in stdin.readline().strip().split()]
            cont += a[2]
        nodos2 = int(stdin.readline().strip())
        for x in range(nodos2):
            b = [int(x) for x in stdin.readline().strip().split()]
            graph.append(b)
        nodos3 = int(stdin.readline().strip())
        for x in range(nodos3):
            c = [int(x) for x in stdin.readline().strip().split()]
            graph.append(c)
        graph.sort(key=lambda r:r[2])
        print(cont)
        print(kruskal(nodos))
        stdin.readline().strip()
        nodos = stdin.readline().strip()
        if nodos != '':
            print()

main()
            
