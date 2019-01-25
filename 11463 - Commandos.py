from sys import stdin
def floyd(graph):
    for z in range(nodos):
        for x in range(nodos):
            for w in range(nodos):
                graph[x][w] = min(graph[x][w],graph[x][z]+graph[z][w])

    time = 0
    for x in range(nodos):
        if graph[source][x] != inf and graph[x][target] != inf:
            time = max(time,graph[source][x]+graph[x][target])
    return time
def main():
    global nodos,source, target,inf
    inf = float('inf')
    casos = int(stdin.readline().strip())
    cont = 0
    for x in range(casos):
        cont += 1
        nodos = int(stdin.readline().strip())
        graph = [[inf]*nodos for x in range(nodos)]
        for i in range(nodos):
            graph[i][i] = 0
        aristas = int(stdin.readline().strip())
        for z in range(aristas):
            a,b = [int(x) for x in stdin.readline().strip().split()]
            graph[a][b] = 1
            graph[b][a] = 1
        source,target = [int(x) for x in stdin.readline().strip().split()]
        time = floyd(graph)
        print('Case {}: {}'.format(cont,time))
        
        
main()
