# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
# n,k = MI()
# arr = LI()
# b=[0]*(n)
# for i in range(n-1):
# 	b[i]=arr[i+1] - arr[i]
# b=b[:n-1]
# b.sort()
# print(b)
# ans=0
# for i in range(n-k):
# 	ans+= b[i]
# print(ans)
for _ in range(II()):
	a,b,c = MI()
	print(a+b)