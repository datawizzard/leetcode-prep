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

def  DFSUtil(x):
	global count
	count+=1
	visited[x]=True
	for i in d[x]:
		# print(x,"ff")
		if visited[i]==False:
			DFSUtil(i)
	return count
for _ in range(II()):
	n,m=MI()
	d=dd(list)
	for i in range(m):
		x,y=MI()
		x-=1
		y-=1
		d[x].append(y)
		d[y].append(x)
	# print(d)
	visited=[False]*(n)
	res=0
	ways=1
	for k in range(0,n):
		if visited[k]==True:
			continue;
		res+=1
		count=0
		l=DFSUtil(k)
		# print(l,"gg")
		ways=(l%mod)*(ways%mod)
	print(res,ways%mod)