import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	if k%2==n%2 and k**2<=n:
		print("YES")
	else:
		print("NO")


