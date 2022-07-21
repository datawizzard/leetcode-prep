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
	ans = float('INF')
	n,u,v = MI()
	a = LI()
	for i in range(1,n):
		if abs(a[i] - a[i-1]) == 1:
			ans = min(ans,min(u,v))
		elif abs(a[i] - a[i-1]) == 0 :
			ans = min(ans,min((u + v),2*v))
		else:
			ans = 0
	print(ans)