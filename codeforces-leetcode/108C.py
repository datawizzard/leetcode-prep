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
	a = [int(x) - 1 for x in input().split()]
	b = LI()
	# print(a)
	# print(b)
	member = [[] for _ in range(n)]
	for i in range(n):
		member[a[i]].append(b[i])
	# print(member)
	for i in range(n):
		member[i].sort(reverse =True)
	for j,ii in enumerate(member):
		# print(ii)
		for i in range(1,len(member[j])):
			member[j][i] += member[j][i-1]
	# print(member)
	# for i in range(1,n+1):
	# 	sum1 = 0
	# 	for s in member:
	# 		# print(s,len(s))
	# 		l = len(s)
	# 		if l > 0:
	# 		# print(l)
	# 			x = l % i
	# 			if l >= i:
	# 				if x != 0:
	# 					sum1 += s[-x-1]
	# 				else:
	# 					sum1 += s[-1]
	# 		# print(sum1)
	# 	print(sum1,end=" ")
	# print()
	out = []
	teams = list(range(n))
	for k in range(1, n + 1):
		teams = [t for t in teams if len(member[t]) >= k]
		# print(teams)
		score = 0.0
		for t in teams:
		    score += member[t][k * (len(member[t]) // k) - 1]
		out.append(int(score))
	print (' '.join(str(x) for x in out))
		