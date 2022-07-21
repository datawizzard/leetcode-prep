import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
INF = float('inf')
from collections import Counter as cc
for _ in range(II()):
	n = II()
	s = LI()
	ans = INF
	c=sorted(cc(s).values())
	print(c)
	for i in range(len(c)):
		q = c[i]
		f = q * (len(c) - i)
		print(n - f)
		ans = min(ans,n - f)
	print(ans)