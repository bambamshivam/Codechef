for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	i=1
	j=n-2
	c=0
	while i<=j:
		while i<j and l[i]>l[i-1]:
			i+=1
		while i<j and l[j]>l[j+1]:
			j-=1
		if i<j:
			if l[i-1]>l[j+1]:
					c+=l[j+1]+1-l[j]
					l[j]=l[j+1]+1
					j-=1
			elif l[i-1]<l[j+1]:
				c+=l[i-1]+1-l[i]
				l[i]=l[i-1]+1
				i+=1
			else:
				if l[i-1]+1-l[i]>l[j+1]+1-l[j]:
					c+=l[j+1]+1-l[j]
					l[j]=l[j+1]+1
					j-=1
				elif l[i-1]+1-l[i]<l[j+1]+1-l[j]:
					c+=l[i-1]+1-l[i]
					l[i]=l[i-1]+1
					i+=1
		elif i==j:
			if l[i]>l[i-1] and l[j]>l[j+1]:
				break
			else:
				c+=max(l[i-1],l[j+1])+1-l[i]
				break
	print(c)



