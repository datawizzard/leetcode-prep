import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	n,x=map(int,input().split())
	arr=list(map(int,input().split()))
	min1,max1=0,0
	min1=math.ceil(sum(arr)/x)
	max1=sum(math.ceil(i/x) for i in arr)
	print(min1,max1)