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
from collections import Counter
for _ in range(II()):
	s = I()
	s = list(s)
	c = Counter(s)
	oddcount = 0
	ans = 0
	for i in c:
		if c[i] % 2 == 1:
			oddcount += 1
	if oddcount <= 1:
		p1,p2 = 0,len(s) - 1
		while p1 < p2:
			if s[p1] != s[p2]:
				k = p2
				while k > p1 and s[k] != s[p1]:
					k -= 1
				if k == p1:
					s[p1],s[p1 + 1] = s[p1 + 1],s[p1]
					ans += 1
				else:
					while k < p2:
						s[k], s[k + 1] = s[k + 1], s[k]
						k += 1
						ans += 1
			else:
				p1 += 1
				p2 -= 1
	else:
		ans = -1
	print(ans)

