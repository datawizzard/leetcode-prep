# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
for _ in range(II()):
	n = II()
	a = LI()
	ans = 0
	idx = [-1]*(2*n+1)
	for i in range(n):
		idx[a[i]] = i + 1
	for s in range(3,2*n):
		i = 1
		while i * i <= s:
			if s % i == 0 and i * i != s and idx[i] != -1 and idx[s//i] != -1 and idx[i] + idx[s//i] == s:
				ans += 1
			i += 1
	print(ans)





	