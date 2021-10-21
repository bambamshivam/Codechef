import math;from heapq import heappush,heappop,heapify;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m=M();adj=[[] for i in range(n)];ind=[0]*n
	for i in range(m):
		a,b=M()
		adj[a-1].append(b-1)
		adj[b-1].append(a-1)
		ind[a-1]+=1
		ind[b-1]+=1
	ans=[0]*n
	def exis(mid):
		a=ind[:]
		c=[-1]*n
		p=n;q=deque()
		for i in range(n):
			if a[i]<=mid:
				q.append(i)
				c[i]=p
				p-=1
		while q:
			r=q.popleft()
			for j in adj[r]:
				a[j]-=1
				if a[j]<=mid and c[j]==-1:
					c[j]=p
					p-=1
					q.append(j)
		for i in c:
			if i==-1:
				return False
		for i in range(n): ans[i]=c[i]
		return True
	opt=n
	l=0;r=n
	while l<=r:
		mid=(l+r)//2
		if exis(mid):
			opt=mid
			r=mid-1
		else:
			l=mid+1
	print(opt)
	print(*ans)