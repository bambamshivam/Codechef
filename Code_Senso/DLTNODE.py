import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
sys.setrecursionlimit(10000000)
for _ in range(I()):
	n=I()
	adj=[[] for i in range(n)]
	for i in range(n-1):
		a,b=M()
		adj[a-1].append(b-1)
		adj[b-1].append(a-1)
	v=L()
	def solve(i,p):
		g[i]=v[i]
		for j in adj[i]:
			if j!=p:
				solve(j,i)
				g[i]=math.gcd(g[i],g[j])
	g=[0]*n;solve(0,-1)
	def dfs(i,p,gp):
		d=gp
		a=[];b=[];child=[]
		for j in adj[i]:
			if j!=p:
				d+=g[j]
				a.append(g[j]);b.append(g[j])
				child.append(j)

		ans[0]=max(ans[0],d);t=len(a)
		for j in range(1,t):
			a[j]=math.gcd(a[j],a[j-1])
		for j in range(t-2,-1,-1):
			b[j]=math.gcd(b[j],b[j+1])
		
		for k in range(t):
			ngp=math.gcd(gp,v[i])
			if k>0:
				ngp=math.gcd(ngp,a[k-1])
			if k<t-1:
				ngp=math.gcd(ngp,b[k+1])
			dfs(child[k],i,ngp)
	ans=[0];dfs(0,-1,0)
	print(ans[0])