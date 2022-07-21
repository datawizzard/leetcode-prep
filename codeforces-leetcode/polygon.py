import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,m=list(map(int,input().split()))
	if n%m==0:
		print("YES")
	else:
		print("NO")
