from sys import stdin
def main():
    casos = int(stdin.readline().strip())
    for z in range(casos):
        palabra = stdin.readline().strip()
        solution = []
        contA = 0
        contM = 0
        contR = 0
        contG = 0
        contT = 0
        contI = 0
        for x in palabra:
            if x == 'A':
                contA += 1
            if x == 'M':
                contM += 1
            if x == 'R':
                contR += 1
            if x == 'T':
                contT += 1
            if x == 'I':
                contI += 1
            if x == 'G':
                contG += 1

        A = contA//3
        R = contR//2
        T = contT//1
        G = contG//1
        I = contI//1
        M = contM//1
        solution.append(M)
        solution.append(A)
        solution.append(R)
        solution.append(G)
        solution.append(I)
        solution.append(T)
        print(min(solution))
main()
                
                
            
        
