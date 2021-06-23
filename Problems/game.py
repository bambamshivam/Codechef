import math
def prime(x):
    if x == 1:
        return False
    elif x%2==0 or x%3==0:
        return False
    else:
        for i in range(5, int(math.sqrt(x)) + 1,2):
            if (x % i == 0):
                return False
        else:
            return True
i=1
l=[2,3]
while(len(l)!=10**5+1):
    if prime(i)==True:
        l.append(i)
    i+=1

def computeXOR(n) :
    if n % 4 == 0 :
        return n
    if n % 4 == 1 :
        return 1
    if n % 4 == 2 :
        return n + 1
    return 0

for _ in range(int(input())):
        n=int(input())
        print(computeXOR(l[n-1]))
