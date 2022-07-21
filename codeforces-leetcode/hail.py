import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	n,x=map(int,input().split())
	arr=list(map(int,input().split()))
	i,c,pos=0,0,0
	j=1
	# z=min(x,n)
	while i<n-1 and c<x:
		if arr[i]!=0:
			l=int(math.log2(arr[i]))
			arr[i]=arr[i]^pow(2,l)
			flag=0
			for j in range(i+1,n):
				#print(j,min1)
				if arr[j]^pow(2,l)<arr[j]:
					pos=j
					flag=1
					break;
			if flag==1:
				arr[pos]=arr[pos]^pow(2,l)
			else:
				arr[-1]=arr[-1]^pow(2,l)
			c+=1
			j=i+1
		if arr[i]==0:
			i+=1
			j+=1
		print(*arr,c,i)
	if n>2:
		print(*arr)
	else:
		if n<=2 and (x-c)%2==0 and c<x:
			print(*arr)
		elif n<=2 and (x-c)%2==1 and c<x:
			if arr[0]==0:
				print(arr[0]^pow(2,0),arr[1]^pow(2,0))
			else:
				l=int(math.log2(arr[i]))
				print(arr[0]^pow(2,l),arr[1]^pow(2,l))
		else:
			print(*arr)