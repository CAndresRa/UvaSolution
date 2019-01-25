from sys import stdin
def dfs(i,color):
    global flag
    
    if visitados[i] == False:
        visitados[i] = color
        if visitados[i] == 'Azul':
            color = 'Rojo'
        elif visitados[i] == 'Rojo':
            color = 'Azul'
    for j in adyacentes[i]:
        if visitados[j] == False:
            dfs(j,color)
        elif visitados[j] == visitados[i]:
            flag = False

def main():
    global adyacentes, visitados , flag
    
    n_nodos = int(stdin.readline().strip())
    while n_nodos:
        flag = True
        visitados = [False]*n_nodos
        n_aristas = int(stdin.readline().strip())
        adyacentes = [list() for x in range(n_nodos)]
        for x in range(n_aristas):
            u,v = [int(x) for x in stdin.readline().strip().split()]
            adyacentes[u].append(v)
            adyacentes[v].append(u)
        dfs(0,'Azul')
        if flag:
            print('BICOLORABLE.')
        else:
            print('NOT BICOLORABLE.')
        n_nodos = int(stdin.readline().strip())
main()
