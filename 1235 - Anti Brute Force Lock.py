from sys import stdin
from collections import deque
def find(n):
    global par,rank
    if par[n]==n:return n
    return find(par[n])
def union(u,v):
    global par,rank
    ru=find(u)
    rv=find(v)
    if ru!=rv:
        if rank[ru]>rank[rv]:
            par[rv]=ru
        else:
            par[ru]=rv
            if rank[ru]==rank[rv]:
                rank[rv]+=1
        return True
    return False

def main():
    global par,rank
    dic={}
    for x in range(10):
        vis=set()
        vis.add(str(x))
        pila=deque()
        pila.append(x)
        contador={str(x):0}
        cont=0
        while len(pila)>0:
            cont+=1
            for y in range(len(pila)):
                u=pila.popleft()
                for k in [-1,1]:
                    t=((int(u)+k)%10)
                    if str(t) not in vis:    
                        vis.add(str(t))
                        pila.append(str(t))
                        contador[str(t)]=cont
        dic[str(x)]=contador
    for x in range(int(stdin.readline())):
        lista=deque(stdin.readline().strip().split())
        K=lista.popleft()
        acumulado=100
        for x in lista:
            s=dic["0"][x[0]]+dic["0"][x[1]]+dic["0"][x[2]]+dic["0"][x[3]]
            if s<acumulado:
                acumulado=s
                p=x
        par={}
        lis=[]
        rank={}
        dic2={}
        for x in range(len(lista)):
            par[x]=x
            rank[x]=1
            dic2[lista[x]]=x
        for x in range(len(lista)-1):
            z=lista[x]
            for y in range(x+1,len(lista)):
                x=lista[y]
                P=dic[z[0]][x[0]]+dic[z[1]][x[1]]+dic[z[2]][x[2]]+dic[z[3]][x[3]]
                lis.append([P,z,x])
        lis.sort()
        cont=2
        for x in lis:
            if union(dic2[x[1]],dic2[x[2]]):
                cont+=1
                acumulado+=x[0]
                if cont==K: break

        print(acumulado)

main()
