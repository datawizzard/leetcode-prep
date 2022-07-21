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
# n=int(input())
# a=str(n)
# s,r=0,0
# for i in a:
# 	if int(i)%2==0:
# 		s+=int(i)
# 	else:
# 		r+=int(i)
# print(max(s,r))
def FindMaxProduct(arr, n):   
    max = 0
    for i in range(n):  
        for j in range(n):   
            if j - 4 > 0: 
                ans = max(ans,(arr[i][j] * arr[i][j - 1] * arr[i][j - 2] * arr[i][j - 3]))   
            if i - 4 > 0 : 
                ans = max(ans,(arr[i][j] * arr[i - 1][j] * arr[i - 2][j] * arr[i - 3][j]))  
            if (i - 4) > 0 and (j - 4) > 0: 
                ans = max(ans,(arr[i][j] * arr[i - 1][j - 1] *arr[i - 2][j - 2] * arr[i - 3][j - 3]))  
            if (i - 4) >= 0 and (j - 1) <= 0: 
               	ans = (ans,(arr[i][j] * arr[i - 1][j + 1] * arr[i - 2][j + 2] * arr[i - 3][j + 3]))
    return ans

