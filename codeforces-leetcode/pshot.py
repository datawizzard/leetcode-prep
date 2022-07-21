import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	a=list(input())
	s,s1,c1,c2,flag=0,0,n,n,0
	for i in range(2*n):
		if i%2==0:
			s=s+int(a[i])
			c1=c1-1
		else:
			s1=s1+int(a[i])
			c2=c2-1
		if s>s1+c2 or s1>s+c1:
			print(i+1)
			flag=1
			break;
	if flag==0:
		print(2*n)



