import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	d={}
	res={}
	for i in arr:
		if i not in d:
			d[i]=1
		else:
			d[i]+=1
	#print(d)
	if all(d[i]>1 for i in d):
		print(-1)
	else:
		res={key:val for key,val in d.items() if not (isinstance(val,int) and (val>1))} 
		#print(res)
		x=min(res.keys())
		#print(x)
		for i in range(n):
			if arr[i]==x:
				print(i+1)




