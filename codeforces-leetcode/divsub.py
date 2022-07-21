import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	if n==1:
		ans=0
	elif n==2:
		ans=1
	elif n==3:
		ans=2
	elif n%2==0:
		ans=2
	elif n%2==1:
		ans=3
	print(ans)