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
# def factors(x):
#     result = []
#     i = 1
#     while i*i <= x:
#         if x % i == 0:
#             result.append(i)
#             if x//i != i:
#                 result.append(x//i)
#         i += 1
#     return result
# a,b=map(int,inp().split())
# arr1=factors(a)
# arr2=factors(b)
# print(len(list(set(arr1)&set(arr2))))
n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
t=s+1
print(math.ceil(t/4))