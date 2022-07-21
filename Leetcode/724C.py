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
	s = I()
	d = {}
	countD,countK = 0,0
	for i in range(n):
		if s[i] == 'D':
			countD += 1
		if s[i] == 'K':
			countK += 1
		p,q = countD,countK
		g = math.gcd(countD,countK)
		p,q = p / g,q / g
		if (p,q) not in d:
			d[(p,q)] = 1
		else:
			d[(p,q)] += 1
		# print(d)
		print(d[(p,q)],end = " ")
	print()