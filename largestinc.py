import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def lis(arr): 
    n = len(arr) 
    dp = [1]*n 
    for i in range (1, n): 
        for j in range(0, i): 
            if arr[i] > arr[j] and dp[i]<dp[j] + 1: 
                dp[i] = dp[j]+1
    maximum = 0 
    for i in range(n): 
        maximum = max(maximum, dp[i]) 
    return maximum
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	x=lis(arr)
	print(x)
