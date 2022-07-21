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
from collections import Counter,OrderedDict
n = int(input())
m = int(input())
a = []
for i in range(n):
	a.append(int(input()))
print(a)
c = Counter(a)
c =dict(sorted(c.items(),key = lambda i: i[0]))
# print(c)
ans = 0
for x in c:
	if c[x] >= 3:
		ans += c[x] // 3
		c[x] = c[x] % 3
for i in c:
	while c[i] > 0:
		if i + 1 in c and i + 2 in c and c[i+1] > 0 and c[i+2] > 0:
			c[i] -= 1
			c[i+1] -= 1
			c[i+2] -= 1
			ans += 1
		else:
			break;
print(ans)

