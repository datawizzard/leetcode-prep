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
	k = II()
	a = []
	s = 0
	for i in range(1,2*k + 2):
		a.append(k+i*i)
	# print(a)
	for i in range(len(a) - 1):
		s += math.gcd(a[i],a[i+1])
	print(s)