import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353;sys.setrecursionlimit(10000000)
for _ in range(I()):
	n=I()
	b=L();f=0
	for i in range(1,n):
		if b[i-1]%b[i]!=0:
			f=1
			break
	if f==1:
		print(-1)
	else:
		print(*b)