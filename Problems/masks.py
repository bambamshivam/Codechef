for _ in range(int(input())):
	n,x,y,z=map(int,input().split())
	di={}
	di[10]=x/10
	di[5]=y/5
	di[1]=z
	di1={}
	di1[10]=x
	di1[5]=y
	di1[1]=z
	di=sorted(di.items(), key = lambda kv:(kv[1], kv[0]))
	c=0
	while n>0:
		for ke in di:
			if ke[0]<=n:
				p=n//ke[0]
				n-=(p*ke[0])
				c+=(p*di1[ke[0]])
				break
			else:
				continue
	print(c)

