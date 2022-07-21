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
	count=[0]*(n)
	prime = [True for i in range(n+1)]
	prime[0] = False
	prime[1] = False
	p = 2
	while (p * p <= n):
	    if (prime[p] == True):
	        for i in range(p * p, n+1, p):
	            prime[i] = False
	    p += 1
	for i in range (n):
	    if(prime[i] == True):
	        if(prime[n-i] == True):
	            count[i] = count[i-1] + 1
	return count
count = seive(20)
print(count)
for _ in range(II()):
	n = II()
	print(count[n])
