for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	c=1
	for i in range(n):
		if l[i]%2==0:
			c*=2
	print(3**n - c)
