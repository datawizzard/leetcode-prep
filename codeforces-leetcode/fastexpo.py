import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
def power(base, exp):
    if exp < 0:
        return 1 / power(base, -exp)
    ans = 1
    while exp:
        if exp & 1:
            ans = (ans * base) % (10**9 + 7)
        exp >>= 1
        base = (base * bas) % (10**9 + 7)
    return ans % (10**9 + 7)
for _ in range(II()):
	n = II()
	base = 2
	exp = n - 1
	print(power(base,exp))