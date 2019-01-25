from sys import stdin
def create_set(e):
   
    padres[e] = e
    rango[e] = 1
def find(e):
    if padres[e] == e:
        return e
    else: 
        return find(padres[e])
def union(u,v):
    ru = find(u)
    rv = find(v)
    if ru != rv:
        if rango[ru] > rango[rv]:
            padres[rv] = ru
        else:
            padres[ru] = rv
            if rango[ru] == rango[rv]:
                rango[rv] += 1
                
def main():
    global padres, rango
    a = int(stdin.readline().strip())
    for x in range(a):
        padres = {} 
        rango = {} 
        b,c = [int(x) for x in stdin.readline().strip().split()]
        for i in range(1,b+1):
            create_set(i)
        for w in range(c):
            d,f = [int(x) for x in stdin.readline().strip().split()]
            union(d,f)
        answer = 0
        fre = {}
        for i in range(1,b+1):
            ri = find(i)
            if not ri in fre:
                fre[ri] = 0
            fre[ri] += 1
            answer = max(answer,fre[ri])
        
        print(answer)
main()
            
            
            
