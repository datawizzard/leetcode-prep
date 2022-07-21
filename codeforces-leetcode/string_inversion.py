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
# Brute Force
# for _ in range(int(input())):
# 	n,k=map(int,input().split())
# 	arr=input()
# 	for i in range(k):
# 		l=0
# 		s=set()
# 		s.add(0)
# 		c,d=map(int,input().split())
# 		for i in range(n):
# 			if i<c-1 or i>d-1:
# 				if arr[i]=='-':
# 					l-=1
# 					s.add(l)
# 				else:
# 					l+=1
# 					s.add(l)
# 		# print(s)
# 		print(len(s))

# Optimal Using Prefix Sum

for _ in range(II()):
	n,k=MI()
	s=I()
	maxi, mini, c = 0, 0, 0
	a=[(0,0,0)]
	for i in s:
		if i=='-':
			c -= 1
		else:
			c += 1
		if c>maxi:
			maxi = c
		if c < mini:
			mini = c
		a.append((maxi,mini,c))
	b=[(0,0,0)]
	maxi, mini, c = 0, 0, 0
	for i in s[::-1]:
		if i=='-':
			c += 1
		else:
			c -= 1
		if c > maxi:
			maxi = c
		if c < mini:
			mini = c
		b.append((maxi,mini,c))

	for i in range(k):
		l,r = MI()
		d = a[l-1]
		e = b[n-r]
		print(max(d[0] ,e[0] + d[2] - e[2]) - min(d[1] ,e[1] + d[2] - e[2]) + 1)