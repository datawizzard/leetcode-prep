# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
# def lcs(a,b,n,m):
# 	ans = 0 
# 	dp=[[0 for j in range(m+1)] for i in range(n+1)]
# 	for i in range(1,n+1):
# 		for j in range(1,m+1):
# 			if a[i-1] == b[j-1]:
# 				dp[i][j] = dp[i-1][j-1] + 1
# 			else:
# 				dp[i][j] = 0
# 			ans = max(ans,dp[i][j])
# 	return ans
for i in range(II()):
	a = I()
	b = I()
	n = len(a)
	m = len(b)
	ans = 0
	# print(n + m - 2 * lcs(a,b,n,m))
	for i in range(len(a)+1):
		for j in range(i,len(a)+1):
			if a[i:j+1] in b:
				ans = max(ans,len(a[i:j+1]))
	# for i in range(len(b)+1):
	# 	for j in range(i,len(b)+1):
	# 		if b[i:j+1] in a:
	# 			ans = max(ans,len(b[i:j+1]))
	print(n + m - 2 * ans)



