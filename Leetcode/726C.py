# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
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
	n = II()
	a = LI()
	a.sort()
	ans = 9999999999
	for i in range(n-1):
		if a[i+1] - a[i] <= ans:
			ans = a[i+1] - a[i]
			x,y = i,i+1
	b = []
	b.append(a[x])
	for i in range(y+1,n):
		b.append(a[i])
	for i in range(0,x):
		b.append(a[i])
	b.append(a[y])
	print(*b)

