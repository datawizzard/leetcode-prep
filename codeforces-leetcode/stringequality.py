import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	a=input()
	b=input()
	d={}
	f={}
	ans="NO"
	for i in a:
		if i not in d:
			d[i]=1
		else:
			d[i]+=1
	for i in b:
		if i not in f:
			f[i]=1
		else:
			f[i]+=1
	if len(d)==len(f):
		for i,j in zip(d,f):
			if ord(i)<ord(j) and d[i]==f[j] and d[i]>=2:
				ans="YES"
	print(ans)


