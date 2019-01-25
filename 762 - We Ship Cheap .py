from sys import stdin
from collections import deque
def path(v):
    global graph , visitados , padre , inicial , final
    if v == inicial:
        return v
    solve.append([padre[v],v])
    return path(padre[v])

def bfs():
    global padre , visitados, inicial , final 
    visitados = set(); visitados.add(inicial)
    padre = {}; padre[inicial] = inicial
    Q = deque(); Q.append(inicial)
    while Q:
        u = Q.popleft()
        if u==final:
            return True
        for v in graph[u]:
            if not v in visitados:
                padre[v] = u
                Q.append(v)
                visitados.add(v)
    return False
    
def main():
    global inicial , final , aristas , graph , solve
    aristas =stdin.readline().strip()
    first=True
    while aristas != '':
        if not first: print()
        else: first=False
        graph = {}
        aristas = int(aristas)
        for x in range(aristas):
            a = [x for x in stdin.readline().strip().split()]
            if a[0] not in graph:
                graph[a[0]] = []
            graph[a[0]].append(a[1])
            if a[1] not in graph:
                graph[a[1]] = []
            graph[a[1]].append(a[0])
        inicial, final = [x for x in stdin.readline().strip().split()]
        solve = []
        if inicial == final:
            print(inicial,final)
        else:
            if inicial in graph and final in graph:
                solution = bfs()
                if solution:
                    path(final)
                    solve.reverse()
                    for x in solve:
                        print(*x)
                else:
                    print('No route')
            else:
                print('No route')
        stdin.readline().strip()
        aristas = stdin.readline().strip()
main()

