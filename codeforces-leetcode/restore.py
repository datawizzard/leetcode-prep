import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def Siev(n): 
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n):  
		if (prime[p] == True): 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	arr1=[]
	for p in range(2, n+1): 
		if prime[p]: 
			arr1.append(p)
	return arr1
x=Siev(4000000)
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	#print(x)
	m=x[:n]
	print(m)
	r = [[arr[i],m[i]] for i in range(n)]
	#print(r)
	for i in r[:n]:
		for j in r[1:]:
			if i[0]==j[0]:
				i[1]=max(j[1],i[1])
	a=[]
	for i,j in r:
		a.append(j)
	print(*a)


			
