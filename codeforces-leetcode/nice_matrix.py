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
	n,m =  MI()
	a=[[int(j) for j in I().split()] for i in range(n)]
	ans=0
	for i in range(n):
		for j in range(m):
			c=a[i][m-j-1]
			d=a[n-i-1][j]
			l=[]
			l.append(a[i][j])
			l.append(c)
			l.append(d)
			l.sort()
			a[i][j] = a[i][m-j-1] = a[n-i-1][j] = l[1]
			ans += (l[1]-l[0])+(l[2]-l[1])
	print(ans)