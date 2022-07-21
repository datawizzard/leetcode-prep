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
	n,m,k = MI()
	mat,res = [],0
	for i in range(n):
	    a = LI()
	    mat.append(a)
	# print(mat)
	for i in range(n):
		for j in range(1,m):
			mat[i][j] += mat[i][j-1]
			# mat[i][j] += mat[i-1][j]
	# print(mat)
	for j in range(m):
		for i in range(1,n):
			mat[i][j] += mat[i-1][j]
	#print(mat)
	b = [0]*(m)
	mat.insert(0,b)
	for i in mat:
		i.insert(0,0)
	# print(mat)
	for i in range(n+1):
		for j in range(m + 1):
			print(mat[i][j],end =" ")
		print()
	# for p in range(1,n+1):
	# 	for i in range(1,n - p + 2):
	# 		low,high,mid,flag = 1,m - p + 1,0,0
	# 		while low <= high:
	# 			mid = (high + low)//2
	# 			# print(mid)
	# 			s = mat[i + p - 1][mid + p - 1] - mat[i + p - 1][mid - 1] - mat[i - 1][mid + p - 1] + mat[i - 1][mid - 1]
	# 			# print(s)
	# 			if s >= k * p * p:
	# 				high = mid - 1
	# 				x = mid
	# 				flag = 1
	# 			else:
	# 				low = mid + 1
	# 		if flag:
	# 			res += m - p - x + 2
	# print(res)


