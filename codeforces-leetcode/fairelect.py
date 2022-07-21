import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# for _ in range(int(input())):
# 	n,m=map(int,input().split())
# 	a=list(map(int,input().split()))
# 	b=list(map(int,input().split()))
# 	a.sort()
# 	b.sort()
# 	if sum(a)>sum(b):
# 		print(0)
# 		continue;
# 	else:
# 		c,flag=0,0
# 		for i in range(n):
# 			if sum(a)<=sum(b):
# 				a[i],b[-(i+1)]=b[-(i+1)],a[i]
# 				c+=1
# 			if sum(a)>sum(b):
# 				print(c)
# 				flag=1
# 				break;
# 	if flag==0:
# 		print(-1)
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
def inp(): return sys.stdin.readline().rstrip("\n")
def out(var):     sys.stdout.write(s(var) + "\n")  
def I():    return (inp())
def II():    return (int(inp()))
def FI():    return (float(inp()))
def SI():    return (list(s(inp())))
def MI():    return (map(int,inp().split()))
def LI():    return (list(MI()))
def SLI():    return (sorted(LI()))
def MF():    return (map(float,inp().split()))
def LF():    return (list(MF()))
def SLF():    return (sorted(LF()))
def fairelection(a,b,n,m):
	a.sort()
	b.sort()
	if sum(a) > sum(b):
		return 0
	else:
		count, flag=0,0
		for i in range(n):
			if sum(a) <= sum(b):
				a[i], b[m-i-1] = b[m-i-1], a[i]
				count+=1
			if sum(a)>sum(b):
				flag = 1
				return count
	if flag==0:
		return -1
for _ in range(int(input())):
	n,m=MI()
	a=LI()
	b=LI()
	print(fairelection(a,b,n,m))