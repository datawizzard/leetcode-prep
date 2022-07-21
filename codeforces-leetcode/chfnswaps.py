import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	d={}
	f={}
	a.sort()
	b.sort()
	for i in a:
		d[i]=0
	for i in b:
		f[i]=0
	for i in a:
		d[i]+=1
	for i in b:
		f[i]+=1
	print(d)
	print(f)
	ans=0
	if d==f:
		print(0)
	else:
		for key,value in d.items():
			if key in f and (f[key]+d[key])%2==0 and f[key]!=1 and d[key]!=1
			

				






