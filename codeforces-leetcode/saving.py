import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	a,b=map(int,input().split())
	n=input()
	l=len(n)
	count=0
	for i in n:
		if i=='1':
			count+=1
	#print(n)
	#print(count)
	if a<=b:
		print(a*count)
	elif 2*count>=l:
		pos=[0]*count
		p=0
		for i in range(l):
			if n[i]=='1':
				pos[p]=i
				p+=1
		print(pos)
		cost=0
		for i in range(1,count):
			if pos[i]-pos[i-1]==2:
				x=pos[i]-pos[i-1]-1
				cost+=b*x
		print(cost+a)
	else:
		print(a*count)






