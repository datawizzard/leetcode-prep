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
	a = []
	for i in range(1,n+1):
		a.append(i)
	# print(a)
	if n % 2 == 0:
		for i in range(0,n,2):
			a[i],a[i+1] = a[i+1],a[i]
		print(*a)
	else:
		x = n - 1
		for i in range(0,x,2):
			a[i],a[i+1] = a[i+1],a[i]
		a[-1],a[-2] = a[-2],a[-1]
		print(*a)