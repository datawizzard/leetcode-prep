import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def maxcoin(arr,s):
	n=len(arr)
	dp=[[0 for j in range(s+1)] for i in range(n+1)]
	for i in range(n+1):
		for j in range(s+1):
			if i==0 and j==0:
				dp[i][j]=0
			elif i==0:
				dp[i][j]=0
			elif j==0:
				dp[i][j]=1
	for i in range(1,n+1):
		for j in range(1,s+1):
			if arr[i-1]<=j:
				dp[i][j]=dp[i-1][j]+dp[i][j-arr[i-1]]
			else:
				dp[i][j]=dp[i-1][j]
	return dp[i][j]
for _ in range(int(input())):
	s=int(input())
	arr=list(map(int,input().split()))
	print(maxcoin(arr,s))