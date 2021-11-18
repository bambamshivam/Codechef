import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353;sys.setrecursionlimit(10000000)
for _ in range(I()):
	n=I()
	s=S()
	i=0;a=""
	if s=='1'*n or s=='0'*n:
		print("Bob");continue
	if s.count('0')==1 or s.count('1')==1:
		print("Alice");continue
	def pri(c):
		if c==0:
			print("Alice")
		else:
			print("Bob")
	while i<n:
		j=i+1
		while j<n and s[j]==s[i]:
			j+=1
		a+=s[i]
		i=j
	c=1
	if len(a)==2:
		t=n-4
		if t%2==0:
			pri(1)
		else:
			pri(0)
		continue
	if (n-len(a))%2==0:
		c=0
	if len(a)==1:
		pri((c+1)%2)
	elif len(a)<=3:
		pri(c)
	else:
		t=len(a)-3
		if t%2==0:
			pri(c)
		else:
			pri((c+1)%2)