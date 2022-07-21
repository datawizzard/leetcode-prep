import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	n,W=map(int,input().split())
	w=list(map(int,input().split()))
	a=[]
	s=0
	for i in range(n):
		if w[i]<=W and w[i]>=math.ceil(W/2):
			a=[i+1]
			s=w[i]
			break;
		else:
			s+=w[i]
			if s>W:
				s-=w[i]
			else:
				a.append(i+1)
				if s>=math.ceil(W/2):
					break;
	if s>=math.ceil(W/2):
		print(len(a))
		print(*a)
	else:
		print(-1)
