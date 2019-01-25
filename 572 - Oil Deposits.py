from sys import stdin
def dfs(x,w):
    global graph , visitados 
    posx = [1,1,1,-1,-1,-1,0,0]
    posy = [1,0,-1,1,0,-1,1,-1]
    visitados[x][w] = True
    for z in range(8):
        nposx = x + posx[z]
        nposy = w + posy[z]
        if 0 <= nposx < f and 0 <= nposy < c and visitados[nposx][nposy] == False:
            visitados[nposx][nposy] = True
            if graph[nposx][nposy] == '@':
                dfs(nposx,nposy)

    
def main():
    global graph , visitados ,f,c
    f,c = [int(x) for x in stdin.readline().strip().split()]
    while f + c:
        graph = []
        visitados = []
        cont = 0
        for x in range(f):
            a = stdin.readline().strip()
            graph.append(a)

        for x in range(f):
            visitados.append([False]*c)
        for x in range(f):
            for w in range(c):
                if visitados[x][w] == False:
                    visitados[x][w] = True
                    if graph[x][w] == '@':
                        cont += 1
                        dfs(x,w)
        print(cont)
        f,c = [int(x) for x in stdin.readline().strip().split()]
main()
