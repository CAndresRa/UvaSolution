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
    solution = float('inf')
    for x in range(1,nodos+1):
        create_set(x)
    cont = 0
    n = nodos
    for x in graph:
        if x[2] >= totalcost:
            break
        if find(x[0])  != find(x[1]):
            union(x[0],x[1])
            cont += x[2]
            n -= 1
         
    if n != 1:
        resp = totalcost*(n) + cont
        
    else:
        resp = totalcost + cont 
    return (resp,n)
def main():
    global graph , padre , rango , totalcost
    
    casos = int(stdin.readline().strip())
    for x in range(casos):
        graph = []
        padre = {}
        rango = {}
        locations,roads,totalcost = [int(x) for x in stdin.readline().strip().split()]
        for w in range(roads):
            a = [int(x) for x in stdin.readline().strip().split()]
            graph.append(a)
        graph.sort(key = lambda r:r[2])
        solution = kruskal(locations)
        print('Case #{}: {} {}'.format(x+1,solution[0],solution[1]))
main()
        
            
