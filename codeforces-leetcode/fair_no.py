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
def check(x):
	y=x
	while y:
		a=y%10
		if a!=0 and x%a!=0:
			return False
		y//=10
	return True
for _ in range(int(input())):
	n=int(input())
	while not check(n):
		n+=1
	print(n)
	# flag=0
	# while flag==0:
	# 	for i in str(n):
	# 		if int(i)!=0 and p%int(i)!=0:
	# 			p+=1
	# 			n=str(p)
	# 			print(p,n)
	# 			break;
	# 	else:
	# 		# print("hh")
	# 		flag=1
	# print(p)
	


	




