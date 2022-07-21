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
	n = II()
	a = LI()
	c = Counter(a)
	# print(c)
	for i in c:
		if c[i] == 1:
			res = i
	# print(res)
	for i in range(n):
		if a[i] == res:
			print(i + 1)
		