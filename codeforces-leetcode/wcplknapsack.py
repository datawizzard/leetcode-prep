import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def knapsac(n,k,arr):
	for i in range(n+1):
		for j in range(k+1):
			# if there are 0 item present or it knapsack capacity is 0
			if i==0 or j==0:
				a[i][j]=0
			# if last item weight is less than knapsack capacity.
			# we have two option either store it in knapsack or ignore it 
			# and move to next item.
			elif arr[i-1]<=j:
				a[i][j]=max(arr[i-1]+a[i-1][j-arr[i-1]],a[i-1][j])
			else:
				a[i][j]=a[i-1][j]
	for i in range(n+1):
		for j in range(k+1):
			print(a[i][k],end=" ")
		print()
	suffix=[0]*(n+1)
	flag=0
	for i in range(1,n):
		suffix[i]=suffix[i-1]+arr[i]
		if suffix[i]-a[i][k]>=k:
			flag=1
			return n-i
	if flag==0:
		return -1
for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	arr.sort()
	a=[[0 for j in range(k+1)]for i in range(n+1)]
	print(knapsac(n,k,arr))
