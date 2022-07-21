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
	a,b,k = MI()
	aa = LI()
	bb = LI()
	d=[0]*(a)
	f=[0]*(b)
	for i in aa:
		d[i-1] += 1
	for j in bb:
		f[j-1] += 1
	print(d)
	print(f)
	ans = 0
	for i in range(a):
		ans += (d[i] * (d[i] - 1))//2
	for i in range(b):
		ans += (f[i] * (f[i] - 1))//2
	print(((k*(k-1))//2)-ans)