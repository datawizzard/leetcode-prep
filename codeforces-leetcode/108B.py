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
for _ in range(II()):
	n,m,k = MI()
	# dp =[[0 for j in range(m)] for i in range(n)]
	# for i in range(n):
	# 	dp[i][0] = i
	# for j in range(m):
	# 	dp[0][j] = j
	# print(dp)
	# for i in range(1,n):
	#     for j in range(1,m):
	#         dp[i][j] = (i - 1) + (j - 1)
	# print(dp)
	# print(dp[n-1][m-1])
	if (n * m) - 1 == k:
		print("YES")
	else:
		print("NO")