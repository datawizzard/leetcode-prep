import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
if n==1:
	print(float(1))
else:
	sum1=0
	while n!=0:
		sum1+=1/n
		n-=1
	print(sum1)