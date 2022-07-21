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
n, q, k = MI()
a = LI()
for _ in range(q):
	l, r = MI()
	l -= 1
	r -= 1
	print(k + a[r] - a[l] - 2*(r - l) - 1)