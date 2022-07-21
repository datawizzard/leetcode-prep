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
	n,m,x = MI()
	a = LI()
	b = [(0,i) for i in range(1,m+1)]
	print("YES")
	for i in range(n):
		x = heapq.heappop(b)
		print(x[1],end=" ")
		heapq.heappush(b,(x[0] + a[i],x[1]))
		# print(b)
	print()

