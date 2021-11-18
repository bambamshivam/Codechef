import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353;sys.setrecursionlimit(10000000)
for _ in range(I()):
    n,k=M()
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    l=[1]
    for i in range(n,1,-1):
        if prime[i] and 2*i>n:
            l.append(i)
    if k<=len(l):
        print("Yes")
        print(*l[:k])
    elif n-k<=len(l):
        d=set(l[:n-k]);a=[]
        for i in range(1,n+1):
            if i not in d:
                a.append(i)
        print("Yes")
        print(*a)
    else:
        print("No")