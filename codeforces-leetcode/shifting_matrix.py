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
n,m = MI()
k = int(input())
p = int(input())
cmd = I()
arr = [[int(j)  for j in input().split()] for  i in range(n)]
k = k % n
if cmd == 'C':
	for i in range(n):
		for j in range(m):
			if j == p-1:
				temp = arr[i][j]
				arr[i][j] = arr[i-k-1][j]
				arr[i-k-1][j] = temp
print(arr)


