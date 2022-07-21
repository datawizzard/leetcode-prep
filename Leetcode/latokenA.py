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
	n,m = MI()
	matrix = []
	for i in range(n):
	    a = list(input())
	    matrix.append(a)
	flag,flag1 = 0,0
	new_mat = [['' for j in range(m)] for i in range(n)]
	new_matA = [['' for j in range(m)] for i in range(n)]
	for i in range(n):
		for j in range(m):
			if (i + j) % 2 == 0:
				new_mat[i][j] = 'W'
			else:
				new_mat[i][j] = 'R'
	# print(new_mat)
	for i in range(n):
		for j in range(m):
			if (i + j) % 2 == 0:
				new_matA[i][j] = 'R'
			else:
				new_matA[i][j] = 'W'
	# print(new_mat)
	for i in range(n):
		for j in range(m):
			if matrix[i][j] != new_mat[i][j] and matrix[i][j] != '.':
				flag = 1
	for i in range(n):
		for j in range(m):
			if matrix[i][j] != new_matA[i][j] and matrix[i][j] != '.':
				flag1 = 1
	if flag == 1 and flag1 == 1:
		print("NO")
	elif flag == 0:
		print("YES")
		for i in range(n):
			for j in range(m):
				print(new_mat[i][j],end="")
			print()

	elif flag1 == 0:
		print("YES")
		for i in range(n):
			for j in range(m):
				print(new_matA[i][j],end="")
			print()

