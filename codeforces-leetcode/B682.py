import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	if len(arr)!=len(set(arr)):
		print("YES")
	else:
		print("NO")
