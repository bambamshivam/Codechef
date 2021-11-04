import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,q=M()
	adj=[[] for i in range(n)];d={}
	for i in range(n-1):
		a,b=M();a-=1;b-=1
		adj[a].append(b)
		adj[b].append(a)
	def bfs(i):
		q=deque()
		q.append(i)
		v[i]=1
		while q:
			r=q.pop()
			for j in adj[r]:
				if v[j]==0:
					q.append(j)
					v[j]=1
					b[j]=b[r]^1
					if len(adj[j])==1 and b[j]==0:
						if len(adj[r])==2 and d.get(r,0)==0:
							c[0]+=1
							d[r]=1
						a[0]+=1
	v=[0]*n;a=[0];c=[0];b=[0]*n;bfs(0)
	if q==1:
		t1=abs(b.count(1)-b.count(0))
		t2=abs(b.count(1)-b.count(0)+2*a[0])
		print(max(t1,t2))
	else:
		g=b.count(0);h=b.count(1)
		m=abs(g-h)
		for i in range(a[0]):
			g-=1
			h+=1
			m=min(abs(g-h),m)
		for i in range(c[0]):
			g+=1
			h-=1
			m=min(abs(g-h),m)
		print(m)