from sys import stdin
def toposort():
    global graph , ceros , arcos
    cola = []
    orden = []
    for i in ceros:
        cola.append(i)
    while cola:
        cola.sort()
        u = cola.pop(0)
        for v in graph[u]:
            arcos[v] -= 1
            if arcos[v] == 0:
                cola.append(v)
        orden.append(u)
        graph[u] = []
        stdin.readline().strip()
    return orden

def main():
    global graph, ceros , arcos
    casos = int(stdin.readline().strip())
    for x in range(casos):
        graph = {}
        arcos = {}
        ceros = set()
        stdin.readline().strip()
        nodos, tareas = [int(x) for x in stdin.readline().strip().split()]
        for w in range(1,nodos+1):
            graph[w] = []
            arcos[w] = 0
            ceros.add(w)
        for w in range(tareas):
            a = [int(x) for x in stdin.readline().strip().split()]
            for z in range(2,len(a)):
                graph[a[z]].append(a[0])
                arcos[a[0]] = arcos[a[0]]+1
                if a[0] in ceros:
                    ceros.remove(a[0])
        solution = toposort()
        print(*toposort())
                
                
main()
            
