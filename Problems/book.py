def maxSubArraySum(a,size):
      
    max_so_far = -max(a) - 1
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=maxSubArraySum(a,n)
    p=0
    for i in a:
        if i>=0:
            p=1
            break
    if p==0:
        ans=max(a)
    if ans>0:
        print("Can study - "+str(ans))
    else:
        print("Cannot study - "+str(ans))
