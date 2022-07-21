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
n,l,r = MI()
a = LI()
b = LI()
c,d,z,m,p,q= a[l-1:r], b[l-1:r] ,a[:l-1],b[:l-1],a[r:],b[r:] 
if sorted(c) == sorted(d) and z == m and p == q:
	print("TRUTH")
else:
	print("LIE")