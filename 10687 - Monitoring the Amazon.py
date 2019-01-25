from sys import stdin
import math
def dfs(u):
    global visitados,pares
    visitados.add(u)
    v=0
    
    estacion=u
    for k in range(2):   
        maximo=math.inf
        for i in range(len(pares)):
            if pares[i]!=u and pares[i]!=v:
                distancia=((u[0]-pares[i][0])**2 + (u[1]-pares[i][1])**2)**(1/2)
                if distancia<maximo:
                    maximo=distancia
                    estacion=pares[i]
                elif distancia==maximo:
                    if pares[i][0]<estacion[0]:
                        estacion=pares[i]
                    elif pares[i][1]<estacion[1]:
                        estacion=pares[i]
        v=estacion
        if not v in visitados:
            dfs(v)
def main():
    global pares,visitados
    n=int(stdin.readline())
    while n!=0:
        if n==1:
            lista=[int(x) for x in stdin.readline().split()]
            print("All stations are reachable.")
            n=int(stdin.readline())
        else:   
            visitados=set()
            lista=[int(x) for x in stdin.readline().split()]
            pares=[]
            for i in range(0,2*n,2):
                pares.append((lista[i],lista[i+1]))
            dfs(pares[0])
            if len(visitados)==n:
                print("All stations are reachable.")
            else:
                print("There are stations that are unreachable.")
            n=int(stdin.readline())
main()
