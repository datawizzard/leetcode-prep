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
	s = str(n)
	x = len(s)
	t = 0
	ans = 0
	for i in range(x):
		t = t * 10 + 1
		for j in range(1,10):
			if t * j <= n:
				ans += 1
	print(ans)