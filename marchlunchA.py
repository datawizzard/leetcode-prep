import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))

# DP solution but it will give TLE alas i tried this one and fucked up (-_-)
# for _ in range(II()):
# 	A,Y,X = MI()
# 	dp = [0]*(Y+1)
# 	dp[0] = 1
# 	for i in range(1,Y + 1):
# 		if i == Y:
# 			dp[i] = dp[i-1] + X - dp[i - Y]
# 		else:
# 			dp[i] = dp[i-1] + X
# 	print(dp[Y])
for _ in range(II()):
	A,Y,X = MI()
	if A >= Y:
		print(X * Y)
	else:
		print(X * A + 1)