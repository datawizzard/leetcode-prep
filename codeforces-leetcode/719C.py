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
from collections import Counter
for _ in range(II()):
	n = II()
	a = LI()
	b = []
	for i in range(n):
		b.append(a[i] - i)
	# print(b)
	count = 0
	x = Counter(b)
	# print(x)
	for i in x:
		if x[i] > 1:
			count += x[i]*(x[i] - 1)//2
	print(count)