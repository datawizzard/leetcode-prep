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
	c1,c2=0,0
	for i in range(n):
		if a[i] == 1:
			c1 += 1
		elif a[i] == 2:
			if c2 > c1: 
				c1 -= 1
			else:
				c2 -= 1
		elif a[i] == 3:
			if c1 >= c2:
				c1 += 1
			else:
				c2 -= 1
	print(c1)

