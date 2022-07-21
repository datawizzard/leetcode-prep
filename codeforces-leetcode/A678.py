import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,m=map(int,input().split())
	arr=list(map(int,input().split()))
	if sum(arr)==m:
		print("YES")
	else:
		print("NO")
