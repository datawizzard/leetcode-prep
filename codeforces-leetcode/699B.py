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
	h = LI()
	rock  = 0
	while rock < k:
		flag = 0
		for i in range(1,n):
			if h[i] > h[i-1]:
				h[i-1] += 1
				ans = i
				flag = 1
				break;
		if flag == 0:
			ans = -1
			break;
		# print(h,rock)
		rock += 1
	print(ans)





