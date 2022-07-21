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
	s = I()
	i = 0
	flag = 0
	while i < n-1:
		while i < n - 1 and s[i] == s[i+1] :
			i += 1
		# print(i)
		for j in range(i+1,n):
			if s[i] == s[j]:
				flag = 1
		i += 1
	if flag == 1:
		print("NO")
	else:
		print("YES")

