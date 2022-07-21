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
import bisect
for _ in range(II()):
	n,l,r = MI()
	a = LI()
	a.sort()
	ans = 0
	for i in range(n):
		x = bisect.bisect_left(a,l - a[i],i+1,n)
		y = bisect.bisect_right(a,r - a[i],i+1,n)
		# print(x,y)
		ans += y - x
	print(ans)