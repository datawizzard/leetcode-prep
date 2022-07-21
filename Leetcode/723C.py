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
n = II()
a = LI()
curr = 0
b = []
for i in range(n):
	curr += a[i]
	heapq.heappush(b,a[i])
	if curr < 0:
		x = heapq.heappop(b)
		curr -= x
# print(b)
print(len(b))

