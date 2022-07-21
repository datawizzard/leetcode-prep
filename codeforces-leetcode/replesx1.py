import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,x,p,k=map(int,input().split())
	arr=list(map(int,input().split()))
	arr.sort()
	#print(arr)
	count=0
	if arr[p-1]==x:
		print(0)
		continue
	elif k>=p and arr[p-1]>=x:
		count=0
		for i in range(p-1,-1,-1):
			if arr[i]>x:
				count+=1
		#continue
			print(arr)
	elif p>=k and arr[p-1]<=x:
		for i in range(p-1,n):
			if arr[i]<x:
				count+=1
			print(arr)
		#continue
	else:
		count=-1
		#continue
	print(count)
