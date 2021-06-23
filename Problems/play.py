for _ in range(int(input())):
	l=list(map(int,input().split()))
	m=max(l)
	i=l.index(m)
	l[i]=-1
	m2=max(l)
	j=l.index(m2)
	if (i+j==1) or (i+j==5):
		print("NO")
	else:
		print("YES")


