import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	i,j=0,0
	x=[0]*(4*n-1)
	y=[0]*(4*n-1)
	for _ in range(4*n-1):
		x[i],y[i]=map(int,input().split())
		i+=1
		j+=1
	d={}
	f={}
	for i in x:
		d[i]=0
	for j in y:
		f[j]=0
	for i in x:
		d[i]+=1
	for j in y:
		f[j]+=1
	for keys,values in d.items():
		if values%2==1:
			cx=keys
	for keys,values in f.items():
		if values%2==1:
			cy=keys
	print(cx,cy)
		




