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
	b = []
	c = []
	ans = 0
	for i in range(n):
		if a[i] % 2 == 0:
			b.append(a[i])
		else:
			c.append(a[i])
	b.extend(c)
	# print(b)
	for i in range(n-1):
		# print(b[i])
		for j in range(i+1,n):
			if math.gcd(2*b[j],b[i]) > 1:
				# print(a[j],a[i])
				ans += 1
	print(ans)
