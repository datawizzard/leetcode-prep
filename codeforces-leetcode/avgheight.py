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
for i in range(II()):
	n = II()
	a = LI()
	b = []
	c = []
	for i in range(n):
		if a[i] % 2 == 0:
			b.append(a[i])
		else:
			c.append(a[i])
	# print()
	b.extend(c)
	print(*b)