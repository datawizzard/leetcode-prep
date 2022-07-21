import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	arr1=[0]*(n)
	m=max(arr)
	for j in range(n):
		arr1[j]=m-arr[j]
	l=max(arr1)
	for i in range(n):
		arr[i]=l-arr1[i]
	if k%2==0:
		print(*arr)
	else:
		print(*arr1)
