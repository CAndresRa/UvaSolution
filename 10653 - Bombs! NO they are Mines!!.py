from sys import stdin
from collections import deque
def main():
    n,m = [int(x) for x in stdin.readline().strip().split()]
    while n != 0:
        minas = int(stdin.readline().strip())
        vis = set()
        dis = []
        for x in range(n):
            dis.append([0]*m)
        for x in range(minas):
            a = [int(x) for x in stdin.readline().strip().split()]
            for w in range(2,len(a)):
                vis.add((a[0],a[w]))
        
        inix,iniy = [int(x) for x in stdin.readline().strip().split()]
        finx,finy = [int(x) for x in stdin.readline().strip().split()]
        inicial = (inix,iniy)
        final = (finx,finy)

        posx = [-1,1,0,0]
        posy = [0,0,-1,1]
        vis.add(inicial)
        dis[inix][iniy] = 0
        Q = deque()
        Q.append(inicial)
        while Q:
            u = Q.popleft()
            for v in range(4):
                nposx = u[0] + posx[v]
                nposy = u[1] + posy[v]
                if 0 <= nposx < n and 0 <= nposy < m:
                    if not (nposx,nposy) in vis:
                        dis[nposx][nposy] = dis[u[0]][u[1]] + 1
                        vis.add((nposx,nposy)) 
                        Q.append((nposx,nposy))
                    if (nposx,nposy) == final:
                        Q.clear()
                        break
        if inicial != final and dis[finx][finy] == 0:
            print(-1)
        else:
            print(dis[finx][finy])                 
        n,m = [int(x) for x in stdin.readline().strip().split()]

main()
