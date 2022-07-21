import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	a=[]
	for i in range(4*n,0,-2):
		a.append(i)
	print(*a[:n])