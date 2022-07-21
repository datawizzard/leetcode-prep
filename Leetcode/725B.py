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
	count = 0
	avg = sum(a) / n
	if math.ceil(avg) != math.floor(avg):
		print(-1)
	else:
		for i in range(n):
			if a[i] > avg:
				count += 1
		print(count)
	