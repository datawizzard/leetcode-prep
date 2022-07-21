import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,x,p,k=map(int,input().split())
	arr=list(map(int,input().split()))
	arr.sort()
	print(arr)
	count=0
	if arr[p-1]==x:
		print(0)
		continue
	elif k>=p and arr[p-1]>=x:
		while(arr[p-1]>x):
			arr[k-1]=x
			arr.sort()
			count+=1
			print(arr)
			#continue
	elif p>=k and arr[p-1]<=x:
		while(arr[p-1]<x):
			arr[k-1]=x
			arr.sort()
			count+=1
			print(arr)
			#continue
	else:
		count=-1
	print(count)

