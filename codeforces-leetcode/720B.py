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
	print(n-1)
	idx = a.index(min(a))	
	for i in range(n):
		if i != idx:
			print(idx + 1 , i + 1,a[idx],a[idx] + abs(idx - i))
