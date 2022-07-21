import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,m,r,c=map(int,input().split())
	print(max((r-1)+(c-1),(n-r)+(m-c),(r-1)+(m-c),(n-r)+(c-1)))