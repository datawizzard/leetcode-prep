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
	arr = LI()
	deff = [0]*31
	for i in range(n):
		for j in range(31):
			r = 1 << j
			if arr[i] & r:
				deff[j] += 1
	ans = 0
	for i in range(31):
		r = 1<<i
		if deff[i]:
			ans += r
	print(ans)
	for k in range(q):
		x,v = MI()
		for i in range(31):
			r = 1<<i
			if arr[x-1]&r:
				deff[i] -= 1
		for i in range(31):
			r = 1<<i
			if v & r:
				deff[i] += 1
		arr[x-1] = v
		ans = 0
		for i in range(31):
			r = 1<<i
			if deff[i] > 0:
				ans += r
		print(ans)
	


