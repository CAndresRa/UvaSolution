from sys import stdin
from heapq import heappush
from heapq import heappop
def diskstra(src,n):
    inf = float('inf')
    dis = [inf]*n
    dis[src] = 0
    Q = []
    heappush(Q,(dis[src],src))
    while Q:
        d,u = heappop(Q)
        for v,w in graph[u]:
            if dis[u]+w < dis[v]:
                dis[v] = dis[u] + w
                heappush(Q,(dis[v],v))
    return dis
    
def main():
    global graph
    inf = float('inf')
    casos = int(stdin.readline().strip())
    for x in range(casos):
        n,m,s,t = [int(x)  for x in stdin.readline().strip().split()]
        graph = [[] for x in range(n)]
        for w in range(m):
            a = [int(x) for x in stdin.readline().strip().split()]
            graph[a[0]].append([a[1],a[2]])
            graph[a[1]].append([a[0],a[2]])
        solution = diskstra(s,n)
       
        if solution[t] != inf:
            print('Case #{}: {}'.format(x+1,solution[t]))
        else:
            print('Case #{}: unreachable'.format(x+1))
            
            
main()
