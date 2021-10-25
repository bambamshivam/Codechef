def findClosest(arr, target):
    n=len(arr)
    if (target <= arr[0]):
        return arr[0]
    if (target >= arr[n - 1]):
        return arr[n - 1]
    i = 0; j = n; mid = 0
    while (i < j):
        mid = (i + j) // 2
 
        if (arr[mid] == target):
            return arr[mid]
        if (target < arr[mid]) :
            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr[mid - 1], arr[mid], target)
            j = mid
        else :
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr[mid], arr[mid + 1], target)
            i = mid + 1
    return arr[mid]

def getClosest(val1, val2, target):
 
    if (target - val1 >= val2 - target):
        return val2
    else:
        return val1


n,q=map(int,input().split())
l=list(map(int,input().split()))
f=0
if n%2==0:
	f=1

l.sort()
di={}
for i in range(n):
	di[l[i]]=i
for j in range(q):
	x=int(input())
	v=findClosest(l,x)
	i=0
	k=di[v]
	if v==0:
		if x<=l[0]:
			i=0
		else:
			i=1
	elif v==l[-1]:
		if x<=l[-1]:
			i=n-1
		else:
			i=n
	elif l[k]==x:
		i=k
	elif l[k-1]<x<l[k]:
		i=k
	elif l[k]<x<l[k+1]:
		i=k+1
	if i<n and l[i]==x:
		print(0)
	elif i%2==0:
		if f==1:
			print("POSITIVE")
		else:
			print("NEGATIVE")
	else:
		if f==1:
			print("NEGATIVE")
		else:
			print("POSITIVE")