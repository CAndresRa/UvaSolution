from sys import stdin
def floyd():
    for x in range(26):
        for i in range(26):
            for j in range(26):
                if l1[i][x] == 1 and l1[x][j] == 1:
                    l1[i][j] = 1
    for x in range(26):
        for i in range(26):
            for j in range(26):
                if l2[i][x] == 1 and l2[x][j] == 1:
                    l2[i][j] = 1
    if l1 == l2:
        return 'YES'
    else:
        return 'NO'
def main():
    global l1,l2
    casos = int(stdin.readline().strip())
    ABC = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    for x in range(casos):
        if x != 0:
            print()
        stdin.readline().strip()
        l1 = [[0]*26 for i in range(26)]
   
        l2 = [[0]*26 for i in range(26)]
       
        nodos1 = int(stdin.readline().strip())
        for w in range(nodos1):
            a,b = [x for x in stdin.readline().strip().split()]

            l1[ABC[a]][ABC[b]] = 1
            l1[ABC[b]][ABC[a]] = 1
        nodos2 = int(stdin.readline().strip())
        for w in range(nodos2):
            c,d = [x for x in stdin.readline().strip().split()]
            l2[ABC[c]][ABC[d]] = 1
            l2[ABC[d]][ABC[c]] = 1
        print(floyd())
        
main()
            
