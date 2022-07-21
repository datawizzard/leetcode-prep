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
	n,m = MI()
	arr = LI()
	idx = 0
	for i in range(n):
		if arr[i] != i+1:
			idx = i + 1
	rev = 1.000000
	ans = 0.000000
	for i in range(m):
		a = input().strip().split()
		r = int(a[0])
		p = a[1]
		# print(r,p)
		if r >= idx:
			# print(rev,p)
			ans = ans + float(rev) * float(p)
			rev = rev * (float(1.000000) - float(p))
	if idx == 0:
		ans = 1.000000
	print(ans)