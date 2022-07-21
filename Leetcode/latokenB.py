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
	b  = [0]
	if n == 1:
		print(a[0])
	else:
		for i in a:
			b.append(i)
		b.append(0)
		# print(b)
		ans = 0
		minugly = 0
		for i in range(1,n+1):
			if b[i-1] < b[i] > b[i+1]:
				l = abs(b[i] - b[i-1])
				m = abs(b[i+1] - b[i])
				mini = min(l,m)
				ans += mini
				if l == mini:
					b[i] = b[i-1]
				else:
					b[i] = b[i+1]
		# print(b,ans)
		for i in range(1,n+2):
			minugly += abs(b[i] - b[i-1])
		print(minugly+ans)



