import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
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
for _ in range(II()):
	x,y,l,r=MI()
	z=list(range(l,r+1))
	ans=[]
	for i in z:
		f=(x&i)*(y&i)
		ans.append(f)
	# print(ans)
	ind=ans.index(max(ans))
	print(z[ind])
