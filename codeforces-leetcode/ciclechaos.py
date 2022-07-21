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
import math
for _ in range(II()):
    (n,x)=tuple(MI())
    l=LI()
    g=l[0]
    m=1
    for i in range(1,x):
        g=math.gcd(g,l[i])
    for i in range(1,int(math.sqrt(g))+2):
        if (g % i == 0):
            if(i<=n):
                m=max(m,i)
            if(int(g/i)<=n):
                m=max(m,int(g/i))
    print(n-m)