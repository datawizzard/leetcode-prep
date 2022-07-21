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
def findPartition(arr, n,s):
	if s % 2 == 1:
		return False
	# print(s)
	for i in range(0, n + 1):
		part[0][i] = True
	for i in range(1, s // 2 + 1):
		part[i][0] = False
	for i in range(1, s // 2 + 1):
		for j in range(1, n + 1):
			part[i][j] = part[i][j - 1]
			if i >= arr[j - 1]:
				part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])
	return part[s // 2][n]

n = II()
a = LI()
s = 0
i, j = 0, 0
for i in range(n):
	s += a[i]
# print(s)
part = [[True for i in range(n + 1)]for j in range(s // 2 + 1)]
if findPartition(a,n,s) == False:
	print(0)
else:
	switch = 0
	while True:
		for i in range(n):
			if a[i] % 2 == 1:
				print(1)
				print(i+1)
				switch = 1 
				break;
			a[i] = a[i] // 2
		if switch == 1:
			break;

