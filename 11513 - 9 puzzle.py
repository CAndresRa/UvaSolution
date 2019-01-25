import sys
from collections import deque

def bfs(src):
    global dist, path
    dist[src]=0;
    q= deque(); q.append((src,0))
    path[src]=''
    while q:
        u,d = q.popleft()
        for i in range(0,9,3):
            v=u[:i]+u[i+1:i+3]+u[i]+u[i+3:]
            if v not in dist:
                dist[v]=dist[u]+1
                path[v]='H'+str(i//3+1)+path[u]
                q.append((v,dist[v]))
        newU=[]
        for i in range(0,9,3):
            newU.append(list(u[i:i+3]))
        for j in range(3):
            tmpU=[[],[],[]]
            for h in range(3):
                for k in range(3):
                    tmpU[h].append(newU[h][k])        
            tmpU[0][j],tmpU[2][j]=tmpU[2][j],tmpU[0][j]
            tmpU[1][j],tmpU[2][j]=tmpU[2][j],tmpU[1][j]
            v=''
            for x in range(3):
                v+=''.join(tmpU[x])
            if v not in dist:
                dist[v]=dist[u]+1
                path[v]='V'+str(j+1)+path[u]
                q.append((v,dist[v]))
        
def main():
    global dist, path
    dist=dict(); path=dict()
    bfs('123456789')
    l=[int(x)for x in sys.stdin.readline().strip().split()]
    while l[0]:
        tgt=''.join(str(x)for x in l)
        for i in range(2):
            l=[int(x)for x in sys.stdin.readline().strip().split()]
            tgt+=''.join(str(x)for x in l)
        if tgt not in dist:
            print('Not solvable')
        else:
            print(dist[tgt],path[tgt])
        l=[int(x)for x in sys.stdin.readline().strip().split()]
main()
