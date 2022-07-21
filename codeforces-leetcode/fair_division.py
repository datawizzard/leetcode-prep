# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
# import sys
# import math
# import bisect
# from sys import stdin, stdout
# from math import gcd, floor, sqrt, log, ceil
# from collections import defaultdict as dd
# from collections import Counter as cc
# from bisect import bisect_left as bl
# from bisect import bisect_right as br
# import functools
# INF = float('inf')
# MOD = 998244353
# mod = 10**9+7
# sys.setrecursionlimit(100000000)
# def inp(): return sys.stdin.readline().rstrip("\n")
# def out(var):     sys.stdout.write(s(var) + "\n")  
# def I():    return (inp())
# def II():    return (int(inp()))
# def FI():    return (float(inp()))
# def SI():    return (list(s(inp())))
# def MI():    return (map(int,inp().split()))
# def LI():    return (list(MI()))
# def SLI():    return (sorted(LI()))
# def MF():    return (map(float,inp().split()))
# def LF():    return (list(MF()))
# def SLF():    return (sorted(LF()))

# # DP Approach
# # Equal Sum Partition Problem
# # we have to partition the arr in two subset such that
# # both the subset have equal sum 
# # So apply equal sum partition problem using DP
def equalsum(arr):
	n=len(arr)
	if sum(arr)%2!=0:
		return False
	else:
		sum1=sum(arr)//2
		a=[[False for j in range(sum1+1)] for i in range(n+1)]	
		for i in range(n+1):
			for j in range(sum1 + 1):
				if i==0 and j==0:
					a[i][j]=True
				elif j==0:
					a[i][j]=True
				elif i==0:
					a[i][j]=False
		for i in range(1,n+1):
			for j in range(1,sum1 + 1):
				if arr[i-1]>j:
					a[i][j]=a[i-1][j]
				else:
					a[i][j]=a[i-1][j] or a[i-1][j-arr[i-1]]
		return a[n][sum1]
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	if equalsum(arr)==True:
		print("YES")
	else:
		print("NO")


# Greedy Approach
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	if sum(arr)%2==1:
		print("NO")
	else:
		c1,c2=0,0
		for i in range(n):
			if arr[i]==1:
				c1+=1
			else:
				c2 += 1
		if c2%2==1 and c1==0:
			print("NO")
		else:
			print("YES")
