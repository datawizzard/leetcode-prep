import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	n,x=map(int,input().split())
	arr=list(map(int,input().split()))
	i,c,pos=0,0,0
	j=i+1
	# z=min(x,n)
	while i<n-1 and c<=x:
		if arr[i]==0:
			i+=1
			j+=1
		if arr[i]!=0 and i<n-1:
			#print(i,j)
			l=int(math.log2(arr[i]))
			#print(l)
			arr[i]=arr[i]^pow(2,l)
			min1=arr[j]^pow(2,l)
			r=min1
			for j in range(i+1,n):
				#print(j,min1)
				if min1>=arr[j]^pow(2,l):
					pos=j
					min1=arr[j]^pow(2,l)
					#print(min1,"hh")
			#print(min1,r,"ff")
			print(pos)
			j=i+1
			print(j)
			if min1<=r: 
				#print("R",j)
				arr[pos]=arr[pos]^pow(2,l)
			else:
				arr[-1]=arr[-1]^pow(2,l)
			c+=1
			print(*arr,c)
	if len(arr)>2:
		print(*arr)
	else:
		if len(arr)<=2 and x%2==1:
			print(*arr)
		else:
			if arr[0]==0:
				print(arr[0]+1,arr[1]+1)
			else:
				l=int(math.log2(arr[i]))
				print(arr[0]^pow(2,l),arr[1]^pow(2,l))








	

