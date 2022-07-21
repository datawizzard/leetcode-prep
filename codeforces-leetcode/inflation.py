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
for _ in range(II()):
	n,k = MI()
	a = LI()
	cent = k / 100
	s = a[0]
	ans = 0
	for i in range(1,n):
		if a[i] / s > cent:
			new = a[i] * 100
			x = math.ceil((new - s * k)/k)
			ans += x
			# print(ans,x)
			s += x
		s += a[i]
	print(ans)
