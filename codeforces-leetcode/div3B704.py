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
	n = II()
	a = LI()
	arr = []
	c0,c1,c2,ans = 0,0,0,0
	for i in range(n):
		if a[i] % 3 == 0:
			c0 += 1
		elif a[i] % 3 == 1:
			c1 += 1
		else:
			c2 += 1
	arr.append(c0)
	arr.append(c1)
	arr.append(c2)
	while True:
		for i in range(3):
			if arr[i] > n // 3:
				diff = arr[i] - n // 3
				arr[(i+1) % 3] += diff
				ans += diff
				arr[i] -= diff
		if all((i==n // 3) for i in arr):
			break;
	print(ans)



	
