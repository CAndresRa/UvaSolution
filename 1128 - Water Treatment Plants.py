from sys import stdin
def water(a):
    global dp
    if a in dp:
        return dp[a]
    else:
        if a == 1:
            dp[a] = 1
            return dp[a]
        if a == 2:
            dp[a] = 3
            return dp[a]
        if a == 3:
            dp[a] = 8
            return dp[a]
        if a > 3:
            dp[a] = 3*water(a-1) - water(a-2)
            return dp[a]
    
def main():
    global dp
    dp = {}
    a = stdin.readline().strip()
    while a != '':
        a = int(a)
        print(water(a))
        a = stdin.readline().strip()
main()
