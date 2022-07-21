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
# def chefant(arr,n):
# 	m=arr[0]
# 	a=arr[1:]
# 	a.sort()
# 	plus,minus,s =0,0,0
# 	if n==1:
# 		if a[0]>0 or a[-1]<0:
# 			return 0
# 		else:
# 			for i in range(m):
# 				if a[i]>0:
# 					minus=i
# 					plus=m-i
# 					print(plus,minus)
# 					break;
# 			while plus>0 and minus>0:
# 				s += (minus+plus) -1
# 				minus -=1
# 				plus -=1
# 			return s
# for _ in range(II()):
# 	n=II()
# 	arr=LI()
# 	print(chefant(arr,n))

def chef(arr,n):
	m=arr[0]
	a=arr[1:]
	a.sort()
	c,t=0,0
	if n==1:
		if a[0]>0:
			return 0
		elif a[-1]<0:
			return 0
		else:
			for i in range(m):
				if a[i]<0:
					c+=1
				else:
					t+=1
			return c*t
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	print(chef(arr,n))