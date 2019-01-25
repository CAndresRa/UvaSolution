from sys import stdin
from collections import deque


def bfs(inicial, p, fil, col):
    posX = [-1,1,0,0]
    posY = [0,0,-1,1]
    for x in inicial:
        vis = {x}
        cola = deque([x])
        p[x] = 0
        while cola:
            nodo = cola.popleft()
            for i in range(4):
                if 0<=nodo[0]+posX[i]<fil and 0<=nodo[1]+posY[i]<col:
                    nodoAux = (nodo[0]+posX[i], nodo[1]+posY[i])
                    b = True
                    if nodoAux in p:
                        p[nodoAux] = min(p[nodoAux], p[nodo]+1)
                        b = False
                    if maze[nodoAux[0]][nodoAux[1]] != "#":
                        if nodoAux not in vis:
                            cola.append(nodoAux)
                            vis.add(nodoAux)
                            if b:
                                p[nodoAux] = p[nodo]+1
                        elif b:
                            p[nodoAux] = min(p[nodoAux], p[nodo]+1)


def recorrido(p1, p2, fil, col):
    resul = float('inf')
    for i in range(fil):
        if maze[i][0] != "#":
            if (i,0) not in p1:
                p1[(i,0)] = float('inf')
            if (i,0) not in p2:
                p2[(i,0)] = float('inf')
            if p1[(i,0)] < p2[(i,0)]:
                resul = min(resul,p1[(i,0)])
        if maze[i][col-1] != "#":
            if (i,col-1) not in p1:
                p1[(i,col-1)] = float('inf')
            if (i,col-1) not in p2:
                p2[(i,col-1)] = float('inf')
            if p1[(i,col-1)] < p2[(i,col-1)]:
                resul = min(resul,p1[(i,col-1)])
    for j in range(col):
        if maze[0][j] != "#":
            if (0,j) not in p1:
                p1[(0,j)] = float('inf')
            if (0,j) not in p2:
                p2[(0,j)] = float('inf')
            if p1[(0,j)] < p2[(0,j)]:
                resul = min(resul,p1[(0,j)])
        if maze[fil-1][j] != "#":
            if (fil-1,j) not in p1:
                p1[(fil-1,j)] = float('inf')
            if (fil-1,j) not in p2:
                p2[(fil-1,j)] = float('inf')
            if p1[(fil-1,j)] < p2[(fil-1,j)]:
                resul = min(resul,p1[(fil-1,j)])
    return resul


def main():
    global maze
    casos = int(stdin.readline())
    while casos:
        fil, col = [int(x) for x in stdin.readline().split()]
        maze = []
        person, fire = [], []
        for i in range(fil):
            maze.append(stdin.readline().strip())
            for j in range(col):
                if maze[i][j] == "J":
                    person.append((i,j))
                elif maze[i][j] == "F":
                    fire.append((i,j))
        parents1 = {}
        parents2 = {}
        bfs(person, parents1, fil, col)
        bfs(fire, parents2, fil, col)
        resul = recorrido(parents1, parents2, fil, col)
        if resul == float('inf'):
            print("IMPOSSIBLE")
        else:
            print(resul+1)
        casos -= 1


main()