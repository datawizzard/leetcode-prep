import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	d={}
	f={}
	for i in arr:
		if i not in d:
			d[i]=1
		else:
			d[i]+=1
	for i in d.values():
		if i not in f:
			f[i]=1
		else:
			f[i]+=1
	print(f)
	it = max(f.items(), key=lambda x: x[1])
	listofk=list()
	for key, value in f.items():
		if value == it[1]:
			listofk.append(key)
	print(min(listofk))

	
