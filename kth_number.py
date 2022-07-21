import sys
import math
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	a,b,k=map(int,input().split())
	j=0
	store=[0]*(b-a+1)
	num=0
	for i in range(a,b+1):
		flag=0
		prod=1
		num=i
		while num>0:
			if num%10!=0:
				prod=prod*(num%10)
				num=num//10
			else:
				flag=1
				break
		sr=math.sqrt(prod)
		if sr-math.floor(sr)==0 and flag==0:
			store[j]=i
			j+=1
	if j<k:
		print(-1)
	else:
		print(store[k-1])
	

