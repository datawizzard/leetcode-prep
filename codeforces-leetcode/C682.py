import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
t = int(input())
for p in range(t):
	n, m = map(int, input().split())
	a = [list(map(int, input().split())) for i in range(n)]
	#print(a)
	for i in range(n):
		for j in range(m):
		    if (a[i][j] -i - j) % 2== 0:
		        a[i][j] += 1
		print(*a[i])
