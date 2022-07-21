import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
n = int(input())
mat = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[float('-inf') for j in range(len(mat[0]))]for i in range(n)]
dp[0][0] = mat[0][0]
for i in range(1,n):
	dp[i][0] = dp[i-1][0] + mat[i][0]
for j in range(1,len(mat[0])):
	dp[0][j] = dp[0][j-1] + mat[0][j]
for i in range(1,n):
	for j in range(1,len(mat[0])):
		dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + mat[i][j]
print(dp)
print(dp[-1][-1])





