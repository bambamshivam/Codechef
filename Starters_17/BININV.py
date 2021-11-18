import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353;sys.setrecursionlimit(10000000)
for _ in range(I()):
	n,m=M();l=[]
	for i in range(n):
		s=S()
		c=s.count('1')
		l.append([c,s])
	l.sort();s=""
	for i in range(n):
		s+=l[i][1]
	z=s.count('0')
	ans=c=0
	for i in range(len(s)):
		if s[i]=='0':
			c+=1
		else:
			ans+=(z-c)
	print(ans)