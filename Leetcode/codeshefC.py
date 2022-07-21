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
a = []
def seive(n):
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
	    if (prime[p] == True):
	        for i in range(p * p, n+1, p):
	            prime[i] = False
	    p += 1
	for p in range(2, n+1):
	    if prime[p]:
	        a.append(p)
	return a
res = seive(10**7+1)
# print(res)
for _ in range(II()):
	N = II()
	ans = 0
	for i in range(len(res)):
		if res[i] <= N:
			ans += 1
		else:
			break;
	# print(ans,"gg")
	for i in range(N+1):
		if res[i] * 2 <= N and res[i] % 2 == 1:
			ans -= 1
	print(ans)
	
