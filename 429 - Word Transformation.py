from sys import stdin
from collections import deque

def valido(s1,s2):
    if len(s1) != len(s2):
        return False
    diferencias = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diferencias += 1
    return diferencias == 1

def main():
    casos = int(stdin.readline())
    stdin.readline()
    for x in range(casos):
        words = []
        pal = stdin.readline().strip()
        words.append(pal)
        while pal != '*':
            words.append(pal)
            pal = stdin.readline().strip()
        dic = {}
        for s1 in words:
            for s2 in words:
                if valido(s1,s2):
                    if s1 not in dic:
                        dic[s1] = []

                    dic[s1].append(s2)

                    if s2 not in dic:
                        dic[s2] = []
                    dic[s2].append(s1)
        if x>0: print()
        q = stdin.readline().strip().split()
        while q:
            ini = q[0]
            fin = q[1]
            vis = set()
            vis.add(ini)
            queue = deque()
            queue.append((ini,0))
            ans = -1
            while queue:
                dato = queue.popleft()
                if dato[0] == fin:
                    ans = dato[1]
                    break
                elif dato[0] in dic:
                    for v in dic[dato[0]]:
                        if v not in vis:
                            vis.add(v)
                            queue.append((v,dato[1]+1))
                        
            print(ini+" "+fin+" "+str(ans))
            q = stdin.readline().strip().split()

main()
