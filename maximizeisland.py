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
	n,m=map(int,input().split())
	main =[list(input())for i in range(n)]
	a = [[0 for j in range(m)] for i in range(n)]
	b = [[0 for j in range(m)] for i in range(n)]
	for i in range(n):
		for j in range(m):
			if (i+j)%2==0:
				a[i][j] = "*"
				b[i][j] = "."
			else:
				a[i][j] = "."
				b[i][j] = "*"
	count,count1,count2,count3 = 0,0,0,0
	for i in range(n):
		for j in range(m):
			if a[i][j] != main[i][j]:
				count+=1
			if b[i][j] != main[i][j]:
				count1+=1
			if a[i][j] == "*":
				count2+=1
			if b[i][j] == "*":
				count3 += 1
	if count2>count3:
		print(count)
	elif count2==count3:
		print(min(count1,count))
	else:
		print(count1)		