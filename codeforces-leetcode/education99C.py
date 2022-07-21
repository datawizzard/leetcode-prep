import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	ans=0
	while n>0:
		ans+=1
		n-=ans
	if n==-1:
		ans+=1
	print(ans)
	
