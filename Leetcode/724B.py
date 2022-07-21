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
from collections import OrderedDict,Counter
d = 'abcdefghijklmnopqrstuvwxyz'
b = []
for i in d:
	b.append(i)
	for j in d:
		b.append(i+j)
		for k in d:
			b.append(i + j + k)
b.sort(key = len)
for _ in range(II()):
	n = II()
	s = I()
	for i in b:
		if i not in s:
			print(i)
			break;
