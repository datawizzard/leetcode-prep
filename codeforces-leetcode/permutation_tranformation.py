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
def dfs(l,r,d):
	if l > r:
		return;
	p,q = 0,0
	if len(a[l:r+1]) > 0:
		p = max(a[l:r+1])
		q = a.index(p)
		# print(p,q,l,r)
		x[q] = d
		dfs(l,q-1,d+1)
		dfs(q+1,r,d+1)
	return x;
for _ in range(II()):
	n = II()
	a = LI()
	l,r,d = 0,n-1,0
	x = [0]*n
	print(*dfs(l,r,d))
	





