import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
for _ in range(int(input())):
	n,W=map(int,input().split())
	w=list(map(int,input().split()))
	a=[]
	sum1=0
	if max(w)<=W and max(w)>=math.ceil(W/2):
		a.append(w.index(max(w))+1)
		print(1)
		print(*a)
	else:
		for i in range(n):
			sum1+=w[i]
			if sum1<=W:
				a.append(i+1)
			else:
				sum1-=w[i]
		if sum1>=math.ceil(W/2):
			print(len(a))
			print(*a)
		else:
			print(-1)
