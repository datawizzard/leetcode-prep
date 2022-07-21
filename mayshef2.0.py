import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	N,Q=map(int,input().split())
	s=input()
	d={}
	for i in range(N):
			d[s[i]]=0
	for i in range(N):
			d[s[i]]+=1
	for _ in range(Q):
		ans=0
		c=int(input())
		for i in d.values():
			if i>c:
				ans+=i-c
		print(ans)