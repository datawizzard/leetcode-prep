import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for i in range(int(input())):
	n,k=map(int,input().split())
	arr=[]
	for _ in range(n):
		p,q=map(int,input().split())
		arr.append((p,q))
	# print(arr)
	flag,ans=0,0
	for i in range(n):
		flag=0
		for j in range(n):
			# print(arr[j][0],j,end=" ")
			if abs(arr[i][0]-arr[j][0])+abs(arr[i][1]-arr[j][1])>k:
				flag=1
				break;
		if flag==00:
			ans=1
	if ans==0:
		print(-1)
	else:
		print(1)