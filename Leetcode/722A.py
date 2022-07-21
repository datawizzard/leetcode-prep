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
	count = 0
	a.sort()
	for i in range(n-1):
		for j in range(i+1,n):
			if a[j] > a[i]:
				# print(a[j],a[i])
				a[j] = 0
				count += 1
				break;
	print(count) 