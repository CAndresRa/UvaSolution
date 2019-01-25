from sys import stdin
from collections import deque

def bfs(S):
    global adjMatrix,lines,value
    dis = [float("inf")]*27
    vis = set()
    dis[S] = 0
    vis.add(S)
    q = deque()
    q.append(S)
    while q:
        cur = q.popleft()
        for i in range(27):
            if adjMatrix[cur][i] and (i not in vis):
                vis.add(i)
                dis[i] = dis[cur]+1
                q.append(i)
    lines[S] = dis[26]
    

def main():
    global adjMatrix,lines,value
    caso = stdin.readline().strip()
    while caso != '':
        adjMatrix = [[False]*27 for i in range(27)]
        value = [0]*26
        lines = [0]*26
        N = int(caso)
        while N > 0:
            line = stdin.readline().strip().split()
            cur = ord(line[0][0]) - ord('A')
            v = line[1]
            to = line[2]
            for i in range(len(to)):
                nextt = to[i]
                if nextt == '*':
                    adjMatrix[cur][26] = True
                else:
                    adjMatrix[cur][ord(nextt)-ord('A')] = True
            
            line = v.split(".")
            value[cur] = int(line[0])*100 + int(line[1])
            N-=1
        for i in range(26):
            if value[i] != 0: bfs(i)

        maxi = 0
        importFrom = -1
        for i in range(26):
            stops = lines[i]-1
            v = value[i]
            while stops > 0:
                v -= v*0.05
                stops -= 1
            if v > maxi:
                maxi = v
                importFrom = i
        print("Import from {0}".format(chr(importFrom+ord("A"))))
        caso = stdin.readline().strip()
