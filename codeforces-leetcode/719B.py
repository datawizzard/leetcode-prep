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
	if n == 2:
		print(-1)
	else:
		a = []
		for i in range(1,n*n+1,2):
			a.append(i)
		for i in range(2,n*n+1,2):
			a.append(i)
		# print(a)
		for j in range(0,len(a),n):
			print(*a[j:j+n])
			# print()