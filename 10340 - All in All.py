from sys import stdin
def main():
    a = [x for x in stdin.readline().strip().split()]
    while a != []:
        a1 = a[0]
        a2 = a[1]
        r = ""
        for x in range(len(a2)):
            if a2[x] in a1:
                if a1.count(a2[x]) <= a2.count(a2[x]):
                    r = r + a2[x]

        if r == "":
            print("No")
        elif r[0] == a1[0] and r[-1] == a1[-1]:
            print("Yes")
        else:
            print("No")
            
        a = [x for x in stdin.readline().strip().split()]
main()
        
