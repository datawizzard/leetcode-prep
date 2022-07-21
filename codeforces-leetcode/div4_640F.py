import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n0,n1,n2=map(int,input().split())
	if n1==0:
		if n0==0:print('1'*(n2+1))
		else:
			print('0'*(n0+1))
	else:
		print('0'*(n0+1)+'1'*(n2+1)+'01'*((n1-1)//2)+'0'*((n1-1)%2))
