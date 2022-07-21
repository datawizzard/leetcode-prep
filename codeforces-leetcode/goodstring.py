import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log, ceil
from collections import defaultdict as dd
from collections import Counter as cc
from bisect import bisect_left as bl
from bisect import bisect_right as br
import functools
INF = float('inf')
MOD = 998244353
mod = 10**9+7
sys.setrecursionlimit(100000000)
def inp(): return sys.stdin.readline()
def out(var):     sys.stdout.write(str(var) + "\n")  
def I():    return (inp())
def II():    return (int(inp()))
def FI():    return (float(inp()))
def SI():    return (list(str(inp())))
def MI():    return (map(int,inp().split()))
def LI():    return (list(MI()))
def SLI():    return (sorted(LI()))
def MF():    return (map(float,inp().split()))
def LF():    return (list(MF()))
def SLF():    return (sorted(LF()))
def minDeletions(s):
	c=cc(s).values()
	# print(c)
	l=list()
	total = 0
	for x in c:
		while x in l and x>0:
			x-=1
			total+=1
		l.append(x)
	# print(l)
	return total
	# Method 2
	# d={}
	# cost=0
	# c=cc(s)
	# # print(c)
	# for i in c.items():
	# 	# print(i[1])
	# 	if i[1] in d:
	# 		a=i[1]
	# 		# print(a,"ggg")
	# 		while a in d and a>0:
	# 			a-=1
	# 			cost+=1
	# 			# print(cost,"cc")
	# 		d[a]=1
	# 	else:
	# 		d[i[1]]=1
	# 	# print(d)
	# return cost
s=input()
print(minDeletions(s))