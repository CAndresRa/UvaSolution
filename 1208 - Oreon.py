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
    cont = 0
    for x in graph:
        if find(x[0]) != find(x[1]):
            union(x[0],x[1])
            print('{}-{} {}'.format(namenode[x[0]],namenode[x[1]],x[2]))
            cont += x[2]
    return cont
            
def main():
    global graph,rango,padres,namenode
    namenode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    cases = int(stdin.readline().strip())
    for x in range(cases):
        print('Case {}:'.format(x+1))
        aristas = int(stdin.readline().strip())
        graph = []
        rango = {}
        padres = {}
        for z in range(aristas):
            a = [int(x) for x in stdin.readline().strip().split(',')]

            for w in range(len(a)):
                aux = []
                if a[w] != 0:
                    aux.append(z)
                    aux.append(w)
                    aux.append(a[w])
                if aux != []:
                    graph.append(aux)
        graph.sort(key=lambda r:r[2])
        
        kruskal(aristas)
main()
                
            
            
            
