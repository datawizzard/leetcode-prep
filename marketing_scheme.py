import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	l,r=map(int,input().split())
	if r<2*l:
		print("YES")
	else:
		print("No")
