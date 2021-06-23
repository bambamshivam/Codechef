for _ in range(int(input())):
	n=int(input())
	m=int(input())
	l=map(int,input().split())
	c=0
	for i in l:
		if i>=5*m and i<=55*m and i%5==0:
			c+=1
	print(c)