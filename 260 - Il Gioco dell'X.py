from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(100000000)
def dfs(x,w):
    posx = [-1,-1,0,0,1,1]
    posy = [-1,0,-1,1,0,1]
    flag = False
    for z in range(6):
        nposx = x + posx[z]
        nposy = w + posy[z]
        if 0 <= nposx < n and 0 <= nposy < n and visitados[nposx][nposy] == False and graph[nposx][nposy] == 'b':
            visitados[nposx][nposy] = True
            dfs(nposx,nposy)
def main():
    global n , graph , visitados 
    n = int(stdin.readline().strip())
    caso = 1
    while n:
        flag = False
        visitados = []
        for u in range(n):
            visitados.append([False]*n)
        graph = []
        for e in range(n):
            a = stdin.readline().strip()
            graph.append(a)
        for w in range(n):
            if graph[0][w] == 'b':
                visitados[0][w] = True
                dfs(0,w)
        for x in range(n):
            if visitados[n-1][x] == True:
                flag = True
                break
        if flag:
            print(caso,'B')
        else:
            print(caso,'W')
        caso += 1
        n = int(stdin.readline().strip())
main()
