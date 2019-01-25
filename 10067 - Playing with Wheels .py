from sys import stdin
from collections import deque
lints = []
lindex = 0

def next_int():
    global lints , lindex
    if lindex < len(lints):
        lindex += 1
        return lints[lindex-1]
    else:
        lints = [int(s) for s in stdin.readline().split()]
        lindex = 0
        return next_int()
    
        
def constructor():
    global adj
    adj = dict()
    for i in range(10000):
        s = "{0:04d}".format(i)
        adj[s] = []
        for j in range(4):
            d = s[j]
            for x in [-1,1]:
                c = str((int(d)+x)%10)
                t = s[0:j] + c + s[j+1:4]
                adj[s].append(t)

    
def main():
    constructor()
    a = int(stdin.readline().strip())
    for x in range(a):
        vis = set()
        par = {}
        v0 =  ''
        for i in range(4): v0 = v0 + str(next_int())
        vf = ''
        for i in range(4): vf = vf + str(next_int())
        n = next_int()
        for i in range(n):
            u = ''
            for i in range(4):
                u = u + str(next_int())
            vis.add(u)
        Q = deque()
        Q.append(v0)
        vis.add(v0)
        par[v0] = v0
        while Q:
            u = Q.popleft()
            for v in adj[u]:
                if not v in vis:
                    vis.add(v)
                    par[v] = u
                    Q.append(v)
                    if v == vf:
                        Q.clear()
                        break
        if vf in par:
            cost = 0
            u = vf
            while par[u] != u:
                cost += 1
                u = par[u]
        else:
            cost = -1
        print(cost)

            
main()
