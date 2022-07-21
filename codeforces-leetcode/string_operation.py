import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k = map(int,input().split())
	l = 2*k - n - 1
	for i in range(1,l+1):
		print(i,end=" ")
	for j in range(k,l,-1):
		print(j, end=" ")
	print()
	