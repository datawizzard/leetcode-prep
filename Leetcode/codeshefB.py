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
for _ in range(II()):
	n,k = MI()
	s = list(map(int,I()))
	queries = LI()
	ans = 0
	if n > 1:
		for i in range(n-1):
			if s[i] == s[i+1]:
				ans += 2
			else:
				ans += 1
		# print(ans)
		for i in range(k):
			x = queries[i]
			if x - 1 != 0 and x -1 != n - 1:
				# print("vv")
				if s[x-1] == 1 and (s[x-2] == s[x] == 0):
					ans += 2
				if s[x-1] == 1 and (s[x-2] == s[x] == 1):
					ans -= 2
				if s[x-1] == 0 and (s[x-2] == s[x] == 1):
					ans += 2
				if s[x-1] == 0 and (s[x-2] == s[x] == 0):
					ans -= 2
			else:
				if s[x-1] == 1 and x - 1 == 0 and s[x] == 0:
					ans += 1
				if s[x-1] == 0 and x - 1 == 0 and s[x] == 0:
					ans -= 1
				if s[x-1] == 1 and x - 1 == 0 and s[x] == 1:
					ans -= 1
				if s[x-1] == 0 and x - 1 == 0 and s[x] == 1:
					ans += 1
				if s[x-1] == 1 and x - 1 == n - 1 and s[x - 2] == 0:
					ans += 1
				if s[x-1] == 0 and x - 1 == n - 1 and s[x - 2] == 0:
					ans -= 1
				if s[x-1] == 1 and x - 1 == n - 1 and s[x - 2] == 1:
					ans -= 1
				if s[x-1] == 0 and x - 1 == n - 1 and s[x - 2] == 1:
					ans += 1
			s[x-1] = s[x-1] ^ 1
			# print(s)
			print(ans)
	else:
		for i in range(k):
			print(0)


	