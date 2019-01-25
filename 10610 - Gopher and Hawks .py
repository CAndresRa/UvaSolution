from sys import stdin
from collections import deque
import math
def path(v,cont):
    global graph, visitados, padre , inicial
    if v == inicial:
        return cont-1
    else:
        return path(padre[v],cont+1)
def bob(x,w):
    global graph
    if x not in graph:
        graph[x] = []
    if w not in graph:
        graph[w] = []
    a = temp[x][0] - temp[w][0]
    b = temp[x][1] - temp[w][1]
    distancia = math.sqrt(a**2+b**2)
    if distancia <= dist:
        graph[x].append(w)
        graph[w].append(x)
        
def bfs(inicial):
    global padre
    flag = False
    inf = float('inf')
    padre = {}
    d = [inf]*len(graph)
    d[inicial] = 0
    Q = deque()
    Q.append(inicial)
    visitados = set()
    visitados.add(inicial)
    while Q:
        u = Q.popleft()
        for x in graph[u]:
            if x not in visitados:
                if d[x] == inf:
                    padre[x] = u
                    visitados.add(x)
                    d[x] = d[u] + 1
                    if x == 1:
                        return 'Yes, visiting {} other holes.'.format(path(x,0))
                        flag = True
                        break
                        Q.clear()
                    else:
                        Q.append(x)
                        
    return 'No.'
def main():
    global temp , dist, graph, inicial 
    inicial = 0
    speed,time = [int(x) for x in stdin.readline().strip().split()]
    while speed + time:
        dist = speed*time*60
        graph = {}
        temp = []
        xini,yini = [float(x) for x in stdin.readline().strip().split()]
        temp.append([xini,yini])
        for x in range(100000):
            a = [float(x) for x in stdin.readline().strip().split()]
            if a == []:
                break
            temp.append(a)
        for x in range(len(temp)):
            for w in range(x+1,len(temp)):
                bob(x,w)
       
        solution = bfs(0)
        print(solution)
        speed,time = [int(x) for x in stdin.readline().strip().split()]
main()
    
