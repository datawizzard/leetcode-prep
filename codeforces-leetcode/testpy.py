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
for _ in range(II()):
	n,q = MI()
	a = LI()
	b = []
	for i in range(n):
		ans = 0
		for j in range(i,n):
			ans = ans + a[j]
			b.append(ans)
	b.sort(reverse = True)
	for i in range(q):
		l,r = map(int,input().split())
		s = 0
		for i in range(l-1,r):
			s += b[i]
		print(s)

