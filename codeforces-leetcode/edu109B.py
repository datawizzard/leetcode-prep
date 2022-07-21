import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
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
	b = a[:]
	# print(b,a)
	b.sort()
	if b == a:
		print(0)
	elif a.index(max(a)) == n -1 or a.index(min(a)) == 0:
		print(1)
	elif a.index(max(a)) == 0 and a.index(min(a)) == n-1:
		print(3)
	else:
		print(2)