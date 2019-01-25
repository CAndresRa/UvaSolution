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
    for x in range(1,nodos+1):
        create_set(x)
    cont = 0
    for d,u,v in distancias:
        if find(u) != find(v):
            union(u,v)
            cont += d
    return cont 
def distancia(a,b):
    dis = ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)
    return dis
def main():
    global padres, rango , distancias
    casos = int(stdin.readline().strip())
    for x in range(casos):
        if x != 0:
            print()
        stdin.readline().strip()
        padres = {}
        rango = {}
        nodos = int(stdin.readline().strip())
        lnodos = []
        for x in range(nodos):
            a = [float(x) for x in stdin.readline().strip().split()]
            nodo = [a[0],a[1]]
            lnodos.append(nodo)
        distancias = []
        for i in range(nodos):
            for j in range(i+1,nodos):
                coorx = lnodos[i]
                coory = lnodos[j]
                dis = distancia(coorx,coory)
                distancias.append([dis,i+1,j+1])
                distancias.append([dis,j+1,i+1])
        distancias.sort()
        resp = kruskal(nodos)
        print('{:.2f}'.format(resp))
            
main()
