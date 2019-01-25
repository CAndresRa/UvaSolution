from sys import stdin
from collections import deque
def heapify(lst,i):
    n=len(lst)
    p = i
    izq = i*2
    der = i*2+1
    if izq < n and lst[izq] < lst[p]:
        p = izq
    if der < n and lst[der] < lst[p]:
        p = der
    if p != i:
        lst[p],lst[i]=lst[i],lst[p]
        heapify(lst,p)
    
def extract_min(lst):
    menor = lst[1]
    lst[1] = lst[len(lst)-1]
    lst.pop()
    heapify(lst,1)
    return menor
def main():
    while True:
        costo=0
        n=int(stdin.readline().strip())
        if not n:
            break
        lst=[None]
        r=list(map(int,stdin.readline().strip().split()))
        lst+=r
        if n==1:
            print(0)
        else:
            for i in range(n//2,0,-1):
                heapify(lst,i)

            while len(lst)>2:
                minimo = extract_min(lst)
                lst[1] += minimo
                costo+=lst[1]
                heapify(lst,1)
            if len(lst)==2: 
                print(costo)
            else:
                print(lst[-1])
                
                
        
main()
        
