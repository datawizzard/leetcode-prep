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
from collections import Counter
for _ in range(II()):
	s = I()
	n = len(s)
	c = Counter(s)
	# print(c)
	x,y = 0,0
	for i in c.values():
		if i == 1:
			x += 1
		if i % 2 == 0:
			y += (i//2)
		if i > 3 and i & 1:
			y += (i - 3)//2
	if y >= x:
		print("YES")
	else:
		print("NO")

	