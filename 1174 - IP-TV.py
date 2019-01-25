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
      
        union(x[0],x[1])
        cont += x[2]
    return cont
            
    
    
def main():
    global graph , padres, rango 
    a = int(stdin.readline().strip())
    for x in range(a):
        if x != 0:
            print()
        stdin.readline().strip()
        b = int(stdin.readline().strip())
        c = int(stdin.readline().strip())
        pal = {}
        numbs = {}
        padres = {}
        rango = {}
        graph = []
        cont = 0
        for x in range(c):
            d = [x for x in stdin.readline().strip().split()]
            aux = []
            for w in range(len(d)-1):
                if d[w] not in pal:
                    pal[d[w]] = cont
                    numbs[cont] = d[w]
                    cont += 1
            aux.append(pal[d[0]])
            aux.append(pal[d[1]])
            aux.append(int(d[2]))
            graph.append(aux)
        graph.sort(key=lambda r:r[2])
        print(kruskal(b))
       
        
            
main()
            
            
    
