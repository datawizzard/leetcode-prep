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
	mini = min(a)
	maxi = max(a)
	p = a.index(mini)
	q = a.index(maxi)
	p += 1
	q += 1
	# print(p,q)
	l = max(p,q)
	m = max(n-p+1,n-q+1)
	r = p + n - q + 1
	s = q + n -p + 1
	print(min(l,m,r,s))
