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
def seive(n):
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
	    if (prime[p] == True):
	        for i in range(p * p, n+1, p):
	            prime[i] = False
	    p += 1
	return prime
ans = seive(1000000)
# print(ans,type(ans))
def res(R):
	for p in range(R,1000001):
		# print(p,"jh")
		if ans[p]:
			print(p)
			break;
for _ in range(II()):
	L,R = MI()
	res(R+1)
