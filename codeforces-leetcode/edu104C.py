# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
for _ in range(II()):
	n = II()
	a = LI()
	c = 0
	for i in range(n-1):
		m = max(a[i],a[i+1])
		n = min(a[i],a[i+1])
		if m/n > 2:
			# print(m,n)
			while m > 2*n:
				m = (m+1)//2
				c += 1
	print(c)
