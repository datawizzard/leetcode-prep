import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
c1=arr[0]-1
c2=arr[0]-1
x=arr[-1]**(1/float(n-1))
x1=math.ceil(x)
x2=math.floor(x)
for i in range(1,n):
	d1=abs(arr[i]-x1**i)
	c1+=d1
	d2=abs(arr[i]-x2**i)
	c2+=d2
print(min(c1,c2))

