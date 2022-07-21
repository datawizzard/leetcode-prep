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
n,q = MI()
a = LI()
x = a.count(1)
y = a.count(0)
for i in range(q):
	t,k = MI()
	if t == 1:
		a[k-1] = 1 - a[k-1]
		if a[k-1] == 1:
			x += 1
			y -= 1
		else:
			y += 1
			x -= 1
		# print(x,y)
	else:
		if k  > x:
			print(0)
		else:
			print(1)

