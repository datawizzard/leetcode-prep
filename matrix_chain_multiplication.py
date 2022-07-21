import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

# # Recursive Solution
# def matrixchainmult(arr,i,j):
# 	if i>=j:
# 		return 0;
# 	ans=sys.maxsize
# 	for k in range(i,j):
# 		temp=matrixchainmult(arr,i,k)+matrixchainmult(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
# 		# print(temp)
# 		ans=min(ans,temp)
# 	return ans;
# for _ in range(int(input())):
# 	arr=list(map(int,input().split()))
# 	print(matrixchainmult(arr,1,len(arr)-1))

# Memoization

def matrixchainmult(arr,i,j):
	if i>=j:
		return 0;
	if dp[i][j]!=-1:
		return dp[i][j]
	ans=sys.maxsize
	for k in range(i,j):
		dp[i][j]=matrixchainmult(arr,i,k)+matrixchainmult(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
		# print(temp)
		ans=min(ans,dp[i][j])
	return ans;
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	dp=[[-1 for j in range(n+1)] for i in range(n+1)]
	print(matrixchainmult(arr,1,len(arr)-1))