from sys import stdin
from collections import deque
def bfs(i1,j1,i2,j2):
    global iF, jF ,matriz, movimientos
    if i1==i2==iF and j1==j2==jF:
        return 0
    if matriz[i1][j1]=="#" or matriz[i2][j2]=="#":
        return "NO LOVE"
    Q,vis = deque(),set()
    Q.append(((i1,j1,i2,j2),0))
    vis.add((i1,j1,i2,j2))
    while len(Q)>0:
       
        u=Q.popleft()
        for k in movimientos :
            a=u[0][0]+k[0]
            b=u[0][1]+k[1]
            c=u[0][2]+k[0]
            d=u[0][3]+(k[1]*-1)
            if matriz [a][b]!="#" or matriz[c][d]!="#":
                
                if matriz[a][b]== "#":
                    a=u[0][0]
                    b=u[0][1]
                if matriz[c][d]=="#":
                    c=u[0][2]
                    d=u[0][3]
                #print(u)
                
                if(a,b,c,d) not in vis :
                    #print(a,b,c,d)
                    Q.append(((a,b,c,d),u[1]+1))
                    vis.add((a,b,c,d))
                if (a,b,c,d)==(iF,jF,iF,jF):
                    return u[1]+1
    return "NO LOVE"        
        
def main():
    global iF, jF ,matriz,movimientos
    movimientos=[(1,0),(-1,0),(0,-1),(0,1)]
    tam=[int(u) for u in stdin.readline().strip().split()]
    while len(tam)!=0:
        coords=[int(u) for u in stdin.readline().strip().split()]
        iF=coords[0]
        jF=coords[1]
        i1=coords[2]
        j1=coords[3]
        i2=coords[4]
        j2=coords[5]
        matriz=[["#" for i in range (tam[1]+2)]]
        for i in range(tam[0]):
            fila=["#"]
            lin=stdin.readline().strip()
            for k in range(len(lin)):
                fila.append(lin[k])
            fila.append("#")
            matriz.append(fila)
        matriz.append(["#" for i in range(tam[1]+2)])
##        for i in matriz:
##            print(i)
        print(bfs(i1,j1,i2,j2))
        tam=[int(u) for u in stdin.readline().strip().split()]
        
main()
        
        
    
