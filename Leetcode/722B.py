# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
for _ in range(II()):
	n = II()
	a = LI()
	a.sort()
	b = []
	flag ,found,min_pos_element= 0,0,0
	for i in range(n):
		if a[i] <= 0:
			b.append(a[i])
		if a[i] > 0:
			min_pos_element = a[i]
			flag = 1
			break;
	# print(b,min_pos_element)
	if flag == 0:
		print(len(b))
	else:
		for i in range(1,n):
			if abs(a[i] - a[i-1]) < min_pos_element and a[i] <= 0:
				found = 1
				break;
		if found == 0:
			print(len(b) + 1)
		else:
			print(len(b))
