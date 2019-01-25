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
    n = nodos 
    for x in graph:
        if find(x[0]) != find(x[1]):
            union(x[0],x[1])
            n -= 1
    return n
    
        
def main():
    global rango , padre , graph
    abc = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}    
    casos = int(stdin.readline().strip())
    stdin.readline().strip()
    for z in range(casos):
        if z != 0:
            print()
        nodos = stdin.readline().strip()
        rango = {}
        padre = {}
        graph = []
        a = stdin.readline().strip()
        while a != '':
            graph.append([abc[a[0]],abc[a[1]]])
            a = stdin.readline().strip()
        print(kruskal(abc[nodos]+1))
        
main()
