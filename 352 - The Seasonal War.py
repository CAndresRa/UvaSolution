from sys import stdin
def dfs(x,w):
    global visitados 
    posx = [1,1,1,-1,-1,-1,0,0]
    posy = [1,0,-1,1,0,-1,1,-1]
    visitados[x][w] = True
    for z in range(8):
        nposx = x + posx[z]
        nposy = w + posy[z]
        if 0 <= nposx < tamaño and 0 <= nposy < tamaño and visitados[x][w] == False:
            if visitados[nposx][nposy] == False and graph[nposx][nposy] == '1':
                dfs(nposx,nposy)
            
def main():
    global tamaño , graph , visitados 
    tamaño = stdin.readline().strip()
    while tamaño != '':
        tamaño = int(tamaño)
        graph = []
        visitados = []
        componentesConectados = 0   
        for x in range(tamaño):
            a = stdin.readline().strip()
            graph.append(a)
        for x in range(tamaño):
            visitados.append([False]*tamaño)
        for x in range(tamaño):
            for w in range(tamaño):
                if visitados[x][w] == False and graph[x][w] == '1':
                    componentesConectados += 1
                    dfs(x,w)
        print(componentesConectados)
        tamaño = stdin.readline().strip()
main()
