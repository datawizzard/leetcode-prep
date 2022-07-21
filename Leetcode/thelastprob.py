import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
mat = [[0 for  j in range(11)]for i in range(11)]
for i in range(1,11):
	mat[i-1][0] = i * (i + 1) // 2 
	for j in range(1,11):
		mat[i-1][j] = mat[i-1][j-1] + i + (j - 1)
print(mat)
for _ in range(II()):
	x1,y1,x2,y2 = MI()
	sum1 = 0
	for i in range(y1-1,y2):
		sum1 += mat[i][x1 - 1]
		# print(sum1)
	for j in range(x1, x2):
		sum1 += mat[y2-1][j]
	print(sum1)

