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
	a = LI()
	ans = 1
	count = [0]*m
	for i in a:
		count[i % m] += 1
	# print(count)
	if count[0] > 0:
		ans = 1
	else:
		ans = 0
	for i in range(1,m//2+1):
		x = count[i]
		y = count[m-i]
		if abs(x - y) <=1 and x!=0 and y != 0:
			ans += 1
		else:
			ans += abs(x-y)
	print(ans)

