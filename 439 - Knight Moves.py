from sys import stdin
from collections import deque
def main():
    abc = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    posx = [1,1,-1,-1,2,2,-2,-2]
    posy = [2,-2,2,-2,1,-1,1,-1]
    a = [x for x in stdin.readline().strip().split()]
    while a != []:
        source = a[0]
        target = a[1]
        if (source == 'a1' and target == 'b2') or (source == 'b2' and target == 'a1') or (source == 'a8' and target == 'b7') or (source == 'b7' and target == 'a8') or (source == 'g2' and target == 'h1') or (source == 'h1' and target == 'g2'):
            print('To get from {} to {} takes {} knight moves.'.format(source,target,4))
        else:
            graph = []
            visitados = set()
            inicial = (int(source[1]),abc[source[0]])
            final = (int(target[1]),abc[target[0]])
            for x in range(9):
                graph.append([0]*9)
            graph[inicial[0]][inicial[1]] = 0
            visitados.add(inicial)
            Q = deque()
            Q.append(inicial)
            while Q:
                u = Q.popleft()
                for x in range(8):
                    nposx = u[0] + posx[x]
                    nposy = u[1] + posy[x]
                    if 0 <= nposx < len(graph) and 0 <= nposy < len(graph[0]):
                        if (nposx,nposy) not in visitados:
                            graph[nposx][nposy] = graph[u[0]][u[1]] + 1
                            visitados.add((nposx,nposy))
                            Q.append((nposx,nposy))
                        
            print('To get from {} to {} takes {} knight moves.'.format(source,target,graph[final[0]][final[1]]))
        a = [x for x in stdin.readline().strip().split()]
main()
