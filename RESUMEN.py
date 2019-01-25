"""
Resumen Grafos
_____________________________________________________________________________
"""
#Kruskal
#Entra una lista ordenada por costo que contiene
#[[incial,final,costo]]
#En caso de string se debe modificiar la str por un int
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
def kruskal(nodos): #Numero de nodos
    AristaMaximaTomada = -float('inf')
    for x in range(nodos):
        create_set(x)
    cont = 0
    n = nodos
    for x in graph:
        if find(x[0]) != find(x[1]):
            union(x[0],x[1])
            cont += x[2]
            nodos -= 1
            AristaMaximaTomada = max(AristaMaximaTomada,x[2])
    if n != 1:
        return 'No todos los nodos estan conectados'
    return cont
            
#BFS
#Se utiliza cuando todas las distancias tienen el mismo valor
#Entra un diccionario con la lista de adyacentes 
from collections import deque
def bfs(graph,inicial,final):
    padre = {}
    padre[inicial] = inicial 
    Q = deque()
    Q.append(inicial)
    visitados = set()
    visitados.add(inicial)
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if not v in visitados:
                padre[v] = u
                Q.append(v)
                visitados.add(v)
                if v == final:
                    Q.clear()
                    break
#Dijsktra
#Se utiliza un diccionario de listas de adyacencia a la cual
#Se agrega una lista con tuplas
# [Inicial:[(Final,Costo)]]
import heapq
def djk_relax(u,v,w):
    global Q,distancia, padre
    if distancia[v]  > distancia[u] + w:
        distancia[v] = distancia[u] + w
        padre[v] = u
        heapq.heappush(Q,(distancia[v],v))
    
def djk(inicial,final):
    global graph , nodos, distancia, padre , Q , inf , visitados
    visitados = set()
    inf = float('inf')
    distancia = [inf]*nodos
    padre = [None]*nodos
    distancia[inicial] = 0
    Q = []
    heapq.heappush(Q,(distancia[inicial],inicial))
    while Q:
        d,u = heapq.heappop(Q)
        for x in graph[u]:
            if x not in visitados:
                visitados.add(x)
                v = x[0]
                w = x[1]
                djk_relax(u,v,w)
    return distancia[final]

#Bellman_ford
#Entra un diccionario de lista de adyacencia con
#tupla
#[Inicial:[(Final,Costo)]]
from sys import stdin
def bell_relax(u,v,w):
    global distancia,pad
    if distancia[v] > distancia[u] + w:
        distancia[v] = distancia[u] + w
        pad[v] = u
def bell(graph,inicial):
    global inf,distancia,pad

    inf = float('inf')
    distancia = [inf]*nodos
    pad= [None]*nodos
    distancia[inicial] = 0
    for x in range(nodos-1):
        for u in graph:
            for tup in graph[u]:
                v = tup[0]
                w = tup[1]
                bell_relax(u,v,w)
    for u in graph:
        for tup in graph[u]:
            v = tup[0]
            w = tup[1]
            if distancia[v] > distancia[u] + w:
                return "Hay ciclo infinito negativo"
    return "No hay ciclo infinito"

#Floyd_warshall
#Se debe hacer una matriz de la forma:
#[[0]*nodos in range(nodos)]
def Floyd_Warshall(c,n): #all_pairs algoritmo
    fw = [[0]*n for i in range(N)]
    for i in range(n):
        for j in range(n):
            dis[i][j] = cost[i][j]    # se copia los costos en otra matriz para poder realizar floydwarshall

    #este es el algoritmo
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis[i][j] = min(cost[i][j],fw[i][k]+cost[k][j])
    return fw # la matriz con la menor distancia entre todas la parejas del grafo
#Si no hay valores:
    for x in range(nodos):
        for i in range(nodos):
            for j in range(nodos):
                if dis[i][x] == 1 and l2[x][j] == 1:
                    dis[i][j] = 1

#Toposort khan:
#Entra un diccionario con matriz de adyacencia
#Ordena nodos evitando los que no estan conectados
def toposort(graph):
    in_degree = { u:0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    Q = deque()
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)
    L = []
    while Q:
        u = Q.pop()
        L.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)
    if len(L) == len(graph):
        return L
    else:
        return []
#dfs
#Diccionario de matriz de adyancencia
#Comprueba si es posible alcancar el nodo final
def dfs(u):
    global visitados,ady,par
    visitados.add(u)
    for v in ady[u]:
        if not v in visitados:
            par[v]=u
            dfs(v)
#Path : permite devolverse por los madres para seleccionar
#elementos
def path(v):
    global graph, visitados, pad , inicial , solution
    solution.append(v)
    if v == inicial:
        return v
    return path(pad[v])
