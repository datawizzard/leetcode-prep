# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         n = len(s)
#         m = len(p)
#         def regular(s,p,n,m):
#             dp=[[False for j in range(m+1)] for i in range(n+1)]
#             dp[0][0] = True
#             for i in range(1,n+1):
#                 dp[i][0] =False
#             for j in range(1,m+1):
#                 if p[j-1] == "*":
#                     dp[0][j] = dp[0][j-2]
#             for i in range(1,n+1):
#                 for j in range(1,m+1):
#                     if s[i-1] == p[j-1] or p[j-1]==".":
#                         dp[i][j] = dp[i-1][j-1]
#                     elif p[j-1] =="*":
#                         if p[j-2] == s[i-1] or p[j-2] ==".":
#                             dp[i][j] = dp[i][j-2] or dp[i-1][j]
#                         else:
#                             dp[i][j] = dp[i][j - 2]
#             return dp[n][m]
#         return regular(s,p,n,m)


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
for _ in range(II()):
	s = I()
	p = I()
	d = {}
	def dfs(i,j):
		if (i,j) in d:
			return d[(i,j)]
		if i >= len(s) and j >= len(p):
			return True
		if j >= len(p):
			return False
		match = i < len(s) and (s[i] == p[j] or p[j] == '.')
		if j + 1 < len(p) and p[j + 1] == '*':
			# If  we found a star we have two choices either to include it or not 
			# include it in the solution.
			d[(i,j)] = (dfs(i,j+2) or # If we dont use star j + 2 because we have to skip * 
			 (match and dfs(i+1,j))) # use star when then is a math a character
			return d[(i,j)]
		if match:
			d[(i,j)] = dfs(i+1,j+1)
			return d[(i,j)]
		return False
	print(dfs(0,0))


                            
                        