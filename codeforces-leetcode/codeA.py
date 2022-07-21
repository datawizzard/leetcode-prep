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
# from collections import Counter
# for _ in range(int(input())):
# 	s=input()
# 	d={}
# 	for i in s:
# 		if i not in d:
# 			d[i]=1
# 		else:
# 			d[i]+=1
# 	c,ans=0,0
# 	for i in d:
# 		if d[i]>=2:
# 			p=d[i]//2
# 			d[i]%=2
# 			c+=p
# 	for i in d:
# 		if d[i]>0 and c>0:
# 			ans+=1
# 			c-=1
# 	c*=2
# 	ans+=(c//3)
# 	print(ans)
for _ in range(int(input())):
	n=int(input())
	s=input()
	t=input()
	a=[]
	if s==t:
		print("Yes")
		continue;
	c=list(s)
	d=list(t)
	# print(c)
	# print(d)
	r=c.count("1")
	z=d.count("1")
	# print(r,z)
	if r!=z:
		print("No")
	else:
		pos,res,flag=0,9999999,0
		for i,j in zip(c,d):
			a.append((int(i)-int(j)))
		# print(a)
		for i in range(n):
			# print(i)
			if a[i]==1:
				pos=i
			if a[i]==-1:
				res=i
			if res<pos:
				print("No")
				break;
		if pos<res:
			print("Yes")
# for _ in range(int(input())):
# 	n,m=map(int,input().split())
# 	row=[]
# 	for i in range(n):
# 		temp = list(map(int,input().split()))
# 		row.append(temp)
# 	q=int(input())
# 	for _ in range(q):
# 		x,y,z=map(int,input().split())
# 		row[x-1][y-1]=z
# 	print(row)
# 	for i in range(n):
# 		for j in range(m):
# 			if 







	
