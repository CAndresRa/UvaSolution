from sys import stdin
def main():
    casos = int(stdin.readline().strip())
    for z in range(casos):
        objetos = int(stdin.readline().strip())
        dp = [0]*31
        for x in range(objetos):
            precio,peso = [int(x) for x in stdin.readline().strip().split()]
            for w in range(30,peso-1,-1):
                if dp[w] < dp[w-peso] + precio:
                    dp[w] = dp[w-peso] + precio
        grupo = int(stdin.readline().strip())
        cont = 0
        for x in range(grupo):
            persona = int(stdin.readline().strip())
            cont += dp[persona]
        print(cont)   
main()
