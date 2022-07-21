import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	for _ in range(int(input())):
		r=int(int(input()))
		if arr[0]==1:
			