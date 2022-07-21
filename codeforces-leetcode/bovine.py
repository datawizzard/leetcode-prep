import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	if n<2:
		print(0)
	else:
		total=math.factorial(n)//(math.factorial(2)*math.factorial(n-2))
		# print(total)
		d=[]
		for i in range(n-1):
			for j in range(i+1,n):
				d.append(arr[j]-arr[i])
		print(total-(len(d)-len(set(d))))